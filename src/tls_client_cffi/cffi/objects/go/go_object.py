import json

import humps

from .... import cffi


class GoObject:
    def __init__(self, id: str):
        self.id = id

        self._memory_allocated = False

    def release(self):
        if self._memory_allocated:
            cffi.free_memory(self.id)
            self._memory_allocated = False

    def __del__(self):
        self.release()

    @classmethod
    def from_bytes(cls, byte_string: bytes):
        data = json.loads(byte_string)
        data = humps.decamelize(data)
        return cls(**data)
