'''
O(n^2) --> Quadratic Time
for loops one-inside-the-other we use MULTIPLICATION

Rule of thumb -
If you see nested loops then instead of having two for loops one-after-the-other where we use addition,
when you see loops that are nested we use MULTIPLICATION!

Quadratic Time - every time the number of elements increase then the number of operations increases
quadratically. For example, for 2 elements we get 2^2=4 operations; for 3 elements we have 3^2=9 operations.

As the number of elements increases then the number of operations increases significantly!

Lots of interview questions asks to solve a problem that is initially O(n^2) and make it faster by
perhaps making it into something that is faster.
'''

# Nesting Loops Big O Notation -
# Log all pairs of array

boxes = ['a', 'b', 'c', 'd', 'e']


def logAllPairsOfArray(arr):
    for i in range(len(arr)):      # O(n)
        for j in range(len(arr)):  # O(n)
            print(arr[i], arr[j])


logAllPairsOfArray(boxes)

# O(n * n) = O(n^2) --> Quadratic Time