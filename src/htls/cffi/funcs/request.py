import json
import asyncio

import humps

from ...cffi_loader import request as go_request
from ..objects import Request, Response


def request(request: Request) -> Response:
    payload = json.dumps(humps.camelize(request.to_payload()), separators=(',', ':')).encode('utf-8')
    response = go_request(payload)
    response = Response.from_bytes(response)

    return response


_go_request = request


async def async_request(request: Request) -> Response:
    return await asyncio.get_event_loop().run_in_executor(None, _go_request, request)
