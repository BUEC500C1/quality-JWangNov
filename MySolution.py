# Copyright 2020 JialunWANG wjl1996@bu.edu

def arabicToRoman(inputNum):
    # Correct Evil
    try:
        if not isinstance(inputNum, int):
            raise TypeError(inputNum)
        if inputNum <= 0:
            raise BadInputValue(inputNum)

        num = int(inputNum)
        arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = ""
        for idx in range(len(arabic)):
            while num >= arabic[idx]:
                ans += roman[idx]
                num -= arabic[idx]
        return ans

    except BadInputValue as bivn:
        print("\n### The integer should be positive!! ###\n        Your input:", bivn, "\n")
        return -1

    except TypeError as e:
        print("\n### The input should be a positive integer!! ###\n        Your input:", e, "\n")
        return -2



class BadInputValue(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



if __name__ == '__main__':
    pass
