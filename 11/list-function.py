### Program making a list by taking input from user and then  conversion of user input list into a new list ### 
 
user = [] 
new = [] 

for x in range (1,21): 
    value = input ('value :') 
    user.append(value) 
    if x == 20 : 
        for i in user: 
            if  i in new: 
                continue
            else:
                new.append(i)

print new
