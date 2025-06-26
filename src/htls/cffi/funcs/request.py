import json

import humps

from ...cffi_loader import request as go_request
from ..objects import Request, Response


def request(request: Request):
    payload = json.dumps(humps.camelize(request.to_payload()), separators=(',', ':')).encode('utf-8')
    response = go_request(payload)
    response = Response.from_bytes(response)

    return response
