n = int(input("Enter the Number to Find the Factorial : "))
Fact = 1
if n < 0:
    print("For Negitive Number Factorial is Doen't Exits")
elif n == 0:
    print("For 0 Factorial Number is : 1")
else:
    for i in range(1,n+1):
        Fact = Fact * i
        print("Factorial of {0} is : {1}".format(i,Fact))
    print("The Sum of Factorial Number is :",Fact)
        
