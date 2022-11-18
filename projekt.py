import random
def velkostplochy(n):
    return 4*(n-3)+8
def spodnepolia(n):
    return 2*(n-3)+4

    
def sachovnica(n,hraciaplocha):
    if(n%2!=0 and n>4):    
        rameno=int((n-3)/2)
        dalsie=0
        dalsie1=0
        print(' '*rameno*2,hraciaplocha[2],hraciaplocha[1],hraciaplocha[0],' '*rameno*2,end="\n")
        for i in range(1,n-1):
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
            elif(i==rameno+2):
                print(" ",end='')
                dalsie1=dalsie
                for u in range(1,n-rameno-1):
                    dalsie+=1
                    print(hraciaplocha[2+dalsie],end=' ')
                print('D',end=' ')
                for p in reversed(range(1,n-rameno-1)):
                    print(hraciaplocha[-dalsie1-p],end=' ')
                    
                print('')
            else:
                dalsie+=1
                print(' '*rameno*2,hraciaplocha[2+dalsie],'D',hraciaplocha[-dalsie],' '*rameno*2,end="\n")
        print(' '*rameno*2,hraciaplocha[dalsie+3],hraciaplocha[dalsie+4],hraciaplocha[dalsie+5],' '*rameno*2,end="\n")
    else:
        print("Z tochto cisla sa neda spravit sachovnica")
    



def hra(n):
    poziciaA=0
    poziciaB=spodnepolia(n)
    hraciaplocha=['*']*velkostplochy(n)
    hraciaplocha[poziciaA]="A"
    hraciaplocha[poziciaB]="B"
    sachovnica(n,hraciaplocha)





hra(9)


