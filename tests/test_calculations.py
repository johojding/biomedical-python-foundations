from pytest import approx, raises
from biocalc import bmi, bsa, zscore, si_unit_conversion, bmi_range, bsa_range

def test_normal_bmi():
    actual = bmi(58, 1.70)
    expected = 20.0692
    assert actual == approx(expected, rel=1e-6)

def test_invalid_bmi_type():
    with raises(TypeError):
        bmi("58", 1.70)

def test_valueerror_bmi():
    with raises(ValueError):
        bmi(0, 1.70)

def test_normal_bsa():
    actual = bsa(58, 170, "mosteller")
    expected = 1.6549
    assert actual == approx(expected, rel=1e-4)

def test_invalid_bsa_method():
    with raises(ValueError):
        bsa(58, 170, "invalid")


def test_normal_zscore():
    actual = zscore(5, 1, 1)
    expected = 4
    assert actual == expected

def test_invalid_zscore():
    with raises(ValueError):
        zscore(5, 1, 0)

def test_normal_si_unit_conversion():
    actual = si_unit_conversion(100, "cm")
    expected = 1
    assert actual == expected

def test_invalid_si_unit_type():
    with raises(TypeError):
        si_unit_conversion(100, 0)

def test_normal_bmi_range():
    actual = bmi_range(20)
    expected = "normal"
    assert actual == expected

def test_edge_bmi_range():
    actual = bmi_range(29.9)
    expected = "overweight"
    assert actual == expected

def test_normal_bsa_range():
    actual = bsa_range(1.3)
    expected = "low"
    assert actual == expected

def test_edge_bsa_range():
    actual = bsa_range(2.0)
    expected = "high"
    assert actual == expected
