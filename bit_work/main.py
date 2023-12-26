from typing import *


# =====================================================================================================================
# TODO: need decision about flags order!!!


# =====================================================================================================================
class Exx_BitsNoSize(Exception):
    pass


class Exx_BitsOutOfRange(Exception):
    pass


# =====================================================================================================================
class Bitfield:
    """
    # ORDER for any field is NO HUMAN!!! or not???
    YOU NEED TO SEE ALWAYS AS REVERCE IN ANY REPRESENTATION!!!
    but when you indexind by obj[] used human order!!!
    """
    field_size: int = None
    _field_data: bytearray = None

    def __init__(self, field_size: int):
        if field_size < 1:
            raise Exx_BitsNoSize

        self.field_size = field_size
        self._field_data = bytearray((field_size + 7) // 8)

    # todo: clear_all+exact+several/setup_all+exact+several/ [by_pos/by_fields]
    # todo: listActiveFlags/list+iter [by_pos/by_fields]

    @property
    def field_str(self) -> str:
        """in human order"""
        return "".join(map(str, self.list()))

    def __getitem__(self, idx: int) -> Union[int, NoReturn]:
        if idx < -self.field_size or idx > self.field_size - 1:
            raise Exx_BitsOutOfRange
        return self._field_data[idx // 8] >> (idx % 8) & 1

    def __setitem__(self, idx: int, value: Union[int, bool, Any]) -> Optional[NoReturn]:
        mask = 1 << (idx % 8)
        if bool(value):
            self._field_data[idx // 8] |= mask
        else:
            self._field_data[idx // 8] &= ~mask

    def __len__(self) -> int:
        return self.field_size

    def count_ones(self) -> int:
        return bin(self.int()).count('1')

    # REPRESENTATIONS ---------------------------------------------------------------
    def list(self) -> List[int]:
        """in NOhuman order
        """
        result = []
        for index in range(self.field_size):
            result.append(self[index])
        result.reverse()
        return result

    def __str__(self) -> str:
        return f"field[{self.field_str}]"

    def int(self) -> int:
        """
        print(int(bytearray(2).hex(), 16))
        """
        return int(self._field_data.hex(), 16)

    def _bin_str(self) -> str:
        """common bin-format (without type prefix)

        print(bin(int(bytearray(2).hex())))     # 0b0
        """
        result = bin(self.int())[2:]
        result = "0" * (self.field_size - len(result)) + result
        return result

    def _hex_str(self) -> str:
        """common hex(full bytes)-format (without type prefix)
        print(bytearray(2).hex())
        """
        return self._field_data.hex()

    def __zero_try_bytearray(self):
        print(bytearray(1))
        print(bytearray(2))

        print(bin())
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
class Flags(Bitfield):
    pass


# =====================================================================================================================
class Bits(Bitfield):
    pass


# =====================================================================================================================
