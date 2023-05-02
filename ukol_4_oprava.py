""" Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420". """

# nacti cislo pro zpravu
tel_cislo = ""
platne_tel_cislo = False
tel_cislo = str(input("1 Zadej telefonni cislo kam se ma poslat SMS v ramci CR, zacni +420: "))

def over_tel_cislo(tel_cislo):
    cislo_platne = True
    tel_cislo_bez_mezer = tel_cislo.replace(" ","")
    print(f"1 tel cislo bez mezer {tel_cislo_bez_mezer} ")
    if tel_cislo_bez_mezer[0:4] != "+420":
        tel_cislo_bez_mezer = "+420"+ tel_cislo_bez_mezer
        #print(f"2 tel cislo bez mezer pridano +420: {tel_cislo_bez_mezer} ")
    if len(tel_cislo_bez_mezer) !=13:
        #print(f"1 Vase SMS nebude zaslana na cislo {tel_cislo_bez_mezer} protoze je neplatne-znaky mimo cisla/predvolba mimo 420")
        cislo_platne = False
    for i in range(4,len(tel_cislo_bez_mezer)):
        if tel_cislo_bez_mezer[i] < '0' or tel_cislo_bez_mezer[i] > '9':
            #print(f"2 Vase SMS nebude zaslana na cislo {tel_cislo_bez_mezer} protoze je neplatne-znaky mimo cisla/predvolba mimo 420")
            cislo_platne = False
    return cislo_platne

def vypocet_ceny_sms(sms_zprava):
    delka_zpravy = int(len(sms_zprava))
    print(f"pri delce zpravy {delka_zpravy} ")
    if delka_zpravy == 0:
        cena_sms = 0
        print(f"cena sms s {len(sms_zprava)} znaky je {cena_sms} ")
    else:
        
        cena_sms = int(((delka_zpravy-1)/5)+1)*3
        print(f"cena sms s {len(sms_zprava)} znaky je {cena_sms} ")
    return cena_sms 


platne_tel_cislo = over_tel_cislo(tel_cislo)
# nacti zpravu
if platne_tel_cislo:
    sms_zprava = str(input("2 Zadej text SMS/ zpoplatnena 3 Kc za zapocatych 180 slov: "))
    cena_teto_sms = vypocet_ceny_sms (sms_zprava)

else: 
    print(f"2 Vase SMS nebude zaslana na cislo {tel_cislo} protoze je neplatne")





