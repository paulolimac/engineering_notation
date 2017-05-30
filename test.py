import pytest
from engineering_notation import EngNumber, EngUnit, __version__


def test_import_version():
    assert __version__
    assert len(__version__.split('.')) == 3


''' tests for EngNum '''


def test_enum_to_str_large():
    assert str(EngNumber('220k')) == '220k'
    assert str(EngNumber('220000')) == '220k'
    assert str(EngNumber(220000)) == '220k'
    assert str(EngNumber(220000.00)) == '220k'
    assert str(EngNumber(220001.25)) == '220k'


def test_enum_to_str_small():
    assert str(EngNumber('220m')) == '220m'
    assert str(EngNumber('0.220')) == '220m'
    assert str(EngNumber(0.220)) == '220m'
    assert str(EngNumber(0.220000125)) == '220m'


def test_enum_add():
    assert str(EngNumber('220m') + EngNumber('10m')) == '230m'
    assert str(EngNumber('220m') + 0.01) == '230m'
    assert str(0.01 + EngNumber('220m')) == '230m'

    assert str(EngNumber('220m') + EngNumber('220u')) == '220.22m'
    assert str(EngNumber('220m') + EngNumber('220n')) == '220m'


def test_enum_sub():
    assert str(EngNumber('220m') - EngNumber('10m')) == '210m'
    assert str(EngNumber('220m') - 0.01) == '210m'

    assert str(EngNumber('220m') - EngNumber('220u')) == '219.78m'
    assert str(EngNumber('220m') - EngNumber('220n')) == '220m'

    assert str(0.220 - EngNumber('0.01')) == '210m'


def test_enum_mul():
    assert str(EngNumber('220m') * EngNumber('2')) == '440m'
    assert str(EngNumber('220m') * 2) == '440m'
    assert str(EngNumber('220m') * 2.0) == '440m'

    assert str(2 * EngNumber('220m')) == '440m'
    assert str(2.0 * EngNumber('220m')) == '440m'


def test_enum_div():
    assert str(EngNumber('220m') / EngNumber('2')) == '110m'
    assert str(EngNumber('220m') / 2) == '110m'
    assert str(EngNumber('220m') / 2.0) == '110m'

    assert str(2 / EngNumber('220m')) == '9.09'
    assert str(2.0 / EngNumber('220m')) == '9.09'


def test_enum_eq():
    assert EngNumber('220k') == EngNumber(220000)
    assert EngNumber('220k') == 220000
    assert EngNumber('220k') == 220000.0

    assert 220000 == EngNumber('220k')
    assert 220000.0 == EngNumber('220k')


def test_enum_gt():
    assert EngNumber('220k') > 219000


def test_enum_lt():
    assert EngNumber('220k') < 221000


def test_enum_ge():
    assert EngNumber('220k') >= 219000
    assert EngNumber('220k') >= 220000


def test_enum_le():
    assert EngNumber('220k') <= 221000
    assert EngNumber('220k') <= 220000


''' tests for EngUnit()'''


def test_to_str():
    assert str(EngUnit('220') == '220')
    assert str(EngUnit('220ohm') == '220ohm')


def test_to_str_large():
    assert str(EngUnit('220kHz')) == '220kHz'
    assert str(EngUnit('220000')) == '220k'
    assert str(EngUnit(220000)) == '220k'
    assert str(EngUnit(220000.00)) == '220k'
    assert str(EngUnit(220001.25)) == '220k'


def test_to_str_small():
    assert str(EngUnit('220mohm')) == '220mohm'
    assert str(EngUnit('0.220')) == '220m'
    assert str(EngUnit(0.220)) == '220m'
    assert str(EngUnit(0.220000125)) == '220m'


def test_add():
    assert str(EngUnit('220mHz') + EngUnit('10mHz')) == '230mHz'
    assert str(EngUnit('220mohm') + EngUnit('220uohm')) == '220.22mohm'
    assert str(EngUnit('220m') + EngUnit('220n')) == '220m'

    assert str(EngUnit('220m') + 0.01) == '230m'
    assert str(0.01 + EngUnit('220m')) == '230m'

    with pytest.raises(AttributeError):
        EngUnit('220mHz') + EngUnit('10m')
    with pytest.raises(AttributeError):
        EngUnit('10m') + EngUnit('220mHz')


def test_sub():
    assert str(EngUnit('220mHz') - EngUnit('10mHz')) == '210mHz'
    assert str(EngUnit('220mohm') - EngUnit('220uohm')) == '219.78mohm'
    assert str(EngUnit('220m') - EngUnit('220n')) == '220m'

    assert str(EngUnit('220m') - 0.01) == '210m'
    assert str(0.220 - EngUnit('0.01')) == '210m'

    with pytest.raises(AttributeError):
        EngUnit('220mHz') - EngUnit('10m')
    with pytest.raises(AttributeError):
        EngUnit('10m') - EngUnit('220mHz')
    with pytest.raises(AttributeError):
        10.0 - EngUnit('220mHz')


def test_mul():
    assert str(EngUnit('220ms') * EngUnit('2Hz')) == '440msHz'
    assert str(EngUnit('220ms') * EngUnit('2')) == '440ms'
    assert str(EngUnit('220m') * EngUnit('2s')) == '440ms'

    assert str(EngUnit('220ms') * 2) == '440ms'
    assert str(EngUnit('220ms') * 2.0) == '440ms'

    assert str(2 * EngUnit('220ms')) == '440ms'
    assert str(2.0 * EngUnit('220ms')) == '440ms'


def test_div():
    assert str(EngUnit('220ms') / EngUnit('2s')) == '110ms/s'
    assert str(EngUnit('220ms') / EngUnit('2')) == '110ms'
    assert str(EngUnit('220m') / EngUnit('2s')) == '110m/s'

    assert str(EngUnit('220ms') / 2) == '110ms'
    assert str(EngUnit('220ms') / 2.0) == '110ms'

    assert str(2 / EngUnit('220ms')) == '9.09/s'
    assert str(2.0 / EngUnit('220ms')) == '9.09/s'


def test_eq():
    assert EngUnit('220k') == EngUnit(220000)
    assert EngUnit('220k') == 220000
    assert EngUnit('220k') == 220000.0

    assert 220000 == EngUnit('220k')
    assert 220000.0 == EngUnit('220k')

    with pytest.raises(AttributeError):
        EngUnit('220mHz') == EngUnit('0.220ohm')
    with pytest.raises(AttributeError):
        EngUnit('220mHz') == 10
    with pytest.raises(AttributeError):
        EngUnit('220mHz') == 10.0


def test_gt():
    assert EngUnit('220kohm') > EngUnit('219000ohm')

    with pytest.raises(AttributeError):
        EngUnit('220kohm') > 219000


def test_lt():
    assert EngUnit('220kohm') < EngUnit('221000ohm')

    with pytest.raises(AttributeError):
        EngUnit('220kohm') < 221000


def test_ge():
    assert EngUnit('220kohm') >= EngUnit('219000ohm')
    assert EngUnit('220kohm') >= EngUnit('220000ohm')

    with pytest.raises(AttributeError):
        EngUnit('220kohm') >= 219000


def test_le():
    assert EngUnit('220kohm') <= EngUnit('221000ohm')
    assert EngUnit('220kohm') <= EngUnit('220000ohm')

    with pytest.raises(AttributeError):
        EngUnit('220kohm') >= 219000
    with pytest.raises(AttributeError):
        219000 >= EngUnit('220kohm')
