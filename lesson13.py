# comparisons
def max(num1,num2,num3):
    if num1>=num2 and num1>=num3:
     return num1
    elif num2>=num1 and num2>=num3:
       return num2
    else:
       return num3
print(max(1,2,3))   
#-----------------------------------# THERE is function in python to give the max num
print(max(30,9,8)) # the function called max
#-------------------------------------------------------------------------#
# for strings
def max_string(str1,str2):
   if str1==str2:
      print(str1)
   else:
      print(str2)  
max_string("belal","amer")     