###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
# def dp_make_weight(egg_weights, target_weight, memo = {}):
#     """
#     Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
#     an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
#     Parameters:
#     egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
#     target_weight - int, amount of weight we want to find eggs to fit
#     memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
#     Returns: int, smallest number of eggs needed to make target weight
#     """
#     # TODO: Your code here
#     target_weight_copy=target_weight
#     decending_weight=sorted(egg_weights,reverse=True)
#     for weight in decending_weight:
#         memo[weight]=target_weight_copy//weight
#         target_weight_copy-=memo[weight]*weight
#     return sum(memo.values()),memo

def dp_make_weight(egg_weights, target_weight, memo = {}):
    total_num=0
    remaining_weight=target_weight
    decending_weight=sorted(egg_weights,reverse=True)
    if len(decending_weight)==1:
        return remaining_weight
    else:
        numegg=remaining_weight//decending_weight[0]
        memo[decending_weight[0]]=numegg
        remaining_weight=remaining_weight%decending_weight[0]
        total_num=total_num+memo[decending_weight[0]]+dp_make_weight(decending_weight[1:],remaining_weight,memo)
    
    return total_num


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1,5,10,25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    egg_weights=(1,5,10,20)
    n = 99
    print("Egg weights = (1, 5, 10, 20)")
    print("n = 99")
    print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    
    