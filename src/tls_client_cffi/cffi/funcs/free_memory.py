from ...cffi_loader import freeMemory


def free_memory(id: str) -> None:
    freeMemory(id.encode("utf-8"))
