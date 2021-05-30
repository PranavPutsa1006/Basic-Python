celsius = int(input("Enter an integer value temp. in celsius"))


def far(cel):
    return round(1.8*cel+32,1)


print("The Fahrenheit equivalent of",celsius,"degrees Celsius is",far(celsius))