def function(temp):
    temp = temp * 9 / 5 + 32
    print(temp)


if __name__ == "__main__":
    result = float(input('Please input you want to convert the degrees Celsius :'))
    print(function(result))
