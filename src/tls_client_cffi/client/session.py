import base64
import time
import uuid
from datetime import timedelta
from typing import Any

from tls_client_cffi import CustomTLSClient
from tls_client_cffi.cffi.objects.request import TransportOptions, Request as TLSRequest
from tls_client_cffi.cffi.funcs import request as do_tls_request
from tls_client_cffi.client import Response
from tls_client_cffi.client.prepared_request import PreparedRequest
from tls_client_cffi.client.request import Request


class Session:
    def __init__(
            self,
            tls_client_identifier: str = "",
            custom_tls_client: CustomTLSClient | dict | None = None,

            catch_panics: bool = False,
            certificate_pinning_hosts: dict | None = None,
            transport_options: TransportOptions | dict | None = None,
            default_headers: dict[str, list[str]] | None = None,
            connect_headers: dict[str, list[str]] | None = None,
            disable_ipv6: bool = False,
            disable_ipv4: bool = False,
            local_address: str | None = None,
            session_id: str | None = None,
            with_debug: bool = False,
            with_default_cookie_jar: bool = False,
            without_cookie_jar: bool = False,
            with_random_tls_extension_order: bool = False
    ):
        self.catch_panics = catch_panics
        self.certificate_pinning_hosts = certificate_pinning_hosts
        self.custom_tls_client = custom_tls_client
        self.transport_options = transport_options
        self.default_headers = default_headers
        self.connect_headers = connect_headers
        self.disable_ipv6 = disable_ipv6
        self.disable_ipv4 = disable_ipv4
        self.local_address = local_address
        self.session_id = str(session_id) or str(uuid.uuid4())
        self.tls_client_identifier = tls_client_identifier
        self.with_debug = with_debug
        self.with_default_cookie_jar = with_default_cookie_jar
        self.without_cookie_jar = without_cookie_jar
        self.with_random_tls_extension_order = with_random_tls_extension_order

    def send(self, prep: PreparedRequest):
        params = {}
        params.update(self.__dict__)
        params.update(prep.tls_params)
        params.update({
            "headers": prep.headers,
            "request_body": base64.b64encode(prep.body).decode("utf-8") if prep.body else None,
            "request_method": prep.method,
            "request_url": prep.url
        })

        tls_request = TLSRequest(**params)
        tls_response = do_tls_request(tls_request)
        rsp = Response()
        rsp.build_response(prep, tls_response)

        return rsp

    def prepare_request(self, request: Request) -> PreparedRequest:
        prep = PreparedRequest()
        prep.prepare_request(request)
        return prep

    def request(
            self,
            method: str,
            url: str,
            params: dict[str, str] = None,
            data: Any | None = None,
            headers: dict[str, str] = None,
            cookies: dict[str, str] = None,
            auth=None,
            timeout: float = None,
            allow_redirects: bool = True,
            hooks=None,
            verify: bool = False,
            json: dict | list | None = None,

            force_http1: bool = False,
            header_order: list[str] | None = None,
            proxy_url: str | None = None,
            request_host_override: str | None = None,
            server_name_overwrite: str | None = None,

            stream_output_block_size: int | None = None,
            stream_output_eof_symbol: str | None = None,
            stream_output_path: str | None = None,

            return_request: bool = False
    ):
        request = Request(method, url, params, data, headers, cookies, auth, timeout, allow_redirects, hooks, verify,
                          json, force_http1, header_order, proxy_url, request_host_override, server_name_overwrite,
                          stream_output_block_size, stream_output_eof_symbol, stream_output_path)
        if return_request:
            return request

        prep = self.prepare_request(request)

        start = time.time()
        rsp = self.send(prep)
        elapsed = time.time() - start
        rsp.elapsed = timedelta(seconds=elapsed)

        return rsp

