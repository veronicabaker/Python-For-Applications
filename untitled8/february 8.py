#import spytools
#gen consecutive chars
#alpha = spytoools.genconsecutivechars
#translated = alpha[1:] + alpha[0]
#i = alpha.index(s)
#translated[i]
#remove_duplicates
#remove_letters
#construct a new string with ook
#consecutive calls to replace


def remove_letters(letters, s):
    for letter in letters:
        s = s.replace(letter, '')
    return s

if __name__ == '__main__':
    print(remove_letters('ab', 'banana'))


def remove_duplicates(s):
    #accumulation

s = "cat"

#s[3] = error
#want s[3] to wrap around using modulo

"""
lists are mutable
when we use a method on a list the list changes most of the time and return a value some of the time and change and give
back a value once?
"""

"""
[1, 2, 3, 4]
[n * 2 for n in numbers]
numbers = [1 , 2, 3 , 4, 5]
[n for n in numbers if n % 2 = 0]
list(range(10))
"""

