from typing import *


# =====================================================================================================================
class PROJECT:
    # AUX --------------------------------------------------
    _VERSION_TEMPLATE: Tuple[int] = (0, 0, 2)

    # MAIN -------------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # ------------------------------------------------------
    NAME_IMPORT: str = "bit_work"
    NAME_INSTALL: str = NAME_IMPORT.replace("_", "-")
    KEYWORDS: List[str] = [
        "_field_bytearray",
        "flags", "flags manipulate",
        "bits", "bit user", "bit work", "bits manipulate",
    ]
    CLASSIFIERS_TOPICS_ADD: List[str] = [
        # "Topic :: Communications",
        # "Topic :: Communications :: Email",
    ]

    # GIT --------------------------------------------------
    DESCRIPTION_SHORT: str = "work with bits (bitfields/flags/bites...)"

    # README -----------------------------------------------
    pass

    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_LONG: str = """
designed for common work with bitfields-like objects
    """
    FEATURES: List[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "Flags",
        "Bits",
    ]

    # HISTORY -----------------------------------------------
    VERSION: Tuple[int, int, int] = (0, 0, 0)
    VERSION_STR: str = ".".join(map(str, VERSION))
    TODO: List[str] = [
        "..."
    ]
    FIXME: List[str] = [
        "..."
    ]
    NEWS: List[str] = [
        "..."
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
