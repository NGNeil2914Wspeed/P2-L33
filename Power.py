from time import sleep

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

name = input("Hey, I'm gonna help you find out how many digits are in a number but first, what's your name? ")
num = getint(f"Hey {name}, could you tell me the number? ")
num2 = str(num)
length = len(num2)
print (f"The length of your number ({num}) is {length}")