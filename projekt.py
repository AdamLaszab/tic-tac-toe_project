import random
def velkostplochy(n): ##Funkcia zisti dlzku hracej plochy NxN sachovnice
    return 4*(n-3)+8
def spodnepolia(n): ## Funkcia zisti poziciu v lavom dolnom rohu kde zacina hrac B na NxN sachovnici
    return 2*(n-3)+4
def gensachovnica(n): ## Funkcia naplni list hviezdickami podla velkosti sachovnice NxN
    t=['*']*velkostplochy(n)
    return t
def dlzkaramena(n): ## Funkcia vypocita dlzku jedneho ramena v sachovnici NxN
    return int((n-3)/2)
    

    
def sachovnica(n,hraciaplocha,domcekA,domcekB): ## Funkcia na vypisanie sachovnice pouzivatelovi 
    if(n%2!=0 and n>=5):                        ## Sachovnica skontroluje ci z daneho cisla je mozne vytvorit sachovnicu   
        rameno=dlzkaramena(n)                   ## Dlzka ramena potrebna na vypocty
        dalsie=0                                ## Premenna ktora bude ratat ktory dalsi index hracieho pola ma byt na pozicii
        dalsie1=0                               ## Pomocna premenna pre dalsie ktoru som pouzil
        indexA=0                                ## Premenna bude index domceku A
        indexB=rameno-1                         ## Premenna bude index domceku B

        print(' '*rameno*2,hraciaplocha[2],hraciaplocha[1],hraciaplocha[0],' '*rameno*2,end="\n") ## Print prvych troch indexov hracieho pola ktore su rovnake pre vsetky velkosti
        odsadenie=2                                         ## Odsadenie sa pouzije na lavej strane sachovnice kde uz indexi 0,1,2 boli pouzite pri prvom printe

        for i in range(1,n-1):
            if(i<rameno):
                dalsie+=1
                print(' '*rameno*2,hraciaplocha[odsadenie+dalsie],domcekA[indexA],hraciaplocha[-dalsie],' '*rameno*2,end="\n")
                indexA+=1

            elif(i>rameno+2):
                dalsie+=1
                print(' '*rameno*2,hraciaplocha[odsadenie+dalsie],domcekB[indexB],hraciaplocha[-dalsie],' '*rameno*2,end="\n")
                indexB-=1

            elif(i==rameno):
                print(" ",end='')
                for j in reversed(range(1,n-rameno-1)):
                    print(hraciaplocha[odsadenie+j+dalsie],end=' ')
                print(domcekA[indexA],end=' ')
                for k in range(1,n-rameno-1):
                    print(hraciaplocha[-k-i+1],end=' ')
                    dalsie+=1
                print('')

            elif(i==rameno+1):
                dalsie+=1
                print(' ',end='')
                print(hraciaplocha[odsadenie+dalsie],end=' ')

                for _ in range(rameno):
                    print('D',end=' ')
                print('X',end=' ')

                for _ in range(rameno):
                    print('D',end=' ')
                print(hraciaplocha[-dalsie])

            elif(i==rameno+2):
                print(" ",end='')
                dalsie1=dalsie

                for _ in range(1,n-rameno-1):
                    dalsie+=1
                    print(hraciaplocha[odsadenie+dalsie],end=' ')
                print(domcekB[indexB],end=' ')
                indexB-=1

                for p in reversed(range(1,n-rameno-1)):
                    print(hraciaplocha[-dalsie1-p],end=' ')
                    
                print('')              

        print(' '*rameno*2,hraciaplocha[dalsie+3],hraciaplocha[dalsie+4],hraciaplocha[dalsie+5],' '*rameno*2,end="\n")
    else:
        print("Z tochto cisla sa neda spravit sachovnica")
    



def hra(n):
    figurkyA=dlzkaramena(n)
    figurkyB=dlzkaramena(n)
    poziciaA=0
    poziciaB=spodnepolia(n)
    priebezneB=0
    domcekA=['D']*dlzkaramena(n)
    domcekB=['D']*dlzkaramena(n)    
    hraciaplocha=gensachovnica(n)
    hraciaplocha[poziciaA]="A"
    hraciaplocha[poziciaB]="B"
    while(True):
        sachovnica(n,hraciaplocha,domcekA,domcekB)
        kockaA=random.randint(1,6)
        kockaB=random.randint(1,6)
        hraciaplocha[poziciaA]="*"
        hraciaplocha[poziciaB]="*"
        poziciaA+=kockaA
        poziciaB+=kockaB
        priebezneB+=kockaB
        if(poziciaA>velkostplochy(n)-1):
            poziciaA=poziciaA-kockaA
        elif(poziciaA==velkostplochy(n)-1):
            figurkyA-=1
            domcekA[figurkyA]='A'
            poziciaA=0
        if(priebezneB>velkostplochy(n)-1):
            poziciaB=poziciaB-kockaB
            priebezneB=priebezneB-kockaB
        elif(priebezneB==velkostplochy(n)-1):
            figurkyB-=1
            domcekB[figurkyB]='B'
            poziciaB=spodnepolia(n)
            priebezneB=0
        elif(poziciaB>velkostplochy(n)-1):
            poziciaB=poziciaB-velkostplochy(n)
        if(poziciaB==poziciaA):
            if(kockaA>kockaB):
                poziciaB=spodnepolia(n)
                priebezneB=0
            else:
                poziciaA=0
        hraciaplocha[poziciaA]="A"
        hraciaplocha[poziciaB]="B"
        print("")
        print("Hod kocky A=",kockaA,"Hracovi A zostavaju",figurkyA,"figurky")
        print("Hod kocky B=",kockaB,"Hracovi B zostavaju",figurkyB,"figurky")  
        print("")
        if(figurkyA==0):
            hraciaplocha[0]="*"
            sachovnica(n,hraciaplocha,domcekA,domcekB)
            print("Vyhral A")
            break
        if(figurkyB==0):
            hraciaplocha[spodnepolia(n)]="*"
            sachovnica(n,hraciaplocha,domcekA,domcekB)
            print("Vyhral B")
            break






hra(9)


