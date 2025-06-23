import ctypes
import os
from sys import platform
from platform import machine

machine_type = machine()

library_platform = ""
library_arch = ""
library_version = "1.10.0"
library_ext = ""

if platform == "darwin":
    library_platform = "darwin"
    library_arch = "arm64" if machine_type == "arm64" else "amd64"
    library_ext = "dylib"
elif platform in ("win32", "cygwin"):
    library_platform = "windows"
    library_arch = "64" if 8 == ctypes.sizeof(ctypes.c_voidp) else "32"
    library_ext = "dll"
else:
    library_platform = "linux"
    if machine_type == "aarch64":
        library_arch = "arm64"
    elif "x86" in machine_type:
        library_platform = "linux-ubuntu"
        library_arch = "amd64"
    else:
        library_platform = "linux-alpine"
        library_arch = "amd64"
    library_ext = "so"


library_name = f"tls-client-{library_platform}-{library_arch}-{library_version}.{library_ext}"

root_dir = os.path.abspath(os.path.dirname(__file__))
library = ctypes.cdll.LoadLibrary(f'{root_dir}/libs/{library_name}')


request = library.request
request.argtypes = [ctypes.c_char_p]
request.restype = ctypes.c_char_p

getCookiesFromSession = library.getCookiesFromSession
getCookiesFromSession.argtypes = [ctypes.c_char_p]
getCookiesFromSession.restype = ctypes.c_char_p

addCookiesToSession = library.addCookiesToSession
addCookiesToSession.argtypes = [ctypes.c_char_p]
addCookiesToSession.restype = ctypes.c_char_p

freeMemory = library.freeMemory
freeMemory.argtypes = [ctypes.c_char_p]
freeMemory.restype = ctypes.c_void_p

destroySession = library.destroySession
destroySession.argtypes = [ctypes.c_char_p]
destroySession.restype = ctypes.c_char_p

destroyAll = library.destroyAll
destroyAll.restype = ctypes.c_char_p
