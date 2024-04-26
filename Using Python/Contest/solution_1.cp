def mex(arr):
    """
    Function to find the minimum excludant of an array.
    """
    i = 0
    while i in arr:
        i += 1
    return i

def game_score(n, a):
    """
    Function to find the game's score for a single test case.
    """
    # Initialize empty array to store Alice's choices
    c = []

    # Sort array a in non-decreasing order
    a.sort()

    # Iterate over the sorted array a
    for i in range(n):
        if i % 2 == 0:  # Alice's turn
            c.append(a[i])  # Alice chooses the element
        # Bob's turn, do nothing
        
    # Calculate and return the MEX of array c
    return mex(c)

# Input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Output game score for current test case
    print(game_score(n, a))
