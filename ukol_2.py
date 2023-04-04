# https://github.com/JankaMarschalkova/python-jaro-2023/blob/main/ukoly/ukol-02.md
# # Firma eviduje informace o počtu součástek na skladě ve slovníku. 
# Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
# Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit.
# Obě informace si ulož. Následně naprogramuj následující varianty:

# Jaké jsou položky slovníku?
print(f"Nabidka soucastek skladem: {sklad.items()} ") # vypis skladu
#print(sklad.items())
##vypis_skladu = sklad.items()
# Jaké jsou klíče ve slovníku?
# print(sklad.keys())
##kod_soucastky_sklad = sklad.keys()
# Jaké jsou hodnoty ve slovníku?
#print(sklad.values())
##pocet_soucastek_sklad = sklad.values()

kod_soucastky_prodej = input("Zadej kod soucastky: ")
pocet_soucastek_prodej = int(input("Zadej pocet soucastek: "))

if kod_soucastky_prodej not in sklad:
    print(f"Součástka {kod_soucastky_prodej} není skladem.") # existence soucastky ve skladu
else:
    if (sklad[kod_soucastky_prodej] >= pocet_soucastek_prodej): # test poctu soucastek
        print(f"Prodej soucastky {kod_soucastky_prodej} v poctu {pocet_soucastek_prodej}.")
        sklad[kod_soucastky_prodej] = sklad[kod_soucastky_prodej] - pocet_soucastek_prodej
        if sklad[kod_soucastky_prodej] == 0:
            print(f"Zustatek soucastek {kod_soucastky_prodej} v poctu {sklad[kod_soucastky_prodej]}, vyrazujeme z prodeje.")
            sklad.pop(kod_soucastky_prodej)
        else:
            print(f"Na skladu zustava {kod_soucastky_prodej} v poctu {sklad[kod_soucastky_prodej]}.")
    else:
        print(f"Prodej soucastky {kod_soucastky_prodej} lze jen v poctu {sklad[kod_soucastky_prodej]}.")
        chce_koupit = ""
        chce_koupit = (input("Chcee odebrat mensí pocet soucastek? A/N "))
        if (chce_koupit == "A" or chce_koupit == "a"): # potvrzeni koupe mene soucastek
            
            print(f"Prodej soucastky {kod_soucastky_prodej} v jen poctu {sklad[kod_soucastky_prodej]} ktery je na skladu .")
            sklad[kod_soucastky_prodej] = 0
            print(f"Zustatek soucastek {kod_soucastky_prodej} v poctu {sklad[kod_soucastky_prodej]}, vyrazujeme z prodeje.")
            sklad.pop(kod_soucastky_prodej)
                     
        else:
            print(f"Prodej soucastky v mensim poctu zamitnut.")
            print(f"Na skladu zustava {kod_soucastky_prodej} v poctu {sklad[kod_soucastky_prodej]}.")
    
        

# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.

# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. 
# Následně součástku odeber ze slovníku, protože je vyprodaná.

# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.