A = []

def check(a, b) :
    for i in range(0, len(a)-1):
        if a[i][0] == b:
            return i
    return -1
    
def new() :

    tag = input("hashtag :")
    
    x = check(A, tag)
    
    if x == -1:
        A.append([tag])
        
    text = input("text :")
    A[x].append(text)
    
while 1 :

    new()
    print (A)
