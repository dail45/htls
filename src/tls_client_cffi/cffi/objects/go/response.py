import json

import humps

from . import GoObject
from .go_exception import GoException

"""
{
  "id": "some response identifier",
  "sessionId": "some reusable sessionId if provided on the request",
  "status": 200,
  "target": "the target url",
  "body": "The Response as string here or the error message",
  "headers": {},
  "cookies": {}
}
"""
class Response(GoObject):
    def __init__(
            self,
            id: str,
            session_id: str = "",
            status: int = 0,
            target: str = "",
            body: str = "",
            headers: dict[str, str] = None,
            cookies: dict[str, str] = None,
            used_protocol: str = ""
    ):
        super().__init__(id)
        self.session_id = session_id
        self.status = status
        self.target = target
        self.body = body
        self.headers = headers or {}
        self.cookies = cookies or {}
        self.used_protocol = used_protocol

        self._exception = GoException(self.body) if self.status == 0 else None

    @classmethod
    def from_bytes(cls, byte_string: bytes):
        data = json.loads(byte_string)
        data = {humps.decamelize(k): v for k, v in data.items()}
        return cls(**data)

    def raise_for_exception(self):
        if self._exception:
            raise self._exception
