## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(lst):
    if lst == None : return  None 
    if lst == [] : return []
    if type(lst) == list :
        final_list = []
        for i in lst :
            student_list = list (i) 
            sum_of_score = 0 
            lst1 = []
            for j in student_list : 
                if j == None : sum_of_score = sum_of_score + 0
                if type(j) == str : lst1.append(j) 
                if type(j) == int or type(j) == float  : sum_of_score = sum_of_score + j
            lst1.append(sum_of_score)
            final_tuple = tuple(lst1)
            final_list.append(final_tuple)
        return final_list
                
                
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(lst):
    lst1 = find_cumulative_marks(lst)
    list_of_score = []
    for i in lst1:
        lst2 = list(i)
        for j in lst2 :
            if type(j) == int or type(j) == float:
                list_of_score.append(j)
    top_student = max(list_of_score)
    counter = 0
    final_list = []
    for i in list_of_score :
        if i == top_student :
            list_of_top_student = list(lst1[counter])
            for i in list_of_top_student :
                if type(i) == int or type(i) == float:
                    list_of_top_student.remove(i)
                    tuple_of_top_student = tuple(list_of_top_student)
                    final_list.append(tuple_of_top_student)
        counter = counter + 1
    if len(final_list) == 1 : return tuple_of_top_student
    else:
        return final_list
            
        
#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
