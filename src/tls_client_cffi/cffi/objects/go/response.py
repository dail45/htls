import json

import humps

from . import GoObject

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
            session_id: str,
            status: int,
            target: str,
            body: str,
            headers: dict[str, str],
            cookies: dict[str, str],
            used_protocol: str
    ):
        super().__init__(id)
        self.session_id = session_id
        self.status = status
        self.target = target
        self.body = body
        self.headers = headers
        self.cookies = cookies
        self.used_protocol = used_protocol

    @classmethod
    def from_bytes(cls, byte_string: bytes):
        data = json.loads(byte_string)
        data = {humps.decamelize(k): v for k, v in data.items()}
        return cls(**data)
