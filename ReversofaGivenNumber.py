#Number = int(input("Eneter the Number to Reverse : "))
Number = 123
Reverse = 0
while(Number > 0):
    Remainder = Number % 10
    Reverse = (Reverse * 10) + Remainder
    Number = Number // 10
print("The Reverse of the Given Nimber is : ",Reverse)
