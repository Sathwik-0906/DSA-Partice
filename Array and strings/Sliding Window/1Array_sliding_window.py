def find_lag_sub(nums,k):
    i = 0
    ans = 0
    sum =0
    for j in range(len(nums)):
        sum+=nums[j]
        while sum > k:
            sum-=nums[i]
            i+=1
        ans = max(ans,j-i+1)
    return ans

def main():
    print("longest sub array of size k is :",find_lag_sub([3,1,2,7,4,2,1,1,5],8))

main()
