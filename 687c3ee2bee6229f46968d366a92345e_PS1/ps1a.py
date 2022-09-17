###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows_data=open(filename,'r')
    cows=cows_data.readlines()
    cow_dict={}
    for cow in cows:  
        cow_split=cow.strip('\n').split(',')
        
        cow_dict[cow_split[0]]=int(cow_split[1])
    return cow_dict


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    sorted_cow=sorted(cows.items(),key=lambda x: x[1],reverse=True)
    sorted_cow_dict=dict(sorted_cow)
    summary_cow_list=[]
    used_cows={}
    while len(used_cows)!=len(sorted_cow_dict):
        total_weight=0
        cow_trip_list=[]
        for key in sorted_cow_dict.keys():
            if key not in used_cows.keys():
                if sorted_cow_dict[key]+total_weight<=limit:
                    cow_trip_list.append(key)
                    total_weight=total_weight+sorted_cow_dict[key]
                    used_cows[key]=sorted_cow_dict[key]
        cow_trip_list.append(total_weight)
        summary_cow_list.append(cow_trip_list)     
    return summary_cow_list

# #Test for greedy
# cows = load_cows("ps1_cow_data_2.txt")
# print(greedy_cow_transport(cows))     

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    dict=cows
    parts=get_partitions(cows)
    updated_list=[]
    
    for partition in parts:
        break_out_flag=False
        for combo in partition:
            total_weight=0
            for j in combo:
                total_weight+=dict[j]
                if total_weight>limit:
                    break_out_flag=True
                    break
            if break_out_flag:
                break     
        if break_out_flag==False:
                updated_list.append([partition,len(partition)])      
    return  sorted(updated_list,key=lambda updated_list:updated_list[:][1])[0]
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    print("---Greedy algorithm---")
    print()
    start = time.time()
    print(greedy_cow_transport(cows))
    end = time.time()
    print(end - start, "seconds")
    print("---Brute force algorithm---")
    print()
    start = time.time()
    print(brute_force_cow_transport(cows))
    end = time.time()
    print(end - start, "seconds")

# compare_cow_transport_algorithms()

