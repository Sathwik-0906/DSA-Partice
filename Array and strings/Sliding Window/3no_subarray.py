# Input:
# nums = [10, 5, 2, 6]
# k = 100
# Table Columns:
# right: Current index in the loop

# nums[right]: Element added to the window

# cur: Product of the current window

# Action: What’s happening (multiply, enter while, divide, move left, etc.)

# left: Position of the left pointer

# Valid Subarrays Count: Subarrays ending at current right index


# Step-by-Step Example (nums = [10, 5, 2, 6], k = 100):
# Let’s walk through up to the point where cur //= nums[left] is triggered:

# Iteration 1:
# right = 0

# cur = 1 * nums[0] = 10 → OK, cur < 100

# Iteration 2:
# right = 1

# cur = 10 * 5 = 50 → OK, cur < 100

# Iteration 3:
# right = 2

# cur = 50 * 2 = 100 → NOT OK, cur >= 100

# Now enter the while loop:

def no_sub_array(nums,k):
    left = ans = 0
    cur = 1

    for right in range(len(nums)):
        cur*=nums[right]
        while cur >= k :
            cur//=nums[left]
            left+=1
        ans+=right - left + 1
    return ans


def main():
    nums=[10,5,2,6]
    k=100
    print("No of Sub array Will be: ",no_sub_array(nums,k))

main()