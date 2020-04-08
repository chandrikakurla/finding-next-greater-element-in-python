def Next_Greater_Element(arr):
    for i in range(1,len(arr),1):
        next=-1
        for j in range(i+1,len(arr),1):
            if arr[i]<arr[j]:
                next=arr[j]
                break
        print(str(arr[i])+"-->"+str(next))
array=[10,9,11,13,2]
Next_Greater_Element(array)
