# Copyright 2020 JialunWANG wjl1996@bu.edu

def arabicToRoman(num):
    nCopy = num
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    ans = ""
    for idx in range(0, len(arabic)):
        while nCopy >= arabic[idx]:
            ans += roman[idx]
            nCopy -= arabic[idx]
    return ans


# Some simple tests
if __name__ == '__main__':

    serial = 0
    serialStep = 1

    inAra = 1
    serial += serialStep
    outRom = arabicToRoman(inAra)
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    print("    The output roman number is:", outRom)

    inAra = 3
    serial += serialStep
    outRom = arabicToRoman(inAra)
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    print("    The output roman number is:", outRom)

    inAra = 4
    serial += serialStep
    outRom = arabicToRoman(inAra)
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    print("    The output roman number is:", outRom)

    inAra = 44
    serial += serialStep
    outRom = arabicToRoman(inAra)
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    print("    The output roman number is:", outRom)

    inAra = 49859
    serial += serialStep
    outRom = arabicToRoman(inAra)
    print("\n[ Test case", serial, "]")
    print("    The input arabic number is:", inAra)
    print("    The output roman number is:", outRom)

