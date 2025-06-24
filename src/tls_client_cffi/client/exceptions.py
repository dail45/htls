from tls_client_cffi import TLSClientException


class InvalidURL(TLSClientException, ValueError):
    pass


class MissingSchema(TLSClientException, ValueError):
    pass
