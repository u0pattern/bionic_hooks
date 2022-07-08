from androidemu.emulator import Emulator
from androidemu.java.helpers.native_method import native_method
from androidemu.utils import memory_helpers

emulator = Emulator()

@native_method
def getenv(mu, ref):
    if b"LD_PRELOAD" in memory_helpers.read_ptr(mu, ref):
        memory_helpers.write_utf8(
            mu,
            memory_helpers.read_utf8(mu, ref),
            b"LD_LIBRARY_PATH\x00"
        )

emulator.modules.add_symbol_hook(
    'getenv',
    emulator.hooker.write_function(getenv) + 1
)
