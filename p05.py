str1 = 'this is a string'
str2 = "this is also a string"
print(str1)
print(str2)
print(str1[5])
print(str2[9])
print("marvel"[3])
# String slicing
str3 = "Apricots"
str4 = str3[:3]     # Slice with first 3 characters
str5 = str3[2:5]    # Slice from index=2 to index=4
str6 = str3[4:]     # Slice with characters from index 4
print(str3)
print(str4)
print(str5)
print(str6)
print(str3[:3])
print(str3[2:5])
print(str3[4:])
a = "Marvel"
b = " "
c = "Studios"
d = a+b+c
print(d)
print(d[7])
print(d[:6])
print(d[3:10])     # Slicing a string does not affect the original string.
print(d[7:])
# e = a-"vel"
# print(e)          "-" operator can not be used in strings to delete a part of a string.

