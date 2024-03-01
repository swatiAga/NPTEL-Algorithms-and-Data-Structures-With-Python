from tokenize import Exponent


def orangecap(d):
    players_total_score = {}
    for match in d.keys():
        for player in d[match].keys():
            if(player in players_total_score.keys()):
                players_total_score[player] = players_total_score[player] + d[match][player]
            else:
                players_total_score[player] = d[match][player]
    max_score = 0    
    player_with_max_score=''
    for player in players_total_score.keys():
        if(max_score< players_total_score[player]):
            max_score=players_total_score[player]
            player_with_max_score=player
    return (player_with_max_score, max_score)

#d={'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
#print(orangecap(d))

# convert a tuple list to dictionary using list comprehension - https://www.geeksforgeeks.org/python-convert-a-list-of-tuples-into-dictionary/
# customizatoin for this problem - reversed the key value from (key,value) to (value,key)
def convert_tuple_to_dictionary(tuple_list1):
    dictionary = dict((value, key ) for key, value in tuple_list1)
    return dictionary

def convert_tuple_to_dictionary2(tuple_list2):
    # Create an empty dictionary
    dictionary = {}
    # Iterate over each tuple in the list
    for tuple in tuple_list2:
        # Check if the key is already in the dictionary
        if tuple[0] in dictionary:
            # If the key is already in the dictionary, append the value to the existing list
            dictionary[tuple[0]].append(tuple[1])
        else:
            # If the key is not in the dictionary, add it and set the value as a new list
            dictionary[tuple[0]] = [tuple[1]]
     # Return the completed dictionary
    return dictionary

# This method convers a dictionary to tuple https://www.geeksforgeeks.org/python-convert-dictionary-to-list-of-tuples/
# customizatoin for this problem - reversed the key value (k,v) to (v,k)
def convert_dictionary_to_tuple(dictionary):
    # Converting into list of tuple
    list_of_tuples = [(v, k) for k, v in dictionary.items()]

    # Converting into list of tuple Using items() 
    #list = list(dict.items())
    
    # Converting into list of tuple by iterating the dictionary 
    #list = []
    # Iteration
    #for i in dict:
    #    k = (i, dict[i])
    #    list.append(k)

    return list_of_tuples
    
# Remove items from dictionary https://www.geeksforgeeks.org/python-ways-to-remove-a-key-from-dictionary/
# If the coefficient held for the exponent is zero then remove the element from the polynomial
def remove_dictionary_elements_with_zero_coefficients(dictionary):
    local_copy_of_dictionary=dictionary.copy()
    if(local_copy_of_dictionary is not dictionary):
        for key, value in dictionary.items():
            if value==0:
                local_copy_of_dictionary.pop(key)
    return local_copy_of_dictionary
#dictionary = {4: 22, 3.5:0, 3: 21, 2: 21, 1: 0, 0:0}
#print(remove_dictionary_elements_with_zero_coefficients(dictionary))

def sort_dictionary_by_keys_desc(dictionary):
    return dict(sorted(dictionary.items(), reverse=True));
#sample_dictionary = {0:3,1:2}
#print(sort_dictionary_by_keys_desc(sample_dictionary))

def addpoly(p1,p2):
    polynomial_1 = convert_tuple_to_dictionary(p1)
    polynomial_2 = convert_tuple_to_dictionary(p2)
    summation_polynomial={}
    # add the coefficients for exponents found only in polynomial1
    for exponent1 in polynomial_1.keys():
        if(exponent1 not in polynomial_2.keys()):
            summation_polynomial[exponent1] = polynomial_1[exponent1]
    # add the coefficients for exponents found only in polynomial2
    for exponent2 in polynomial_2.keys():
        if(exponent2 not in polynomial_1):
            summation_polynomial[exponent2] = polynomial_2[exponent2]
    # add the coefficients for exponents found in both polynomials
    for exponent1 in polynomial_1.keys():
        for exponent2 in polynomial_2.keys():
            if(exponent2 in polynomial_1.keys() and exponent2 not in summation_polynomial.keys()):
                summation_polynomial[exponent2] = polynomial_1[exponent1] + polynomial_2[exponent2]
        
    # remove the elements with zero coefficient
    summation_polynomial = remove_dictionary_elements_with_zero_coefficients(summation_polynomial)
    # sort the dictionary in descending value of the keys
    summation_polynomial = sort_dictionary_by_keys_desc(summation_polynomial)
    # convet the dictionary back to tuple format
    tupleslist_of_summation = convert_dictionary_to_tuple(summation_polynomial)

    return tupleslist_of_summation

#print(addpoly([(4,3),(3,0)],[(-4,3),(2,1)]) == [(2, 1),(3, 0)])

def multpoly(p1,p2):
    polynomial_1 = convert_tuple_to_dictionary(p1)
    polynomial_2 = convert_tuple_to_dictionary(p2)
    multiplication_polynomial = {}
    for key1, value1 in polynomial_1.items():
        for key2, value2 in polynomial_2.items():
            new_exponent = key1 + key2
            if(new_exponent in multiplication_polynomial.keys()):
                multiplication_polynomial[new_exponent] = multiplication_polynomial[new_exponent] + (value1 * value2)
            else:
                multiplication_polynomial[new_exponent] = value1 * value2
    
    # remove the elements with zero coefficient
    multiplication_polynomial = remove_dictionary_elements_with_zero_coefficients(multiplication_polynomial)
    # sort the dictionary in descending value of the keys
    multiplication_polynomial = sort_dictionary_by_keys_desc(multiplication_polynomial)
    # convet the dictionary back to tuple format
    tupleslist_of_multiplication = convert_dictionary_to_tuple(multiplication_polynomial)
    return tupleslist_of_multiplication

#print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])==[(1, 3),(-1, 0)])



