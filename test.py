def velkostplochy(n):
    return 4*(n-3)+8

def spodnepolia(n):
    return 2*(n-3)+5

hraciaplocha=[]
for i in range(0,32):
    hraciaplocha.append(i)
    




##hraciaplocha=['*']*velkostplochy(n)



def sachovnica(n):
    rameno=int((n-3)/2)
    dalsie=0
    print(' '*rameno*2,hraciaplocha[2],hraciaplocha[1],hraciaplocha[0],' '*rameno*2,end="\n")
    for i in range(1,n):
        if(i==rameno):
            print(" ",end='')
            for j in reversed(range(1,n-rameno-1)):
                print(hraciaplocha[2+j+dalsie],end=' ')
            print('D',end=' ')
            for k in range(1,n-rameno-1):
                print(hraciaplocha[-k-i+1],end=' ')
                dalsie+=1
            print('')
        elif(i==rameno+1):
            dalsie+=1
            print(' ',end='')
            print(hraciaplocha[2+dalsie],end=' ')
            for i in range(rameno):
                print('D',end=' ')
            print('X',end=' ')
            for i in range(rameno):
                print('D',end=' ')
            print(hraciaplocha[-dalsie])
        else:
            print(' '*rameno*2,hraciaplocha[2+i],'D',hraciaplocha[-i],' '*rameno*2,end="\n")
            dalsie+=1
    








sachovnica(9)


