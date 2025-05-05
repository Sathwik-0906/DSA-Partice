def check_palindrome(s: str) ->bool:
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1

    return True

def main():
    s="racecar"
    res=check_palindrome(s)
    if res == False:
        print("Not a palindrome")
    else:
        print("palindrome")
main()