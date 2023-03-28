# Napiš program, který bude obsahovat jednu proměnnou jmeno
# Tato proměnná bude obsahovat libovolné křestní jméno
# Program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše
promenna_jmeno = "Alena"
promenna_upravena = (promenna_jmeno.strip()).lower()
domena = "@czechias.cz"
# print(promenna_upravena)
print(f"Vase emailova adresa je {promenna_upravena}{domena}")