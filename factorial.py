number= int(input("Enter a number to cal factorial"))

if number < 0:
    print("Factorial is not defined for negative numbers")

elif number == 0 or number == 1:
    print("The factorial " , number , "is " ," 1")
else:
    factorial = 1
    for i in range(2, number+1):
        factorial *=i

    print("The factorial of " , number , "is " , factorial)