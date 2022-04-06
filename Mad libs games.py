from distutils.log import debug
from doctest import debug_script


color = input("enter a colour name:  ")
plural_noun = input("enter a plural noun:   ")
celebrity = input("enter celebrity  name:  ")

print("roses are" + color)
print(plural_noun + "are blue")
print("i love " + celebrity)

debug_script