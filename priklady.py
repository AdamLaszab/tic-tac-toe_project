import random
##def funkcia():
##    maxi=0
##    akecislo=0
##    x =[]
##    while(True):
##        print("Zadaj cislo")
##        vstup=int(input())
##        if(vstup==0):
##            for item in x:
##                if(maxi<x.count(item)):
##                    maxi=x.count(item)
##                    akecislo=item
##            print(akecislo,maxi)
##            break
##        x.append(vstup)
##
##funkcia()

##t = [1, 2, 3, 4]

##def chop(t):
##    t.pop(0)
##    t.pop(-1)
##
##
##chop(t)
##print(t)
# a=[1,2,10,2,2,5]
# b=[[1,0,2],[3,3,-1],[-2,1,3]]
# c=[[0]*len(a[0]) for _ in range(len(a))]
# def zrataj(a,b):
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             c[i][j]=a[i][j]+b[i][j]

# zrataj(a,b)
# print(c)

# def vynasob(a,b):
#     if(len(a[0])==len(b)):
#         c=[[0]*len(b[0]) for _ in range(len(a))]
#         for i in range(len(c)):
#             for j in range(len(c[0])):
#                 spolu=0
#                 for k in range(len(a[0])):
#                     spolu+=a[i][k]*b[k][j]
#                 c[i][j]=spolu
#         return c
#     else:
#         print("zle")

# print(vynasob(a,b))       
# def funkcia(t):
#     spolu=0
#     for item in t:
#         if(t.count(item)==1):
#             spolu+=1
#     return spolu

# print(funkcia(a))

# def funkcia(n):
#     vysledok=0
#     if(n==1):
#         return 1
#     else:
#         vysledok=n+funkcia(n-1)
#     return vysledok

# print(funkcia(5))

# def funkcia(n):
#     vysledok=0
#     if(n==0):
#         return 0
#     else:
#         print("Zadaj cislo")
#         x=int(input())+funkcia(n-1)
#         vysledok+=x
#     return vysledok

# print(funkcia(5))

# def funkcia(n):
#     if(n==0):
#         return 0
#     else:
#         print("Zadaj cislo")
#         x=int(input())
#         recurse=funkcia(n-1)
#         if(x%2==0):
#             return recurse+1
#         else:
#             return recurse
        

# print(funkcia(5))

# def funkcia(n):
#     if(n==0):
#         return True
#     else:
#         print("Zadaj cislo")
#         x=int(input())
#         priebezne=True
#         recurse=funkcia(n-1)
#         if(x%2==0):
#             priebezne=True
#         else:
#             priebezne=False    
#         if(priebezne==recurse):
#             return True
#         else:
#             return False

def test_prvociselnosti(a):
  if a < 2:
    raise ValueError("Prvocislo nemoze byt menise ako 2")
  for i in range(2, a):
    if a % i == 0:
      return False
  return True

def sucet_prvocisel(n):
  if n < 2:
    raise ValueError("Vstup musi byt vacsi ako 1")

  if n == 2:
    return 2
  
  if test_prvociselnosti(n):
    return n + sucet_prvocisel(n - 1)
  return sucet_prvocisel(n - 1)

        

print(sucet_prvocisel(13))
        

