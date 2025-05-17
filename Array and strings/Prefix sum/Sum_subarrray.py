# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] 
# and an integer limit, return a boolean array that represents the answer to each query. 
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], 
# and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].


def sub_array(nums,queries,limit):
    prefix_sum=[0]*(len(nums)+1)
    for i in range(len(nums)):
        prefix_sum[i+1]=prefix_sum[i]+nums[i]

    ans=[]
    for x,y in queries:
        cur = prefix_sum[y+1]-prefix_sum[x]
        ans.append(cur<limit)
    return ans

def sub_arrays(nums,queries,limit):
    prefix_sum=[0]*(len(nums)+1)
    for i in range(len(nums)):
        prefix_sum[i+1]=prefix_sum[i]+nums[i]

    ans=[]
    for x,y in queries:
        cur = prefix_sum[y+1]-prefix_sum[x]
        ans.append(cur<limit)
    return ans
def main():
    nums=[1, 6, 3, 2, 7, 2]
    queries = [[0, 3], [2, 5], [2, 4]]
    limit = 13
    res = sub_array(nums,queries,limit)

    print(res)

main()