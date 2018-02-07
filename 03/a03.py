## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(num,guess=0.0):
    if num and guess < 0:
        return None
    elif abs(guess*guess-num)<0.00001:
        return guess
    else:
        new_guess=improve_guess(num,guess=5.00000)
        return new_guess

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(a,b):
    if a and b < 0:
        return None
    else:
        avg=(a+b)/2.000000
        return avg

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(num,guess=1.00000):
    if num and guess < 0:
        return None
    elif abs(guess*guess-num)<0.00001:
        return guess

    else:
        new_num = float(num)/float(guess)
        unique=new_num*1.00000
        new_guess=average(float(guess),unique)
        return improve_guess(num,new_guess)



#### End OF MARKER




if __name__ == '__main__':
    print sqrt(25)
