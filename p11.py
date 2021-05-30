print("Hello")
name = input("What is your name?\n")
print("Hello",name)
print("Your name is "+name+".")      # You can use this only for inserting strings,not numbers.
print("Your name is "+name)
print(type(name))
num = input("What is your favourite number?")
print("Your favourite number is "+num+".")
print(type(num))
# So, whatever you input, it is stored as a string,until you convert it using type-casting.
d = int(num)
print("The integer you entered is ", d)
# print("The integer you entered is "+d+".") does not work bcz python can't concatenate numbers with strings.
print(type(d))
print(num*5)
