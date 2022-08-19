
arr = [-6,1,2,7,6]

def maxProd(arr):
    ans=arr[0]
    cur=1
    for i in arr:
        cur=cur*i
        ans=max(cur,ans)
        if cur==0:
            cur=1
    cur=1
    for i in reversed(arr) :#2nd for  is for test case with only one negative element in arr 
        cur=cur*i
        ans=max(cur,ans)
        if cur==0:
            cur=1
    return ans        




# ---O(n2)
# def maxProd(arr):
#     max=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]*arr[j]>max:
#                 max=arr[i]*arr[j]
#     return max 

print(maxProd(arr))
            