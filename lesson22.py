# ERROR IN PYTHON
# try / except
try:
   value= int(input("enter your value "))
   print(value)
except: # default exception
   print("invalid number")   
   print("failed")
#----------------------------------#
try:
   result=10/0 # error in python can division
   value= int(input("enter your value "))
   print(value)
except ZeroDivisionError: 
   print("can not division by zero")   
   
 #--------------------------------#
try:

   value= int(input("enter your value "))
   print(value)
   result=10/0 # error in python can division
except ZeroDivisionError: 
   print("can not division by 0")   
   
except: 
   print("invalid number")   
   print("failed")
#----------------------#
try:

   value= int(input("enter your value "))
   print(value)
   result=10/0 # error in python can division
except ZeroDivisionError as err:  # to show type of error to user
   print("err")   
   
except ValueError as err1:  # to show type of error to user
   print(err1)   
   print("failed")

#--------------------------------------
#quit()in except meaning stop and exit