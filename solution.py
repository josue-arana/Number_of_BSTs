# Given n, how many structurally unique BST’s exist that store values 1,..,n?
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

# input: the desired nth number
# output: the number of BSTs for a tree with n nodes. 
def num_bsts(n):
    #edge case.
    if n is None or n < 0:
        return None

    #container
    seq = {0:1, 1:1}

    for i in range(2, n+1):
        for j in range(0, i):
            if i in seq:
                seq[i] += seq[j]*seq[i-j-1]
            else:
                seq[i] = seq[j]*seq[i-j-1]

    return seq[n]


# Explanation: We start the algorithm by checking the edge cases, if the given input is null or negative since we
# cannot have a negative. Then we create a dictionary to store the results and initialize the first two base cases, 
#  0 and 1. We then loop i from 2 to n+1 and also an inner loop from 0 to i while also storing and adding the result 
# to the corresponding index, and also use the previous stored results dynamically to be efficient. 
#
# This way we can store the elements in the pattern to produce the catalan number sequence: 1,1,2,3,5,14,42... 
# 
# For example: if we the given nth number is 3, then the loop would do the following:
#
#   We already know the first 2
#   seq[0] = 1
#   seq[1] = 1  
#  
#   i represents the outer loop from i to n+1. 
#   j represents the inner loop from j to i.
#       i = 2 
#       j = 0   seq[2]  = seq[0] * seq[1]  = 1 * 1 = 1
#       j = 1   seq[2] += seq[1] * seq[0]  = 1 * 1 = 1    
#           
#       so,   seq[2] = 1 + 1 = 2
#
#       i = 3 
#       j = 0   seq[3]  = seq[0] * seq[3-0-1]  =  seq[0]*seq[2] = 1 * 2 = 2 
#       j = 1   seq[3] += seq[1] * seq[3-1-1]  =  seq[1]*seq[1] = 1 * 1 = 1 
#       j = 2   seq[3] += seq[2] * seq[3-2-1]  =  seq[2]*seq[0] = 2 * 1 = 2   
#          
#       so,  seq[2] = 2 + 1 + 2 = 5     
# 
# Another way to find the sequence is trough the formula for the Catalan Number. 
# Formula: (2n)! / ((n + 1)! * n!)    

# Time Complexit: ~ O(n^2)
# Space Complexity: ~ O(n)






    

    
