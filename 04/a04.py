## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(marks):
    marks=round(marks)
    if marks<=100:
        if marks >= 90 and marks<=100:
            return "A+"
        elif marks>=86 and marks<90:
            return "A"
        elif marks>=82 and marks<86:
            return "A-"
        elif marks>=78 and marks<82:
            return "B+"
        elif marks>=74 and marks<78:
            return "B"
        elif marks>=70 and marks<74:
            return "B-"
        elif marks>=66 and marks<70:
            return "C+"
        elif marks>=62 and marks<66:
            return "C"
        elif marks>=58 and marks<62:
            return "C-"
        elif marks>=54 and marks<58:
            return "D+"
        elif marks>=50 and marks<54:
            return "D"
        else:
            return "F"

    else:
        print None
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####


def score(n):

    if n=="A+":
        return 4.0
    elif n=="A":
        return 4.0
    elif n=="A-":
        return 3.67
    elif n=="B+":
        return 3.33
    elif n=="B":
        return 3.0
    elif n=="B-":
        return 2.67
    elif n=="C+":
        return 2.33
    elif n=="C":
        return 2.0
    elif n=="C-":
        return 1.67
    elif n=="D+":
        return 1.33
    elif n=="D":
        return 1.0
    
    elif n=="F":
        return 0.0
def calculate_sgpa(g1,g2,g3):
    subjects=0.0
    points=0.0
    if not g1 == "nothing":
        gpa1=score(g1)
        subjects=subjects+1
        points=points+gpa1

    if not g2 == "nothing":
        gpa2=score(g2)
        subjects=subjects+1
        points=points+gpa2

    if not g3== "nothing":
        gpa3=score(g3)
        subjects=subjects+1
        points=points+gpa3
    if subjects==0:
        return 0
    else:
        final_sgpa=(points/subjects)
        return final_sgpa
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
