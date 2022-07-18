'''
O(1) --> Constant Time
In the function below - const_time_func() - what is the big-O of this function?
How many steps/operations does this function take if the array increases from zero to 10/100/100,000?
This is Constant Time - no matter how many times the array increases / no matter how many elements we have
in the array we are always taking the same amount of actions/operations - we always print the first
item in the array.

When in comes to O(1) we don't care about O(1) or O(2) or O(3) or even O(100) etc.
We simply round it down to O(1).
O(1) is Excellent! It's very scalable! We love it :)
It does not matter how many elements we have, it's ALWAYS going to run the same!
'''

everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']

def const_time_func(arr):
    '''
    :param arr: array of elements
    :return: always prints out the first element of the array
    '''
    print(arr[0])


const_time_func(everyone)  # O(1) --> Constant Time

def print_first_two_elements(arr):
    '''
    :param arr:
    :Description: Each times this function runs 2 operations
    '''
    print(arr[0])  # O(1)
    print(arr[1])  # O(1)

# This function in total running O(2) operations every time.
# So, no matter how big the array gets, the number of operations is going to be 2.
