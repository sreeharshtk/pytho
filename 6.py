Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Remainder = Number %10
    Reverse = (Reverse *10) + Remainder
    Number = Number //10

print(f" Reverse of entered number is = {Reverse}")
