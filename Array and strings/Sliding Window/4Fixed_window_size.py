# Fixed window size
# In the examples we looked at above, our window size was dynamic. We tried to expand it to the right as much as we could while keeping the window within some constraint and removed elements from the left when the constraint was violated. Sometimes, a problem will specify a fixed length k.

# These problems are easy because the difference between any two adjacent windows is only two elements (we add one element on the right and remove one element on the left to maintain the length).

# Start by building the first window (from index 0 to k - 1). Once we have a window of size k, if we add an element at index i, we need to remove the element at index i - k. For example, k = 2 and you currently have elements at indices [0, 1]. Now, we add 2: [0, 1, 2]. To keep the window size at k = 2, we need to remove 2 - k = 0: [1, 2].

# Here's some pseudocode:

# function fn(arr, k):
#     curr = some data to track the window

#     // build the first window
#     for (int i = 0; i < k; i++)
#         Do something with curr or other variables to build first window

#     ans = answer variable, probably equal to curr here depending on the problem
#     for (int i = k; i < arr.length; i++)
#         Add arr[i] to window
#         Remove arr[i - k] from window
#         Update ans

#     return ans


# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

# As we mentioned before, we can build a window of length k and then slide it along the array. Add and remove one element at a time to make sure the window stays size k. If we are adding the value at i, then we need to remove the value at i - k.

# After we build the first window we initialize our answer to curr to consider the first window's sum.

def fixed_window_max_subarray_sum(nums,k):
    left  = 0
    cur = 0
    for right in range(k):
        cur+=nums[right]
    ans=cur
    for i in range(k,len(nums)):
        #1st its add nums[i] into cur sum value then from that sum value it minus the value of nums[i-k]
        cur+=nums[i]-nums[i-k]
        ans=max(ans,cur)

    return ans


def main():
    nums=[3,-1,4,12,-8,5,6]
    k=4
    print("Max sum of the sub array: ",fixed_window_max_subarray_sum(nums,k))

main()