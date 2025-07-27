
def sortArray(nums):
    # merge sort
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    leftarr = sortArray(nums[:mid])
    rightarr = sortArray(nums[mid:])
    print("left arr",leftarr,"right arr",rightarr)

    return(merge(leftarr,rightarr))

def merge(left,right):
    temparr =[]
    i,j=0,0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            temparr.append(left[i])
            i+=1
        else:
            temparr.append(right[j])
            j+=1
    temparr.extend(left[i:])
    temparr.extend(right[j:])
    return temparr


arr = [5, 2, 9, 1, 6, 3,12,4,0]
sorted_arr = sortArray(arr)
print("Sorted array:", sorted_arr)