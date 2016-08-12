"""
chr(65)
A

chr(90)
Z

chr(97)
a

len("hello")
5

chr- character of a unicode code point
ord- unicode code point of a character
len- # chars in a string

#operators that work on strings
-concatenation +
-index []
-repetition *
-slicing [:]
-in/not in
-string formatting %
"""

"""
plain text - some original message
cyphertext - scrambled version of plain text
encryption - process of transforming cyphertext back to plain text
decryption - process of transforming cypertext back to plain text

#transposition cypher
"hello"
 01234

 evens - hlo
 odds -  el

 elhlo

"""
"""
s = "hello"
for letter in s:
    print(letter)

for i in range(len(s)):
    print(s[i])

"""

def encrypt(s):
    evens = ""
    odds = ""
    for i in range(len(s)):
        if i % 2 == 0:
            evens += s[i]
        else:
            odds += s[i]
    new_word = odds + evens

def decrypt(s):
    if len(s) % 2 == 0:
        half = len(s)/2
        final = ""

        for i in range(int((half))):
            final += s[(int(i + half))]
            final += s[i]

    else:
        half = int((len(s)-1)/2)
        final = ""
        for i in range(half + 1):
            final +=s[i + half]
            if i < half:
                final += s[i]

    return final

print(decrypt("tp/icntre.o/5ah/ATO/ieIae/4/tlmnrb118x04jght:/.d.unrcmvcceCRONst/mgsi8a_eoga__2012.p"))
