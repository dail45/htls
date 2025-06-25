import urllib.request
from http.cookiejar import CookieJar, Cookie
from typing import Mapping
from urllib.parse import urlparse, urlencode, urlunparse, quote
from json import dumps

import idna

from tls_client_cffi.client import CaseInsensitiveDict
from tls_client_cffi.client.exceptions import MissingSchema, InvalidURL, InvalidJSONError
from tls_client_cffi.client.request import Request
from tls_client_cffi.client.utils import unquote_unreserved


class PreparedRequest:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = None
        self.body = None
        self.tls_params = {}
        self.raw_request = None

        self._cookies = None

    @staticmethod
    def _encode_params(data):
        # this method was copied from requests library
        if isinstance(data, (str, bytes)):
            return data
        elif hasattr(data, "read"):
            # change because this library don't support readable body
            return data.read()
        elif hasattr(data, "__iter__"):
            result = []
            if isinstance(data, Mapping):
                data = list(data.items())
            for k, vs in data:
                if isinstance(vs, (str, bytes)) or not hasattr(vs, "__iter__"):
                    vs = [vs]
                for v in vs:
                    if v is not None:
                        result.append(
                            (
                                k.encode("utf-8") if isinstance(k, str) else k,
                                v.encode("utf-8") if isinstance(v, str) else v,
                            )
                        )
            return urlencode(result, doseq=True)
        else:
            return data

    def prepare_request(self, request: Request):
        self.prepare_method(request.method)
        self.prepare_url(request.url, request.params)
        self.prepare_headers(request.headers)
        self.prepare_cookies(request.cookies)
        self.prepare_body(request.data, request.json)
        self.prepare_tls_params(request)

        self.raw_request = request

    def prepare_method(self, method):
        # this method was partially copied from requests library
        if isinstance(method, bytes):
            self.method = method.decode("utf8")
        else:
            self.method = str(method)
        self.method.upper()

    def prepare_url(self, url, params):
        # this method was partially copied from requests library
        if isinstance(url, bytes):
            url = url.decode("utf8")
        else:
            url = str(url)
        url = url.lstrip()

        if ":" in url and not url.lower().startswith("http"):
            self.url = url
            return

        result = urlparse(url)
        scheme, auth, host, port, path, query, fragment = (
            result.scheme,
            f"{result.username}{':' + result.password if result.password else ''}" if result.username else None,
            result.hostname,
            result.port,
            result.path,
            result.query,
            result.fragment,
        )
        if not scheme:
            raise MissingSchema(
                f"Invalid URL {url!r}: No scheme supplied. "
                f"Perhaps you meant https://{url}?"
            )

        if not host:
            raise InvalidURL(f"Invalid URL {url!r}: No host supplied")

        is_ascii = True
        try:
            host.encode('ascii')
        except UnicodeEncodeError:
            is_ascii = False

        if not is_ascii:
            try:
                host = idna.encode(host, uts46=True).decode('utf-8')
            except idna.IDNAError:
                raise InvalidURL("URL has an invalid label.")
        elif host.startswith(("*", ".")):
            raise InvalidURL("URL has an invalid label.")

        netloc = auth or ""
        if netloc:
            netloc += "@"
        netloc += host
        if port:
            netloc += f":{port}"

        if not path:
            path = "/"

        if isinstance(params, (str, bytes)):
            if isinstance(params, bytes):
                params = params.decode("ascii")

        enc_params = self._encode_params(params)
        if enc_params:
            if query:
                query = f"{query}&{enc_params}"
            else:
                query = enc_params

        uri = urlunparse([scheme, netloc, path, None, query, fragment])
        safe_with_percent = "!#$%&'()*+,/:;=?@[]~"
        safe_without_percent = "!#$&'()*+,/:;=?@[]~"
        try:
            url = quote(unquote_unreserved(uri), safe=safe_with_percent)
        except InvalidURL:
            url = quote(uri, safe=safe_without_percent)
        self.url = url

    def prepare_headers(self, headers):
        """
        # this method was partially copied from requests library
        Prepares the given HTTP headers.
        """

        self.headers = CaseInsensitiveDict()
        if headers:
            for header in headers.items():
                # Raise exception on invalid header value.
                name, value = header
                self.headers[str(name)] = value

    def prepare_cookies(self, cookies):
        # this method was partially copied from requests library
        cookies = cookies or {}

        if isinstance(cookies, CookieJar):
            self._cookies = cookies
        else:
            self._cookies = CookieJar()
            for k, v in cookies.items():
                self._cookies.set_cookie(Cookie(
                    version=0,
                    name=k,
                    value=v,
                    port=None,
                    port_specified=False,
                    domain="",
                    domain_specified=False,
                    domain_initial_dot=False,
                    path="/",
                    path_specified=False,
                    secure=False,
                    expires=None,
                    discard=True,
                    comment=None,
                    comment_url=None,
                    rest={"HttpOnly": None},
                    rfc2109=False
                ))

    def prepare_body(self, data, json):
        # this method was partially copied from requests library
        body = None
        content_type = None

        if not data and json is not None:
            content_type = "application/json"

            try:
                body = dumps(json, allow_nan=False)
            except ValueError as ve:
                raise InvalidJSONError(ve)

            if not isinstance(body, bytes):
                body = body.encode("utf-8")

        if data:
            body = self._encode_params(data)
            if isinstance(data, (str, bytes)):
                content_type = None
            else:
                content_type = "application/x-www-form-urlencoded"

        self.prepare_content_length(body)
        if content_type and ("content-type" not in self.headers):
            self.headers["Content-Type"] = content_type

        self.body = body

    def prepare_content_length(self, body):
        # this method was partially copied from requests library
        if body is not None:
            length = len(body)
            if length:
                self.headers["Content-Length"] = str(length)
        elif (
                self.method not in ("GET", "HEAD")
                and self.headers.get("Content-Length") is None
        ):
            self.headers["Content-Length"] = "0"

    def prepare_tls_params(self, request: Request):
        cookie: Cookie
        cookies = [{
            "domain": int(cookie.domain or 0),
            "expires": int(cookie.expires or 0),
            "maxAge": 0,
            "name": cookie.name,
            "path": cookie.path,
            "value": cookie.value
        } for cookie in self._cookies]

        self.tls_params.update({
            "follow_redirects": request.allow_redirects,
            "force_http1": request.force_http1,
            "header_order": request.header_order,
            "insecure_skip_verify": request.verify,
            "is_byte_request": True,
            "is_byte_response": True,
            "is_rotating_proxy": False,
            "proxy_url": request.proxy_url,
            "request_cookies": cookies,
            "request_host_override": request.request_host_override,
            "server_name_overwrite": request.server_name_overwrite,
            "stream_output_block_size": request.stream_output_block_size,
            "stream_output_eof_symbol": request.stream_output_eof_symbol,
            "stream_output_path": request.stream_output_path,
            "timeout_milliseconds": 0,
            "timeout_seconds": request.timeout
        })
