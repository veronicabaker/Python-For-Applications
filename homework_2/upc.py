"""
upc.py
=====
Implement the following two functions as specified in the docstrings:

1. generate_bar_widths(s)
2. valid_barcode(s)

Some resources that may help with your implementation:

* https://en.wikipedia.org/wiki/Universal_Product_Code#Encoding
* http://electronics.howstuffworks.com/gadgets/high-tech-gadgets/upc3.htm
* http://www.adams1.com/upccode.html

"""
def generate_bar_widths(s):
    """Takes a barcode number as a string and translates it to a series
    of bar widths (a string that consists of 1's, 2's, 3's and 4's with
    each number corresponding to a width of a bar). For example, a
    series of bar widths starting with '1113 ... ' would consists of
    a black single width bar, a white single width bar, a black single
    width bar... and then a white triple width bar'.

    generate_bar_widths('043000181706')
    # --> '11132111132141132113211321111111222112132221131232111114111'

    :param s: the number to be translated to a series of bar widths
    :type s: str
    :return: a string representing the width of each bar, including the
    start, middle and end patterns (111, 11111, and 111)
    :rtype: str
    """
    # implement this function!
    bar_widths = "111"
    for i in range(int(len(s) / 2)):
        if s[i] == "0":
            bar_widths += "3211"
        elif s[i] == "1":
            bar_widths += "2221"
        elif s[i] == "2":
            bar_widths += "2122"
        elif s[i] == "3":
            bar_widths += "1411"
        elif s[i] == "4":
            bar_widths += "11411"
        elif s[i] == "5":
            bar_widths += "1231"
        elif s[i] == "6":
            bar_widths += "1114"
        elif s[i] == "7":
            bar_widths += "1312"
        elif s[i] == "8":
            bar_widths += "1213"
        elif s[i] == "9":
            bar_widths += "3112"
    bar_widths += "11111"
    for i in range(int(len(s)/2) + 1, len(s)):
        if s[i] == "0":
            bar_widths += "3211"
        elif s[i] == "1":
            bar_widths += "2221"
        elif s[i] == "2":
            bar_widths += "2122"
        elif s[i] == "3":
            bar_widths += "1411"
        elif s[i] == "4":
            bar_widths += "11411"
        elif s[i] == "5":
            bar_widths += "1231"
        elif s[i] == "6":
            bar_widths += "1114"
        elif s[i] == "7":
            bar_widths += "1312"
        elif s[i] == "8":
            bar_widths += "1213"
        elif s[i] == "9":
            bar_widths += "3112"
    bar_widths += "111"
    return bar_widths

def valid_barcode(s):
    """Determines whether a barcode is valid or not based on length and
    the check digit. A "UPC-A" barcode consists of 12 digits, with the
    last digit being the check digit. Some examples:

    valid_barcode('036000291452') # --> True
    valid_barcode('036000291450') # --> False
    valid_barcode('075678164125') # --> True
    valid_barcode('')            # --> False

    :param s: barcode number
    :type s: str
    :return: true if the barcode is valid, false otherwise
    :rtype: bool
    """
    # implement this function!
    odd_digits = 0
    even_digits = 0
    result = 0
    for i in range(len(s) - 1):
        if i % 2 == 0:
            odd_digits += int(s[i])
        else:
            even_digits += int(s[i])
    result = (3 * odd_digits + even_digits) % 10
    if result != 0:
        result = 10 - result

    try:
        if int(s[-1]) == result and len(s) == 12:
            return True
        else:
            return False
    except IndexError:
        return False

if __name__ == '__main__':
    print(generate_bar_widths("043000181706"))
    assert valid_barcode('036000291452') == True
    assert valid_barcode('036000291450') == False
    assert valid_barcode('075678164125') == True
    assert valid_barcode("") == False
    print('try your functions here!')
