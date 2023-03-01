# FALTY CALCULATOR
#Qn: Design a calculator which will correctly solve all the problems expect the following ones:
# 40*7=124, 57+9=77 and 46/6=4
# Your program should take operator and the two numbers as input from the user and resturn the result.


# SOLUTION:

num1 = int(input("Enter your first number: "))
Operator = input("Which operator you want to use?\nChoose one (+, -, *, /, %, **):")
num2 = int(input("Enter your second number: "))


if num1==40 and Operator=='*' and num2==7:
    print("124")
elif num1==57 and Operator=='+' and num2==9:
    print("77")
elif num1==46 and Operator=='/' and num2==6:
    print("4")
elif Operator=='+':
    print(num1+num2)
elif Operator=='-':
    print(num1-num2)
elif Operator=='*':
    print(num1*num2)
elif Operator=='/':
    print(num1/num2)
elif Operator=='%':
    print(num1%num2)
elif Operator=='**':
    print(num1**num2)
else:
    print("Invalid Operator!")

