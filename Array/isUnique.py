arr = [1,2,3,4]

def isUnique(arr):
    n=len(set(arr))
    n1 = len(arr)
    if n!=n1:
        return False
    return True    

print(isUnique(arr))