# 2- objects to call datatype and use it
from lesson27 import employee
employee1=employee("belal",20,"cyber_security",True,5,5000)  # object to call class data type and use it
print(employee1.name)
print(employee1.name,employee1.age,employee1.department,employee1.is_manager,employee1.rating,employee1.salary)
print(employee1.is_exellent())
employee1.bonus()