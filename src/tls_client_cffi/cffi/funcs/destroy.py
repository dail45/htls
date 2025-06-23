import json

from ...cffi_loader import destroySession, destroyAll
from ..objects.go import DestroySessionObject


def destroy_session(session_id: str) -> DestroySessionObject:
    payload = {"sessionId": session_id}
    result = destroySession(json.dumps(payload).encode("utf-8"))
    return DestroySessionObject.from_bytes(result)


def destroy_all() -> DestroySessionObject:
    result = destroyAll()
    return DestroySessionObject.from_bytes(result)
