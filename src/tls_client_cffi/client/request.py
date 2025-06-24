from typing import Any


class Request:
    def __init__(
            self,
            method: str,
            url: str,
            params: dict[str, str] = None,
            data: Any | None = None,
            headers: dict[str, str] = None,
            cookies: dict[str, str] = None,
            auth=None,  # ?
            timeout: float = None,
            allow_redirects: bool = True,
            hooks=None,  # ?
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
    ):
        # self.follow_redirects = follow_redirects
        # self.force_http1 = force_http1
        # self.header_order = header_order
        # self.headers = headers
        # self.insecure_skip_verify = insecure_skip_verify
        # self.is_byte_request = is_byte_request
        # self.is_byte_response = is_byte_response
        # self.is_rotating_proxy = is_rotating_proxy
        # self.proxy_url = proxy_url
        # self.request_body = request_body
        # self.request_cookies = request_cookies
        # self.request_host_override = request_host_override
        # self.request_method = request_method
        # self.request_url = request_url
        # self.server_name_overwrite = server_name_overwrite
        # self.stream_output_block_size = stream_output_block_size
        # self.stream_output_eof_symbol = stream_output_eof_symbol
        # self.stream_output_path = stream_output_path
        # self.timeout_milliseconds = timeout_milliseconds
        # self.timeout_seconds = timeout_seconds
        self.method = method
        self.url = url
        self.params = params
        self.data = data
        self.headers = headers
        self.cookies = cookies
        self.auth = auth
        self.timeout = timeout
        self.allow_redirects = allow_redirects
        self.hooks = hooks
        self.verify = verify
        self.json = json

        self.force_http1 = force_http1
        self.header_order = header_order
        self.proxy_url = proxy_url
        self.request_host_override = request_host_override
        self.server_name_overwrite = server_name_overwrite

        self.stream_output_block_size = stream_output_block_size
        self.stream_output_eof_symbol = stream_output_eof_symbol
        self.stream_output_path = stream_output_path

