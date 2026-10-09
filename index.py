number = int(input("Enter a number: "))
total = 0

for digit in str(number):
    total = total + int(digit) ** len(str(number))

if total == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

