from cmath import inf


nums=[3,-1,12]




def maxProdTwoEle(nums):
    first,sec= 0,0
    for num in nums:
        if num > first:
            sec=first
            first=num            
        else:
            sec = max(num,sec)
    return first*sec    

print(maxProdTwoEle(nums))            
        
