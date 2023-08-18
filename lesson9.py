# lists
# sum of more than one varible and many diffrent varible[int,string,...]
# my_name="islam" varible
#my_name=[1,"ss",true.false,another list [1,"ssss"]] list
frinds=[1,"3333",True,False,[1,"SSSS"]]
print(frinds)
print(frinds[-1])
print(frinds[0])
print(frinds[1:4]) # means i talled python include from index 1 to index 4 but index 4 not include
print(frinds[0:5]) #or print(frinds[0:])
print(frinds[0:])
frinds[0]=3 # change in index 0 in list frinds 
print(frinds)
youth=[2,3,"ss",True,[1,"ddddd"]]
frinds.extend(youth) # to conatination two lists or frinds += youth or frinds= frinds + youth
frinds.append([1]) # to insert value in the end of list
frinds.append([1,"sss"])
print(frinds)
frinds.pop() # remove last value in list
print(frinds)
frinds.insert(0,"df") # choose index to insert value
print(frinds)
frinds.remove("df") # choose index to remove
print(frinds)
x=frinds.pop()
print(x)
frinds.count("ss") # count the repeated words
print(frinds.count("ss"))
y=["c","d","a","b","g"]
y.sort()
print(y)
frinds.clear() # clear all list
print(frinds)
#---------------------------------------------------------------------#
belal=[1,2,3,4,5,6]
amer=belal # any change in belal will be affected in amer
belal.append(1)
print(belal)
print(amer)
#---------------#
belal=[1,2,3,4,5,6]
amer=belal.copy() # any change in belal will NOT be affected in amer (shallow copy)
belal.append(1)
print(belal)
print(amer)
#-----------------------------------------string are immutable and lists are mutable مينفعش اغير في سترينج
for i in ["aa",1,5.5]:
    print(i)
#----------------------------------------------
print(range(4))
frinds=["ahmed","shahd","youssef"]
print(range(len(frinds)))
for i in range(len(frinds)):
    print("happy new year "+frinds[i])
for i in frinds:
    print("happy new year "+i)
#----------------------------------------conjection
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print(1 in a) # logic exprission
print(sum(a))
#---------------------------------------------------------- split to covert to list spaces convert to lists
a="mony bank china"
b=a.split()
print(b)
d="mony;bank;china"
c=d.split(";")# search for ; and split about according to that
print(c)

 