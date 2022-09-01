ar = [2,8,12,15]

def pair(tgt):
    required={}
    for i in range(len(ar)):
        if tgt-ar[i] in required:
            return (required[tgt-ar[i]],i)
        else:
            required[ar[i]]=i
    return required

print(pair(20))
