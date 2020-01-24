from MySolution import arabicToRoman

def test_atr_001():
    assert arabicToRoman(3) == "III"

def test_atr_002():
    assert arabicToRoman(4) == "IV"
