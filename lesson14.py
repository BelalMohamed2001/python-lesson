# calculator 2
print("hello sir")
print("can i help you select yes or no")
response =input()
if response=="yes":
    print("go to main calculator ")
    print("press number 1 to start calculator ")
    print("press number 2 to exit calculator ")
    number=input()
    if number=="1":
        operator= input("choose operator + - * / ")
        num1=float(input("enter your first number: "))
        num2=float(input("enter your second number: "))
        if operator=="+":
            print(num1+num2)
        elif operator=="-":
            print(num1-num2)   
        elif operator=="/":
            print(num1/num2)    
        elif operator=="*":
            print(num1*num2)
        else:
            print("please enter operator again") 
    elif number=="2":
        print("the calculator will be closed")       
elif response=="no":
     print("thanks to use app ")
