
### finding Greatest odd Number by taking Input ###
def greatest_odd_number():
    first_input = input ( 'intergers:')
    if first_input % 2 != 0 : 
        t = 0
        
        while t < 9 :
            2nd_input = int(input ( 'intergers :'))
            if 2nd_input % 2 != 0  :
                if first_input < 2nd_input :
                    first_input = 2nd_input
                   
            t += 1
        print "Greatest Odd Number is : " first_input
    else:
        print "Please enter Odd number"
        
   
