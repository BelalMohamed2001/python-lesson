# writing
'''                 r  r+  w  w+  a  a+
--------------    |---------------------
read              | +  +      +       +
write             |    +   +  +   +   +
create            |        +  +   +   +    // even if file not found
truncate(delete)  |        +  +
position to start | +  +   +  +
position to end   |               +   +
                  |
'''
workers_file=open("test.txt","a")
workers_file.write("\nsara - waiter")  # \n to start new line 
#file=open("worker.html","a")  # a , a+ ,w ,w+ (create file even if it is not found)
#file.write("<p> html is web development</P>")
#workers_file=open("test.txt",'w') if you use w or w+ ,python will delete information and start beginning
# workers_file.write(" sara - waiter")
#list=["\nfirst line","\nsecond line","\nthird line"]
#workers_file.writelines(list) # return lines not only one
workers_file.close()
