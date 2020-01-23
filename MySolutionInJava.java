// Copyright 2019 JialunWANG wjl1996@bu.edu

class MySolutionInJava {

    public static String intToRoman(int num) {
        int nCopy = num;
        int[] arabic = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = new String[]{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder ans = new StringBuilder();
        for (int idx = 0; idx < arabic.length; idx++) {
            while (nCopy >= arabic[idx]) {
                ans.append(roman[idx]);
                nCopy -= arabic[idx];
            }
        }
        return ans.toString();
    }


    public static void main(String[] args) {
        System.out.println("These are tests from LeetCode.com");
        System.out.println(intToRoman(3).equals("III") ? "Correct." : "ERROR!!");
        System.out.println(intToRoman(4).equals("IV") ? "Correct." : "ERROR!!");
        System.out.println(intToRoman(9).equals("IX") ? "Correct." : "ERROR!!");
        System.out.println(intToRoman(58).equals("LVIII") ? "Correct." : "ERROR!!");
        System.out.println(intToRoman(1994).equals("MCMXCIV") ? "Correct." : "ERROR!!");
    }
}
