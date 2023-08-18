# looping (while/ for)
i=1
while i<=10:
   print(i)
   i+=1
print("end loop")   
#-----------------------------------#
# An infinite loop is a very dangerous thing, only use it when necessary
# i=1
#while True: # infinte loop
    #print(i)
    #i+=1
#print("end loop")    
#------------------------------------------------#
i=1
while i<=10:
   i+=1
   if i==6:
      continue # continue here means when i==6 stop and go back to while loop
   print(i)  
print("end loop")   
#----------------------------------------------#
i=1
while i<=10:
   i+=1
   if i==6:
      break # break here means when i==6 stop and exit from while loop
   print(i)  
print("end loop")  
 