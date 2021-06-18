
def add(x,y):
     return x+y

def substract(x,y):
     return x-y

def multiply(x,y):
     return x*y

def divide(x,y):
     return x/y

print("select operation")
print("1.Add")
print("2.substract")
print("3.Multiply")
print("4.Divide")

while True:
    choise = input("Enter operation(1,2,3,4)")

    if choise in ("1","2","3","4"):
        num1 = float(input("Enter First Number:"))
        num2 = float(input("Enter Second Number:"))

        if choise == "1" :
            print(num1, "+", num2, "=",  add(num1, num2) )

        elif choise == "2" :
            print(num1, "-", num2, "=",  substract(num1, num2) )

        elif choise == "3" :
            print(num1, "*", num2, "=",  multiply(num1, num2) )

        elif choise == "4" :
            print(num1, "/", num2, "=",  divide(num1, num2) )

        break

    else:
        print("invalid input")




        

