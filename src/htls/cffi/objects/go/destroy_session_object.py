from . import GoObject


class DestroySessionObject(GoObject):
    def __init__(self, id: str, success: bool):
        super().__init__(id)
        self.success = success
    