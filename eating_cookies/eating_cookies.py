'''
Input: an integer
Returns: an integer
'''
# Time complexity of this solution is 3^n
# def eating_cookies(n):
#     # Your code here
#     # Base case
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1

#     # How can we GET to the base case
#     # what if I ate just 1 cookie
#     number_of_ways = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3) 

#     return number_of_ways

# This solution is O(n)
def eating_cookies(n, cache):
    # Your code here
    # Base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    # Before we try to solve our problem
    # lets see if the answer is already stored in cache
    if cahce[n] > 0:
        # this must have been precomputed!
        return cache[n]

    # How can we GET to the base case
    # what if I ate just 1 cookie
    number_of_ways = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    cache[n] = number_of_ways 

    return number_of_ways

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
