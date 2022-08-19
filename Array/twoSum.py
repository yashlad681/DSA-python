ar = [1,2,3,4,5,6,7]

def pair(tgt):
    required={}
    for i in range(len(ar)):
        if tgt-i in required:
            return (required[tgt-ar[i]],i)
        else:
            required[ar[i]]=i
    return required

print(pair(7))
