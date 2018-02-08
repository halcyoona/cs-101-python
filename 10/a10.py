## IMPORTS GO HERE
import os
## END OF IMPORTS



### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(directory , filename , condition = False):
    count = 0
    final_file = os.path.join(directory , filename)
    with open (final_file , 'r') as f:
        list_of_lines = f.read().split('\n')
        if condition == True:
            for line in list_of_lines:
                if line != '':
                    count = count + 1
        if condition == False:
            for line in list_of_lines:
                count = count + 1
    return count        

#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(directory , filename , y = False):
    count = 0
    final_file = os.path.join(directory , filename)
    with open (final_file , 'r') as f:
        if y == True:
            for line in f:
                for i in line:
                    if i == ' ' or i == '\n' :
                        count = count + 0
                    else:
                        count = count + 1
        if y == False:
            for line in f:
                for i in line:
                    count = count + 1
            
    return count  
#### End OF MARKER



### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
def move_lines(file1 , file2 , lines):
    with open (file1 , 'r') as f:
        list_of_lines = f.read().split('\n')
        list_of_lines 
        value = list_of_lines[:lines]
        with open (file2 , 'w') as f:
            final = '\n'.join(value)
            f.write(final)
        
            
        
        
            
        
        
        
#### End OF MARKER



if __name__ == '__main__':
    print line_count('.', 'essay.txt')
    print line_count('.', 'essay.txt', True)

    print character_count('.', 'essay.txt')
    print character_count('.', 'essay.txt', True)

    move_lines('essay.txt', 'out.txt', 3)

    pass
