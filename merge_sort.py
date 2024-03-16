def merge_sort(arr,dummy):
    if(len(arr)>1):
        mid=len(arr)//2
        l=arr[:mid]
        merge_sort(l,dummy)
        r=arr[mid:]
        merge_sort(r,dummy)
        j=k=a=0
        while(j<len(l) and k<len(r)):
            if(l[j]<r[k]):
                arr[a]=l[j]
                j+=1
            else:
                arr[a]=r[k]
                k+=1
            a+=1
        while(j<len(l)):
            arr[a] = l[j]
            j+=1
            a+=1
        while(k<len(r)):
            arr[a] = r[k]
            k+=1
            a+=1
        if(len(arr)==dummy):
            return arr
arr=[12,1,11,13,5,6,7]
arr=merge_sort(arr,len(arr))
print(arr)
