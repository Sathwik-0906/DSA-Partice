from typing import List

def sortedSquares(self, nums: List[int]) -> List[int]:
    i = 0
    ans=[]
    while i < len(nums):
        ans.append(nums[i]**2)
        i+=1
            
    return ans

def main():
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums))

main()