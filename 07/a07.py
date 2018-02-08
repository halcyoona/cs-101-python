## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def score(n):

    if n == "A+" : return 4.0
    elif n == "A" : return 4.0
    elif n == "A-" : return 3.67    
    elif n == "B+" : return 3.33 
    elif n == "B" : return 3.0  
    elif n == "B-" : return 2.67
    elif n == "C+" : return 2.33
    elif n == "C" : return 2.0
    elif n == "C-" : return 1.67
    elif n == "D+" : return 1.33    
    elif n == "D" : return 1.0
    elif n == "F" : return 0.0
    elif n == None : return None 
    else :
        return None
       
def calculate_sgpa(lst):
    if lst == None : return None
    if lst == [] :return 0 
    if type(lst) == list :
        counter =len(lst)
        b = []                # List of score 
        for i in lst :
            a = score (i)
            if a == None:
                return None
            b.append (a)     
        sum_of_score = sum(b)  # Adding the Element of list 
        sgpa = sum_of_score / counter
        return sgpa
    else:
        new = [lst]
        return calculate_sgpa(new)


	
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(lst1 , lst2):
    if lst1 == [] or lst2 == [] : return 0 
    if type(lst1) != list:
        result= score(lst1)
        return result
    l1 = len (lst1)
    l2 = len (lst2)
    weighted = sum(lst2)
    points = []                #lsit of point scored
    if l1 == l2 :
        for i in lst1 :
            c = score(i)
            if c == None : return None
            points.append(c)
        multiplied_value = []                 #list of ponits scored multipy with weighted
        for i in points :
            for j in lst2 :
                t = i * j
                multiplied_value.append(t)
                lst2.pop(0)
                break
        total_points = sum(multiplied_value)
        final_value = total_points / weighted
        return final_value 
    else:
        return None
    
    
        
        
    
    
    
    
        
        
    
    

#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(['A+'])
    print calculate_sgpa_weighted(['A+'], [4])
