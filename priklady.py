t=[[1,2],[0,5],[6,7]]
def test(x,y):
    if(x[1]<y[0]):
        return False
    elif(x[0]>y[1]):
        return False
    else:
        return True
def funkcia(A):
    z=[]
    v=False
    for j in range(len(A)):
        for i in range(len(A)):
            if(j!=i):
                if(test(A[j],A[i])== True and A[i][0]<A[j][0] and A[j][1]<A[i][1]):
                    v=True
        if(v==False):
            z.append(A[j])
        v=False

    return z


print(funkcia(t))