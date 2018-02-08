## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def output_prime_factors(num):
    num = round (num)
    start=0
    while start<num:
        start=start+1
        if num%start==0:
            if is_prime (start) :
                print  start

def is_prime(p):
    if prime(p):
        x = 11
        while p >= x * x:
            x = x + 2
            if p == x * x:
                return False
        else:
            return True
    else:
        return False


def prime(new):
    if new <= 1:
        return False
    else:
        p=int(new)
        if new==p:
            if p == 2 or p == 3 or p == 5 or p == 7 or p == 11:
                return True
            if p % 2 == 0 :
                return False
            if p % 3 == 0 :
                return False
            if p % 5 == 0:
                return False
            if p % 7 == 0 :
                return False
            if p % 11 == 0 :
                return False
            else:
                return True
        else:
            return False
#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(n):
    if n==1:
        return 2
    else:
        b = 1
        while n > 1:
            b = b + 2
            if is_prime(b):
                n = n - 1
                if n == 1:
                    return b
#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
