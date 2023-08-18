# tuples can not change inside tuples// can not insert or remove 
coordinates=(23,56) # because coordinates can not change after build it
print(coordinates[0])
#coordinates[0]=24 #errrrrror because not support change in tuples
#print(coordinates)

list=[(1,2),(4,3),(4,7)]
print(list)
#list[0][0]=5 # here first [0] refer to (1,2) and second [0] refer to 1 in (1,2) alsooo that's errror because tuple inside list cannot change
#print(list)
(x,y)=(4,"fred")
print(y)
#------------------------------------------------------\ itmes mesthode in dict is return tuples when using
belal=dict()
belal["ahmed"]=100
belal["youssef"]=200
tup=belal.items()
print(tup)
#-----------------------------

print((1,2,3)<(1,2,4))
#---------tuples not sorted, list of tupels sorted
belal=dict()
belal["ahmed"]=100
belal["youssef"]=200
tup=belal.items()
print(tup)
print(sorted(tup))
#--------------------------

