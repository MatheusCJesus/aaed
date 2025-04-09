# Generating permutation has always been an important problem in computer science. 
# In this problem you will have to generate the permutation of a given string in ascending order. 
# Remember that your algorithm must be efficient.
"""
Input
The first line of the input contains an integer n, 
which indicates how many strings to follow. 
The next n lines contain n strings. 
Strings will only contain alphanumeric and never contain any space. 
The maximum length of the string is 10.

Output
For each input string print all the permutations possible in ascending order. 
Note that the strings should be treated, 
as case sensitive strings and no permutation should be repeated. 
A blank line should follow each output set.
"""

"""
Sample input: 
3
ab
abc
bca

Sample output:
ab
ba

abc
acb
bac
bca
cab
cba

abc
acb
bac
bca
cab
cba
"""

#%%
def str_to_list(string):
    """
    This function takes a string and converts it into a list of characters.
    """
    return [char for char in string]

#%%
# Function to sort the string
def bubble_sort(list):
    
    interator = len(list)
    isSorted = False
    
    while isSorted == False:
        
        isSorted = True
        for i in range(interator - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                isSorted = False
        
        interator -= 1
    return list


# %%
bubble_sort(str_to_list("bacrtg"))
# %%
def permutation(string):
    """
    This function takes a string and returns all the permutations of the string in ascending order.
    """
    
    # Convert the string to a list of characters
    list = str_to_list(string)
    
    # Sort the list of characters
    sorted_list = bubble_sort(list)
    
    sorted_permutations = []

    # Generate all permutations of the string
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            # Swap the characters
            sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
            # Append the permutation to the list
            sorted_permutations.append("".join(sorted_list))
            # Swap back the characters
            sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

