# import time

'''
Big O is a way for us to measure, in terms of efficiency, what is good code and what is bad code -
what is code that can scale: as the number of inputs / elements increases it does not
constantly slow down more and more.

Big O notation is a language we use for talking about how long an algorithm takes to run.

When we talk about Big O and scalability of code we simply mean - when we grow bigger and bigger with
our input, how much does the algorithm or function slow down.

Algorithmic Efficiency:
As the number of Elements increases, how many more operations do we have to do.

So, remember: when we talk about Big O and scalability of code we simply mean - when we grow bigger
and bigger with our input, how much does the algorithm slow down - the less it slows down or the
slower it slows down the better it is.

O(1) --> Constant Time
O(n) --> Linear Time / Proportionally
O(n^2) --> Quadratic Time

BIG O RULES:
1. Worst Case
2. Remove Constants
3. Different Terms for Inputs
4. Drop Non Dominants

for loops one-after-the-other we use ADDITION.
for loops one-inside-the-other we use MULTIPLICATION.

Scalability - as things grow larger and larger, does it scale?
'''

# BIG O Exersice 1 -
# What is the Big O of the below function? (Hint, you may want to go line by line)

def anotherFunction():
    pass


def funChallenge(input):
    a = 10      # O(1) - this is only running once when we run funChallenge() and does not matter how big the input is.
    a = 50 + 3  # O(1)

    for i in range(input.length):  # O(n)
        anotherFunction()   # O(n) - How many times this function runs? n times - depends on the size of the input.
        stranger = True     # O(n)
        a += 1  # O(n)

    return a  # O(1)

    # In total: BIG O(3 + 4n) = O(n)


# BIG O Exersice 2 -
# What is the Big O of the below function? (Hint, you may want to go line by line)
def anotherFunChallenge(input):
    a = 5   # O(1)
    b = 10  # O(1)
    c = 50  # O(1)
    for i in range(input.length):  # O(n)
        x = i + 1  # O(n) - runs O(n) times - depending on the size of the input
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in range(input.length):  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    whoAmI = "I don't know"  # O(1)

    # In Total: BIG O(4 + 7n) = O(n)

'''
Simplifying Big-O:
When we talk about big-O we are only going to give (in interviews) one of the answers in the BigO complexity
chart. 
This is allowed according to these rules - 
BIG O RULES:
1. Worst Case
    When calculating big-O we always think about the worst case! For example - running on the entire array.
2. Remove Constants
    Ignoring variable assignments and small calculations - for ex. O(n/2 + 100) = O(n + 1) = O(n)
3. Different Terms for Inputs
    If we have 2 inputs and two for loops, each running on each input then we get - O(n+m)
4. Drop Non Dominants
    Always keep the most important / dominant term! For example: O(n^2 + n) = O(n^2)
'''
