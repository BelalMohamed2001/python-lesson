# exponent function
# in python we have function to exponent function
# first function
print(2**5)
# or
print(pow(2,5))
# but now we build function pow
def power(base,power):
    result=1
    for x in range(power):
        result=result*base  # result will be changed every time in the loop  (1,2,4,8,16,32)
    return result 
print(power(2,5))
