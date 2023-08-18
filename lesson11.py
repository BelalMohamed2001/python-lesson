# functions  to implement one task /calculater has many function add/sub/multi 
def say_hi():  # def is definition of function 
    print("hello")
print( "thanks") # out of function
say_hi() # call function to print
#-------------------------------------#
def sayhi(name):
    print("hello bro "+name)     # one paramter
sayhi("belal")
#--------------------------------------#
def sayhi(name,age): # can take paramter true /false/ [1,"ss"] / (1,2)
    print("hello bro "+name+"your age "+age)    # two paramter or str(age)
sayhi("belal","20")
#---------------------------------------#
def cube(num):  
   return num*num*num # return use for return value but you can use varible to store result
 #result=cube(3)
print(cube(3)) # we can replace cube 3 to result in line 17
#-----------------------------------------#
def sum(num1,num2):
    return (num1+num2) # return is last line in function so when it seens the return it going out of function
print(sum(1,2))
