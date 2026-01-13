from time import sleep

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

sum = 0
name = input("hey im gonna help you do some maths stuffbut first, whats your name? ")
num = getint(f"{name} please enter the number: ")
i = 0
while num>=i:
    print (i)
    sum+=i
    i += 1
    sleep(1)

print (f"The sum of those numbers is {sum}")
