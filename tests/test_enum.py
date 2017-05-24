from collections import OrderedDict

import pytest

from venum import Enum


DATA = OrderedDict([
    ('SPADES', 1),
    ('PI', 3.141592),
    ('HTML', 'text/html; charset=utf-8'),
])


class TestEnum:
    def test_correct_values(self):
        enum = Enum(*[(key, DATA[key]) for key in DATA])
        assert enum.SPADES == DATA['SPADES']
        assert enum.PI == DATA['PI']
        assert enum.HTML == DATA['HTML']

    def test_correct_order(self):
        enum = Enum(*[(key, DATA[key]) for key in DATA])
        assert list(enum._fields) == list(DATA.keys())

    def test_duplicate_field(self):
        with pytest.raises(ValueError):
            Enum(('BLUE', 1), ('RED', 2), ('BLUE', 0))

    def test_immutable(self):
        enum = Enum(*[(key, DATA[key]) for key in DATA])

        with pytest.raises(AttributeError):
            enum.PI = 3.14

    def test_name(self):
        enum = Enum(*[(key, DATA[key]) for key in DATA], name='DATA')
        assert str(enum)[:4] == 'DATA'

    def test_name_default(self):
        enum = Enum(*[(key, DATA[key]) for key in DATA])
        assert str(enum)[:4] == 'Enum'
