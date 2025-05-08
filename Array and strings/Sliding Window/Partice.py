# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000




from typing import List

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         cur = 0.0
#         for i in range(k):
#             cur += nums[i]

#         ans = cur / k

#         for i in range(k, len(nums)):
#             cur += nums[i] - nums[i - k]
#             b = cur / k
#             ans = max(ans, b)

#         return ans


# sol = Solution()
# print(sol.findMaxAverage([5], 1))  # Expected: 5.0



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = cur = 0
        for right in range(len(nums)):
            if nums[right]==0:
                cur+=1
                
            while cur>k:
                if nums[left]==0:
                    cur-=1
                left+=1
            
            ans=max(ans,right-left+1)
        
        return ans
    

sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 1))


