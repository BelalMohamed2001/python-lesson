# project 2 translator
# convert any vowel letter (a,o,u,e,i) to letter z
statement=input("enter your statement: ")
translator=""
for letter in statement:
    if letter.lower() in "aouei": # rather than "AEOIUAOUEI" for example her if E will be e then go to isupper as E not e
        if letter.isupper(): # to return capital letter 
           translator=translator+"Z"
        else:
            translator=translator+"z"   
    else:
        translator=translator+letter
print(translator)