from methods import *
from Part4 import *
from Part5 import *

print(scramble2Encrypt("Clarkson"))
print(scramble2Decrypt("lrsnCako"))

key = keyGen()
print(key)
mes = (substitutionEncrypt("I love Clarkson", key))
print(mes)
print(substitutionDecrypt(mes, key))

print(" ")


newKey = genKeyFromPass("hello")
print(newKey)
encMes = substitutionEncrypt("I love Clarkson", newKey)
print(encMes)
decMes = substitutionDecrypt(encMes, newKey)
print(decMes)


print(rescramble2Encrypt("hello everyone"))
print(rescramble2Decrypt("hloeeynel vroe"))

print(palindrome("yes"))
print(palindrome("nursesrun"))