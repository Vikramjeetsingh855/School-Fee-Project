def arithmetic(n1,n2,by=None):
    if by=="+":
        return n1+n2
    if by=="*":
        return n1*n2
    else:
        print("invalid")
print(arithmetic(eval(input("enter num1:")),eval(input("enter num2:")),by=input("select operation:")))

eval(input("enter num1:"))
eval(input("enter num2:"))