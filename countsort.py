def count_sort(lst):
    maxv=max(lst)
    count=[0]*(maxv+1)
    for i in lst:
        count[i]=count[i]+1
    for i in range(1,len(count)):
        count[i]=count[i]+count[i-1]
    output=[0]*len(lst)
    for i in reversed(lst):
        output[count[i]-1]=i
        count[i]-=1
    for i in range(len(lst)):
        lst[i]=output[i]
    return lst
n=int(input("enter the size of the list"))
lst=[]
for i in range(n):
    lst.append(int(input()))
result=count_sort(lst)
print(result)
