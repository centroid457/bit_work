import os
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from bit_work import *


# =====================================================================================================================
class Test__Flags:
    VICTIM: Type[Flags] = type("VICTIM", (Flags,), {})

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (Flags,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__ClassMethod_and_obj(self):
        assert True


# =====================================================================================================================
