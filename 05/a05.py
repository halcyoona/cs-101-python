## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(p):
    if prime(p):
        x=11
        while p>=x*x:
            x=x+2
            if p==x*x:
                return False
        else:
            return True
    else:
        return False
#### Problem is that square of prime number is not a prime number####
def prime(new):
    if new<=1:
        return False
    else:
        p=int(new)
        if new==p:
            if p==2 or p==3 or p==5 or p==7 or p==11:
                return True
            if p%2==0 :
                return False
            if p%3==0 :
                return False
            if p%5==0:
                return False
            if p%7==0 :
                return False
            if p%11==0 :
                return False
            else:
                return True
        else:
            return False
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(num):
    if num>=1:
        n=int(num)
        if n==num:
            new_num=int((num+4)/2)
            for start in range (1,new_num):
                if num%start==0:
                    print (start)
            print (n)
        else:
            print (None)
    else:
        print (None)
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def improvement(number):
    if number%2==0:
        new_number=number-1
        return new_number
    else:
        new_number=number-2
        return new_number
def get_largest_prime(p):
    if p>=2:
        p=int(p)
        if is_prime(p):
            return p
        else:
            new_p = improvement(p)
            return get_largest_prime(new_p)
    else:
        return None
#### End OF MARKER



if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
