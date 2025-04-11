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
    Uses a non-recursive approach based on lexicographic ordering.
    """
    # Convert the string to a list of characters
    chars = str_to_list(string)
    
    # Sort the list of characters to start with the first permutation
    chars = bubble_sort(chars)
    
    # Initialize the result list with the first permutation
    result = [''.join(chars)]
    
    while True:
        # 1. Find the largest index i such that chars[i] < chars[i+1]
        i = len(chars) - 2
        while i >= 0 and chars[i] >= chars[i+1]:
            i -= 1
            
        # If no such index exists, we've generated all permutations
        if i < 0:
            break
            
        # 2. Find the largest index j > i such that chars[j] > chars[i]
        j = len(chars) - 1
        while chars[j] <= chars[i]:
            j -= 1
            
        # 3. Swap chars[i] and chars[j]
        chars[i], chars[j] = chars[j], chars[i]
        
        # 4. Reverse the suffix starting at chars[i+1]
        chars[i+1:] = chars[i+1:][::-1]
        
        # Add the new permutation to the result
        result.append(''.join(chars))
    
    return result

# %%
permutation("abc")
# %%
