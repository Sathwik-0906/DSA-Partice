# Example 2: 2270. Number of Ways to Split Array

# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or
# equal to the sum of the second section. The second section should have at least one number.
from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(n - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans
    
sol = Solution()
res=sol.waysToSplitArray([10,4,-8,7])
print(res)



# Do we need the array?
# In this problem, the order in which we need to access prefix is incremental: 
# to find leftSection, we do prefix[i] as i increments by 1 each iteration.

# As such, to calculate leftSection we don't actually need the array. We can just initialize leftSection = 0 
# and then calculate it on the fly by adding the current element to it at each iteration.

# What about rightSection? By definition, the right section contains all the numbers in the array that aren't 
# in the left section. Therefore, we can pre-compute the sum of the entire input as total, then calculate rightSection as total - leftSection.

# We are still using the concept of a prefix sum as each value of leftSection represents the sum of a prefix.
# We have simply replicated the functionality using an integer instead of an array.

class Solutions:
    def waysToSplitArrays(self, nums: List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans
    
sol = Solutions()
res=sol.waysToSplitArrays([10,4,-8,7])
print(res)


# Do we need the array?
# In this problem, the order in which we need to access prefix is incremental: 
# to find leftSection, we do prefix[i] as i increments by 1 each iteration.

# As such, to calculate leftSection we don't actually need the array. We can just initialize leftSection = 0 
# and then calculate it on the fly by adding the current element to it at each iteration.

# What about rightSection? By definition, the right section contains all the numbers in the array that aren't 
# in the left section. Therefore, we can pre-compute the sum of the entire input as total, then calculate rightSection as total - leftSection.

# We are still using the concept of a prefix sum as each value of leftSection represents the sum of a prefix.
# We have simply replicated the functionality using an integer instead of an array.

