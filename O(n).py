'''
Linear Time --> O(n)
As the number of inputs/elements increase, the number of operations increase as well.
Notice: Iterating through half a collection is still O(n).
Also: Two separate collections: O(a+b).
'''

'''
We can see here that as the inputs increase (the elements in the arrays) we see that
the number of operations increases LINEARLY.
'''
import time
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']

large_arr = []
for i in range(100):
    large_arr.extend(everyone)


def findNemo(arr):
    # t0 = time.time()
    for i in range(len(arr)):
        if arr[i] == 'nemo':
            print('Found Nemo!')
    # t1 = time.time()
    # print(t1-t0)


findNemo(large_arr)  # O(n) --> Linear Time / Proportionally