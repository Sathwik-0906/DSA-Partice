# Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

from collections import defaultdict
def find_long_sub(s,k):
    map= defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        map[s[right]]+=1
        while len(map) > k:
            map[s[left]]-=1
            if map[s[left]]==0:
                del map[s[left]]
            left+=1

            ans = max(ans,right-left+1)
    return ans

def main():
    s = "eceba"
    k=2
    res=find_long_sub(s,k)
    print(res)

main()