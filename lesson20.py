# 2d lists and nested loop
# 1- 2d lists use for maps ,some games ,coordinates of snake game for example
twoD_list= [
         #0 1 2 colums
         [1,2,3], # 0 rows
         [4,5,6], # 1
         [7,8,9], 
         [0]
]
print(twoD_list[2][1]) # 2 for row and 1 for colum
#-----------------------------------------#
# 2- nested loop
for row in twoD_list:
    print(row)

for row in twoD_list:
    for colum in row: # after print row , in every row [1,2,3] print colum 1,2,3..
        print(colum)  
 #______________#
 # for you you can write comment like that
''''''''''
belal mahmoud amer 
computer engineering and software system
'''''''''''

       