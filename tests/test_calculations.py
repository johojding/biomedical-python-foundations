from biocalc.calculations import bmi

def test_normal_bmi():
    actual = bmi(58, 1.70)
    expected = 20.0692
    assert actual == expected