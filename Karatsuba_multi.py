import time


def product(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    num1a = num1_str[:len(num1_str)//2]
    num1b = num1_str[len(num1_str)//2:]
    num2a = num2_str[:len(num2_str)//2]
    num2b = num2_str[len(num2_str)//2:]

    if len(num1a) != 1 and len(num2a) != 1:
        num1a__num2a = product(int(num1a),int(num2a))
    else:
        num1a__num2a = int(num1a)*int(num2a)

    if len(num1a) != 1 and len(num2b) != 1:
        num1a__num2b = product(int(num1a),int(num2b))
    else:
        num1a__num2b = int(num1a)*int(num2b)

    if len(num1b) != 1 and len(num2a) != 1:
        num1b__num2a = product(int(num1b),int(num2a))
    else:
        num1b__num2a = int(num1b)*int(num2a)

    if len(num1b) != 1 and len(num2b) != 1:
        num1b__num2b = product(int(num1b),int(num2b))
    else:
        num1b__num2b = int(num1b)*int(num2b)

    return (10**len(num1_str))*num1a__num2a + (10**(len(num1_str)//2))*(num1a__num2b+num1b__num2a) + num1b__num2b


if __name__ == '__main__':
    number1 = 31415926535897932384626433832795028841971
    number2 = 27182818284590452353602874713526624977572
    print(type(number1), type(number2))
    time1 = time.time()
    prod = product(int(number1),int(number2))
    print("product of {} and {} is given by {}".format(number1,number2,prod))
    time2 = time.time()
    print("Time taken by recursive is {}".format(time2-time1))
    time3 = time.time()
    product2 = number1*number2
    time4 = time.time()
    print("time by normal {}".format(time4-time3))
    print(product(number1,number2)==(number1*number2))