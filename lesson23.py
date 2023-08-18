# here there are some problem in this lesson to run code , try to run code in another compiler
# read file : to show file of type txt,html,.....
# getting information from this files:
# reading file : get info can not change in file /command of read is r ,write w,append a insert in last file, r+ read and write

workers_file= open("test.txt","r")
#print(workers_file.readable()) # To check if the file is ready to be read
print(workers_file.read())
#print(workers_file.readline()) # print first line
#print(workers_file.readline()) # print second line and so on..
#print(workers_file.readlines()) # return list 
#print(workers_file.readlines()[0]) # return first value in list
for worker in workers_file.readlines(): # Return the value one by one and you can add a statement
    print(worker+"the first worker in the egypt")

workers_file.close()