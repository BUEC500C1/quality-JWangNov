# Copyright 2020 JialunWANG wjl1996@bu.edu

from MySolution import arabicToRoman

def _simpleTests():
    print("These are some simple tests.")
    serial = 0
    serialStep = 1

    inAra = 3
    serial += serialStep
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    outRom = arabicToRoman(inAra)
    print("    The output roman number is:", outRom)

    inAra = 4
    serial += serialStep
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    outRom = arabicToRoman(inAra)
    print("    The output roman number is:", outRom)

    inAra = 44
    serial += serialStep
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    outRom = arabicToRoman(inAra)
    print("    The output roman number is:", outRom)

    inAra = 49859
    serial += serialStep
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    outRom = arabicToRoman(inAra)
    print("    The output roman number is:", outRom)

    inAra = 0.2
    serial += serialStep
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    outRom = arabicToRoman(inAra)
    print("    The output roman number is:", outRom)

    inAra = "Hello"
    serial += serialStep
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    outRom = arabicToRoman(inAra)
    print("    The output roman number is:", outRom)

    inAra = -10
    serial += serialStep
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    outRom = arabicToRoman(inAra)
    print("    The output roman number is:", outRom)



if __name__ == '__main__':
    _simpleTests()
