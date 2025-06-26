from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tls_client_cffi.client import PreparedRequest


class AuthBase:
    """
    this class was copied from requests library
    Base class that all auth implementations derive from
    """

    def __call__(self, r: "PreparedRequest") -> "PreparedRequest":
        raise NotImplementedError("Auth hooks must be callable.")
