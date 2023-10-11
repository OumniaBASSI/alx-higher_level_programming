#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    sum = 0
    index = 0
    if roman_string is not None:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        listrom = list(roman.keys())
        lenght = len(roman_string)
        for char in roman_string:
            # print("++ "+char)
            if char in roman:
                #print("+ "+char, roman[char])
                if char 'IXC':
                    if index < lenght-1:
                        if listrom[index+1] in 'VXLCDM':
                            sum = sum + (roman[listrom[index+1]]-roman[char])
                            sum += roman[char]
                            index += 1
                            return sum
                        """
                        check if current character index is equal to lenght
                        "I" can be ubtracted from "V" and "X",
                        "X" can be subtracted from "L" and "C",
                        "C" can be subtracted from "D" and "M".
                        However, "V", "L", and "D" cannot be used to represnet substraction;
                        """
