import math
class AssignmentWeek3:
    def remdup(input_list_of_integers):
        if input_list_of_integers is None or len(input_list_of_integers)<=1:
            return input_list_of_integers
        final_list = []
        for item in input_list_of_integers:
            if item not in final_list:
                final_list.append(item)
        return final_list

    def sumsquare(list_of_numbers):
        if list_of_numbers is None or len(list_of_numbers)==0:
            return list_of_numbers
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
        return odd_even

    # let m be a list with m lists (number of rows) of size n (number of columns)
    def transpose(m):
        number_of_rows_in_m = len(m)
        # Check if there is at least one row in the list
        if number_of_rows_in_m<=0:
            return m

        # Check if each of the m rows is of the same size (n) in the input list m
        row_size_of_m=0
        for item in m:
            if(row_size_of_m!=0 and row_size_of_m!=len(item)):
                return m
            else:
                row_size_of_m=len(item)

        new_list_with_n_rows = []
        for i in range(row_size_of_m):
            new_row=[]
            for j in range(number_of_rows_in_m):
                new_row.append(m[j][i])
            new_list_with_n_rows.append(new_row)
        return new_list_with_n_rows



class AssignmentWeek2:
    def threesquares(m):
        if m<=0 or math.modf(m)[0]>0 or math.modf(m)[1]<=0:
            return False
        # Legendre's theorem - If m can be written in the form 4^a(8b+7) then it can not be expressed as a sum of three squares
        while m%4==0:
            m=m/4
        if m%8==7:
            return False
        return True

    def repfree(s):
        if s is not None and len(s)>0:
            print(set(s))
            print(len(set(s)))
            if(len(s)>len(set(s))):
                return False
        else:
            return False
        return True
    
    def hillvalley (l):
        trend= []
        if len(l) in {0,1,2}:
            return False
        for a in range(1, len(l)):
            if l[a] >= l[a-1] and (len(trend)==0 or trend[-1]!='up'):
                trend.append('up')
            if l[a] <= l[a-1] and (len(trend)==0 or trend[-1]!='down'):
                trend.append('down')
        if len(trend) >2 or len(trend) ==1:
            return False
        if len(trend) ==2 and (trend[-1]=='up' or trend[-1]=='down'):
            return True
        return False 

class AssignmentWeek4:
    # If the coefficient held for the exponent is zero then remove the element from the polynomial
    def remove_dictionary_elements_with_zero_coefficients(self, dictionary):
        local_copy_of_dictionary=dictionary.copy()
        if(local_copy_of_dictionary is not dictionary):
            for key, value in dictionary.items():
                if value==0:
                    local_copy_of_dictionary.pop(key)
        return local_copy_of_dictionary

    # customizatoin for this problem - reversed the key value from (key,value) to (value,key)
    def convert_tuple_to_dictionary(self, tuple_list1):
        dictionary = dict((value, key ) for key, value in tuple_list1)
        return dictionary

    def sort_dictionary_by_keys_desc(self, dictionary):
        return dict(sorted(dictionary.items(), reverse=True));

    # customizatoin for this problem - reversed the key value (k,v) to (v,k)
    def convert_dictionary_to_tuple(self, dictionary):
        # Converting into list of tuple
        list_of_tuples = [(v, k) for k, v in dictionary.items()]
        return list_of_tuples

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

    def addpoly(self,p1,p2):
        polynomial_1 = self.convert_tuple_to_dictionary(p1)
        polynomial_2 = self.convert_tuple_to_dictionary(p2)
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
                    summation_polynomial[exponent2] = polynomial_1[exponent2] + polynomial_2[exponent2]
        
        # remove the elements with zero coefficient
        summation_polynomial = self.remove_dictionary_elements_with_zero_coefficients(summation_polynomial)
        # sort the dictionary in descending value of the keys
        summation_polynomial = self.sort_dictionary_by_keys_desc(summation_polynomial)
        # convet the dictionary back to tuple format
        tupleslist_of_summation = self.convert_dictionary_to_tuple(summation_polynomial)
        return tupleslist_of_summation

    def multpoly(self,p1,p2):
        polynomial_1 = self.convert_tuple_to_dictionary(p1)
        polynomial_2 = self.convert_tuple_to_dictionary(p2)
        multiplication_polynomial = {}
        for key1, value1 in polynomial_1.items():
            for key2, value2 in polynomial_2.items():
                new_exponent = key1 + key2
                if(new_exponent in multiplication_polynomial.keys()):
                    multiplication_polynomial[new_exponent] = multiplication_polynomial[new_exponent] + (value1 * value2)
                else:
                    multiplication_polynomial[new_exponent] = value1 * value2
    
        # remove the elements with zero coefficient
        multiplication_polynomial = self.remove_dictionary_elements_with_zero_coefficients(multiplication_polynomial)
        # sort the dictionary in descending value of the keys
        multiplication_polynomial = self.sort_dictionary_by_keys_desc(multiplication_polynomial)
        # convet the dictionary back to tuple format
        tupleslist_of_multiplication = self.convert_dictionary_to_tuple(multiplication_polynomial)
        return tupleslist_of_multiplication

    