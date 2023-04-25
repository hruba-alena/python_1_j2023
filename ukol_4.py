# nacti cislo pro zpravu
tel_cislo = ""
tel_cislo = str(input("1 Zadej telefonni cislo kam se ma poslat SMS v ramci CR, zacni +420: "))

def over_tel_cislo(tel_cislo):
    cislo_platne = True
    tel_cislo_bez_mezer = tel_cislo.replace(" ","")
    print(f"1 tel cislo bez mezer {tel_cislo_bez_mezer} ")
    if tel_cislo_bez_mezer[0:4] != "+420":
        tel_cislo_bez_mezer = "+420"+ tel_cislo_bez_mezer
        print(f"2 tel cislo bez mezer pridano +420: {tel_cislo_bez_mezer} ")
    if len(tel_cislo_bez_mezer) !=13:
        print(f"1 Vase SMS nebude zaslana na cislo {tel_cislo_bez_mezer} protoze je neplatne-znaky mimo cisla/predvolba mimo 420")
        cislo_platne = False
    for i in range(4,len(tel_cislo_bez_mezer)):
        if tel_cislo_bez_mezer[i] < '0' or tel_cislo_bez_mezer[i] > '9':
            print(f"2 Vase SMS nebude zaslana na cislo {tel_cislo_bez_mezer} protoze je neplatne-znaky mimo cisla/predvolba mimo 420")
            cislo_platne = False
            break
    return cislo_platne


over_tel_cislo(tel_cislo)

sms_zprava = str(input("2 Zadej text SMS/ zpoplatnena 3 Kc za zapocatych 180 slov: "))
def vypocet_ceny_sms(sms_zprava):
    delka_zpravy = int(len(sms_zprava))
    print(f"pri delce zpravy {delka_zpravy} ")
    if delka_zpravy == 0:
        cena_sms = 3
        print(f"cena sms s {len(sms_zprava)} znaky je {cena_sms} ")
    else: 
        cena_sms = int(((delka_zpravy-1)/180)+1)*3
        print(f"cena sms s {len(sms_zprava)} znaky je {cena_sms} ")
    return cena_sms 

vypocet_ceny_sms (sms_zprava)


