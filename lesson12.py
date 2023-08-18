#conditions  (options)
#if  a=b setting b in a
#if a==b a equal  b
is_hungry=False
if is_hungry:  #  equal to if is_hungry==True always even if is_hungry becomes false
    print("go eat")
else:
    print("do not eat")    
#-------------------------------#    
is_hungry=True
wanttoeat= True
if is_hungry or wanttoeat:  # its suffint of one of them be true to print go eat
    print("go eat")
else:
    print("do not eat")    
#--------------------------------------#
is_hungry=False
wanttoeat= True
if is_hungry and wanttoeat:  # both must be true to print go eat
    print("go eat")
else:
    print("do not eat")   

#--------------------------------# 
is_hungry=False
wanttoeat= True
if is_hungry and wanttoeat:  
    print("go eat")
elif is_hungry and not wanttoeat:  # is hungry true but want to eat is false
    print("eat for survive")    
elif not is_hungry and  wanttoeat:  
    print("do not eat now")    
else:
    print("do not eat")    