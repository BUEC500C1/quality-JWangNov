from MySolution import arabicToRoman


def test_atr_000():
    """These are some normal integers."""
    assert arabicToRoman(1) == "I"
    assert arabicToRoman(3) == "III"
    assert arabicToRoman(4) == "IV"
    assert arabicToRoman(9) == "IX"
    assert arabicToRoman(48) == "XLVIII"
    assert arabicToRoman(999) == "CMXCIX"


def test_atr_001():
    """These are some big integers."""
    assert arabicToRoman(1986) == "MCMLXXXVI"
    assert arabicToRoman(1996) == "MCMXCVI"
    assert arabicToRoman(2020) == "MMXX"
    assert arabicToRoman(3456) == "MMMCDLVI"


def test_atr_002():
    """These are some integers which are way too big."""
    assert arabicToRoman(49859) == -1
    assert arabicToRoman(123456) == -1


def test_atr_003():
    """These are negative integers and zero."""
    assert arabicToRoman(0) == -1
    assert arabicToRoman(-1) == -1
    assert arabicToRoman(-2) == -1
    assert arabicToRoman(-12378) == -1
    assert arabicToRoman(-6) == -1
    assert arabicToRoman(-44) == -1
    assert arabicToRoman(-259) == -1
    assert arabicToRoman(-999999999999) == -1


def test_atr_004():
    """These are some bad inputs."""
    assert arabicToRoman(1.1) == -2
    assert arabicToRoman(0.888888) == -2
    assert arabicToRoman(12.6-9127312312) == -2
    assert arabicToRoman(-23.45) == -2
    assert arabicToRoman("Hello") == -2
    assert arabicToRoman([1,]) == -2
    assert arabicToRoman((777,33)) == -2
    assert arabicToRoman({'o':6}) == -2
