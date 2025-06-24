from typing import Mapping
from urllib.parse import urlparse, urlencode, urlunparse

import idna
from requests.utils import requote_uri

from tls_client_cffi.client.exceptions import MissingSchema, InvalidURL
from tls_client_cffi.client.request import Request


class PreparedRequest:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = None
        self.body = None
        self.hooks = None

    @staticmethod
    def _encode_params(data):
        # this method was copied from requests library
        if isinstance(data, (str, bytes)):
            return data
        elif hasattr(data, "read"):
            return data
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
        self.method = request.method.upper()
        self.prepare_url(request.url, request.params)
        ...

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
            f"{result.username}{':' + result.password if result.password else ''}",
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

        url = requote_uri(urlunparse([scheme, netloc, path, None, query, fragment]))
        self.url = url
