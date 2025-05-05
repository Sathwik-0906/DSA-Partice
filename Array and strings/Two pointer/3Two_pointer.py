# combing two arrays in to one which are sorted
def combine(arr1,arr2):
    i = j = 0
    arr=[]
    while i < len(arr1) and  j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while i < len(arr1):
        arr.append(arr1[i])
        i+=1
    while j < len(arr2):
        arr.append(arr2[j])
        j+=1

    return arr

def main():
    print("combined aaray of aar1 and arr2 is :",combine([2,2,4,4,6,8],[1,3,5,7,9,11]))

main()

        
