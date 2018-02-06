## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x,guess=0.0):
    if x and guess<0:
        print None
    if good_enough(guess,x):
        return guess
    else:
        new_guess=improve_guess(guess,x)
        return sqrt(x,new_guess)
def good_enough(guess,x):
    if abs(guess*guess-x)<0.00001:
        return True
    else:
         return False
#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(x,y):
    avg=(x+y)/2.0
    return avg

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess,x):
	x=x*1.0
    if guess < 1.:
        return guess+5.00000
    else:
        new_guess=average(guess,x/guess)
        return new_guess




#### End OF MARKER




if __name__ == '__main__':
    print sqrt(36)
