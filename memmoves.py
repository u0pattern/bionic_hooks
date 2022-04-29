from androidemu.emulator import Emulator
from androidemu.java.helpers.native_method import native_method
from androidemu.utils import memory_helpers

emulator = Emulator()

@native_method
def memmoves(mu, data, block):

    if len(memory_helpers.read_ptr(my, data)) > 96 :
        check = None
        
    des = memory_helpers.read_utf8(mu, data)
    chunk = memory_helpers.read_utf8(mu, block)

    if check is None:
        memory_helpers.write_utf8(
            mu,
            data,
            b"HOOKED\x00"
        )
    else:
        mu.mem_write(
            data,
            bytes((des % (chunk, 96)).encode('utf-8'))
        )

emulator.modules.add_symbol_hook(
    'memmoves',
    emulator.hooker.write_function(memmoves) + 1
)
