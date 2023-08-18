# return to looping
# now for loop
for x in "belal":
    print(x)
#---------------#
list=["be","la","l"]    
for x in list:
    print(x)
#----------------#    
for x in range(10):  # from 0 to 9
    print(x) 
for x in range (1,10): # If you need to start from a specific point (1 include but 10 not include)
    print(x)
print(len(list)) 
print(len("belal")) 
for x in range (len(list)) : # loop of size of list (0,1,2) // len(list)=3
    print(x)
for x in range(len(list)):
    print(list[x])   # === list[0] ,list[1],list[2]
for x in range (10):
    if x % 2==0: # to check even / odd number
        print(x," is even number")
    else:
        print(x," is odd muber")  
for x in range(len(list)):
     if list[x]=="l": # list[x] = l  == "l"
         print(x," is win")
     else:
         print(x," is lose")
for x in list:
    if x=="be":
        print(x,"found")
        break
else: # else here for forlooping
    print(x,"not found")        
