# classes and objects: To make your code organized and tidy
# until now we learn data types : strings , numbers, boolean
# but if we need to data types for employee or cars or animales...
# we need to use classes and objects
# 1- classes to build data type
class employee:
    def __init__(self,name,age,department,is_manager,rating,salary): # attributes of data types (constructor)
        self.name=name
        self.age=age
        self.department=department
        self.is_manager=is_manager
        self.rating=rating
        self.salary=salary

    # class functions
    def is_exellent(self):
        if self.rating>=4.5:
            return "exellent"
        else:
            return "bad"
    def bonus(self):
        if self.age==20:
            print(" you have bonus in salary: 500 , so your salary now: "+str(self.salary+500))
        else:
            print(" sorry !!! you do not have bonus:your salary "+str(self.salary))      