from MySolution import arabicToRoman

def test_atr_000():
    """These are some normal numbers."""
    assert arabicToRoman(1) == "I"
    assert arabicToRoman(3) == "III"
    assert arabicToRoman(4) == "IV"
    assert arabicToRoman(9) == "IX"
    assert arabicToRoman(48) == "XLVIII"
    assert arabicToRoman(999) == "CMXCIX"

def test_atr_001():
    pass
