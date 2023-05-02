""" Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

Vytvoř seznam průměrných teplot pro každý den.
Vytvoř seznam ranních teplot.
Vytvoř seznam nočních teplot.
Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu. """

#eznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
#seznam seznamů
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
#print(teploty)
#print(teploty[0])

denni_prumer=[]
ranni_teploty=[]
nocni_teploty=[]
poledni_nocni_teploty=[]
dvojice_poledni_nocni=[]


#Vytvoř seznam průměrných teplot pro každý den.

def prumerna_teplota_dne (teploty_l):
    soucet_teplot_dne=0
    pocet_teplot_dne = int(len(teploty_l))
    #print(f'pocet teplot v dnu {len(teploty_l)}')
    for mereni in teploty_l:
        #print(f'mereni {mereni}') 
        soucet_teplot_dne = soucet_teplot_dne + mereni
    prumerna_teplota_dne_l = soucet_teplot_dne/pocet_teplot_dne
    return prumerna_teplota_dne_l


for den in teploty:
    prumer_dne = prumerna_teplota_dne(den)
    denni_prumer.append(prumer_dne)
print(f'denni_prumer {denni_prumer}')  

#Vytvoř seznam ranních teplot
for den in teploty:
    ranni_teploty.append(den[0])
print(f'ranni_teploty {ranni_teploty}') 

#Vytvoř seznam nočních teplot.
for den in teploty:
    nocni_teploty.append(den[3])
print(f'nocni_teploty {nocni_teploty}') 

#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu
i_dne = 0
dvojice_poledni_nocni.append(0)
dvojice_poledni_nocni.append(0)
for den in teploty:
    poledni_nocni_teploty.append(dvojice_poledni_nocni)
    #print(f'poledni_nocni_teploty {poledni_nocni_teploty}')    
    poledni_nocni_teploty[i_dne][0]=(den[1])
    poledni_nocni_teploty[i_dne][1]=(den[3])
    i_dne+=1
print(f'poledni_nocni_teploty {poledni_nocni_teploty}') 



