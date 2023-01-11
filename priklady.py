# import random
# def funkcia(ret):
#     ret=set(list(ret))
#     return ret

# print(funkcia("adam"))

# def funkcia(ret):
#     vysledok=[]
#     for letter in ret:
#         if(ret.count(letter)==1):
#             vysledok+=letter
#     return vysledok

# print(funkcia("adam"))

# def funkcia(t):
#     vysledok=0
#     for element in t:
#         if(len(set(element))==len(element)):
#             vysledok+=1
#     return vysledok
# t=["adam","ema","chris","roland"]
# print(funkcia(t))



# def funkcia(n):
#     t=[]
#     while(True):
#         print("Zadaj cislo")
#         x=input()
#         t+=x
#         if(int(max(t))-int(min(t))>n):
#             return t


# print(funkcia(6))


# def funkcia(n):
#     t=[]
#     z=0
#     while(z<n):
#         print("Zadaj cislo")
#         x=input()
#         t+=x
#         z=len(set(t))
#     return t

# print(funkcia(5))

# def funkcia(A):
#     maxi=A[0][0]
#     for riadok in range(len(A)):
#         for stlpec in range(len(A[0])):
#             if(int(A[riadok][stlpec])>maxi):
#                maxi=A[riadok][stlpec]
#     return maxi

# print(funkcia(A))

# def funkcia(A):
#     maxi=A[0][0]
#     posR=0
#     posS=0
#     vysledok=[]
#     for riadok in range(len(A)):
#         for stlpec in range(len(A[0])):
#             if(int(A[riadok][stlpec])>maxi):
#                maxi=A[riadok][stlpec]
#                posR=riadok
#                posS=stlpec
#     vysledok.append(posR)
#     vysledok.append(posS)
#     return vysledok

# print(funkcia(A))
A=[[1,2,0,0],[3,4,0,0],[11,3,0,0]]
def funkcia(A):
    vysledok=0
    t=[]
    p=0
    for stlpec in range(len(A[0])):
        for riadok in range(len(A)):
            t.append(A[riadok][stlpec])
        for element in t:
            if(int(element)==0):
                p+=1
        if(len(t)==p):
            vysledok+=1
        p=0
        t=[]
    return vysledok

print(funkcia(A))
                
                
            
                

        
