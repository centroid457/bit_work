from typing import *


# =====================================================================================================================
pass


# =====================================================================================================================
class Bitfields:
    size: int = None
    bytes: bytes = None

    def __init__(self, size: int):
        self.size = size
        self.bytes = bytearray(size + 7 // 8)

    # todo: int+bytes
    # todo: len=size
    # todo: clear_all+exact+several/setup_all+exact+several/ [by_pos/by_fields]
    # todo: listActiveFlags/list+iter [by_pos/by_fields]

    def __getitem__(self, idx: int):
        return self.bytes[idx // 8] >> (idx % 8) & 1

    def __setitem__(self, idx: int, value: Union[int, bool, Any]):
        mask = 1 << (idx % 8)
        if bool(value):
            self.bytes[idx // 8] |= mask
        else:
            self.bytes[idx // 8] &= ~mask

    def count(self):
        pass

    def int(self):
        pass

        print(int(bytearray(1).hex(), 16))
        print(int(bytearray(2).hex(), 16))

    def hex(self):
        print(bytearray(1).hex())
        print(bytearray(2).hex())
        pass

    def __zero_try_bytearray(self):
        print(bytearray(1))
        print(bytearray(2))

        print(bytearray(1).hex())
        print(bytearray(2).hex())

        print(int(bytearray(1).hex(), 16))
        print(int(bytearray(2).hex(), 16))
        """
        bytearray(b'\x00')
        bytearray(b'\x00\x00')
        00
        0000
        0
        0
        """
        # print(bytearray())
        # print(bytearray(0))
        # print(bytearray(1))
        # print(bytearray(2))
        # """
        # bytearray(b'')
        # bytearray(b'')
        # bytearray(b'\x00')
        # bytearray(b'\x00\x00')
        # """


# =====================================================================================================================
class Flags(Bitfields):
    pass


# =====================================================================================================================
class Bits(Bitfields):
    pass


# =====================================================================================================================
