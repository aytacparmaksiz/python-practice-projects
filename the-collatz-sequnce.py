# Collatz sequnce is a sequence that explains all natural numbers greater than 1 can be reduced to 1 shortly.
# This program lets the user type an integer and then keeps calling the function untile it returns the value 1.

def collatz(num):
    global number
    if num % 2 == 0:
        number = num // 2
        print(number)
    elif num % 2 == 1:
        number = 3 * num + 1
        print(number)

print('Enter number:')

number = int(input())

try:
    if number == 1:
        print(number)
    else:
        while number != 1:
            collatz(number)
except ValueError:
    print('Type a number')
