def remdup(input_list_of_integers):
    if input_list_of_integers is None or len(input_list_of_integers)<=1:
        return None
    final_list = []
    for item in input_list_of_integers:
        if item not in final_list:
            final_list.append(item)
    print(final_list)

#test_list = [3,2,1,1]
#remdup(test_list)

def sumsquare(list_of_numbers):
    if list_of_numbers is None or len(list_of_numbers)==0:
        return 
    odd_even = []
    sum_odd_squares=0
    sum_even_squares=0
    for item in list_of_numbers:
        if item%2==0:
            sum_even_squares+=item*item
        else:
            sum_odd_squares+=item*item
    odd_even.append(sum_odd_squares)
    odd_even.append(sum_even_squares)
    print(odd_even)
    return odd_even



#print(sumsquare([1,3,5]))

# let m be a list with m lists (number of rows) of size n (number of columns)
def transpose(m):
    number_of_rows_in_m = len(m)
    # Check if there is at least one row in the list
    if number_of_rows_in_m<=0:
        return None

    # Check if each of the m rows is of the same size (n) in the input list m
    row_size_of_m=0
    for item in m:
        if(row_size_of_m!=0 and row_size_of_m!=len(item)):
            return None
        else:
            row_size_of_m=len(item)
    
    new_list_with_n_rows = []
    for i in range(row_size_of_m):
        new_row=[]
        for j in range(number_of_rows_in_m):
            new_row.append(m[j][i])
        new_list_with_n_rows.append(new_row)
    print(m)
    return new_list_with_n_rows
print(transpose([[1, 2, 3, 4], [5, 6, 7, 8]]))

