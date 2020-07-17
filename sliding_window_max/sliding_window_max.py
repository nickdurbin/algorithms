'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# This solution is O(n^2)
def sliding_window_max(nums, k):
    # Your code here
    output_arr = []

    for i in range(len(nums) - k + 1):
        current_window = nums[i:i+k]
        current_max = max(current_window)
        output_arr.append(current_max)

    return output_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
