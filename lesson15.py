# dictionaries to store data as key : value
monthnumber={
    0:"janewary",
    1:"febrawary",
    2:"march"
}
print(monthnumber[1])
#-----------------------------------#
monthnumber={
    
    0:"janewary",
    1:"febrawary",
    2:"march"
}
print(monthnumber.get(1))
#----------------------------#
monthnumber={     # if key is dublicate the python choose last key
    0:"janewary",
    0:"febrawary",
    0:"march"
}
print(monthnumber[0])
#----------------------------#
monthnumber={
    0:"janewary",
    1:True,    # boleen
    2:["march", "the end of fall"] # lists
}
print(monthnumber.get(1,"the key does not  exist")) # if key does no exist, we  can use function get to show that

belal=dict()
belal["course"]=100
belal["age"]=10
print(belal)




