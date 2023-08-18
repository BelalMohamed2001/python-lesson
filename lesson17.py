# guessing game project 1
secret_word="belal"
guess=""
initial_count=0
limit_count=3
out_of_guess=False

while guess!=secret_word and initial_count<limit_count:
    if initial_count<limit_count:
        guess=input("enter your guess ")
        initial_count +=1
    
if initial_count==limit_count and guess!= secret_word:
    print("you lose")
else:
    print("you win")

#-----------------------------------------------------------------------------# or
