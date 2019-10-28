# retezec = 20 * '-'
# print(retezec)

def vyhodnot(retezec): 
    '''vyhodnoti retezec pro piskvorky.'''

    if 'xxx' in retezec:
        #print('Vyhrál hráč s křížky.')
        return 'x'
    elif 'ooo' in retezec:
        #print('Vyhrál hráč s kolečky')
        return 'o'
    elif '-' in retezec:
        #hra pokracuje
        return '-'
    else:
        #remiza
        return '!'   


# vyhodnot(retezec)
# vyhodnot('----oxoxxooo----')


def tah(retezec, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    return retezec[:cislo_policka] + symbol + retezec[cislo_policka + 1:]


def tah_hrace(retezec):
    "definuje, jak hraje hrac."
      
    pole_hrace = int(input('Na jake pole budes hrat?'))
    while pole_hrace < 0 or pole_hrace > 19 or retezec[pole_hrace] != '-':
        pole_hrace = int(input('Spatny vstup. Priste to zkus lepe. Na jake pole budes hrat ted?'))
        
    return tah(retezec, pole_hrace, "x")


def tah_pocitace(retezec):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    from random import randrange
    pole_pocitace = randrange(20)
    while retezec[pole_pocitace] != '-':
        pole_pocitace = randrange(20)

    return tah(retezec, pole_pocitace, 'o')    

# retezec = '-x---oxoxxooo----ox-'

# tah_pocitace(retezec)

def piskvorky1d():
    retezec = 20 * '-'
    cislo_kola = 0
    
    while vyhodnot(retezec) == '-':
        retezec = tah_hrace(retezec)
        cislo_kola = cislo_kola + 1
        print(cislo_kola, retezec)
        if  vyhodnot(retezec) != '-':
            break
        retezec = tah_pocitace(retezec)
        cislo_kola = cislo_kola + 1
        print(cislo_kola, retezec)
    
    vysledek = vyhodnot(retezec)
    if vysledek == "x":
        print("Vyhral jsi.")
    elif vysledek == "o":
        print("Vyhral pocitac.")
    else:
        print("Remiza.")        
      
     
   
piskvorky1d()
    