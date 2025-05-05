# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

def sum_of_two(nums,target):
    i=0
    j=len(nums)-1

    while i < j:
        c = nums[i]+nums[j]

        if c==target:
            return True
        if c>target:
            j-=1
        else:
            i+=1
    return False

def main():
    arr = [1, 2, 4, 6, 8, 9, 14, 15]
    res = sum_of_two(arr,13)
    print(res)
main()