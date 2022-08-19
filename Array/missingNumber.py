

nums = [1,2,4,5]


# def missingNumber(myList):
#     missing=[]
#     for i in range(myList[0],myList[-1]+1):
#         if i not in myList:
#             missing.append(i)  
#     return missing         

# print(missingNumber(myList))

def missingNumber( nums) :
        n = len(nums)
        sum_of_n = (((n+1)*(n+2))/2)  #sum of n numbers 10
        sum_of_elems = 0
        for num in nums:
            sum_of_elems += num    #total sum of elements in array
            
        return int(sum_of_n - sum_of_elems)

print(missingNumber(nums))
