"""
projekt1.py: Textový analyzátor - prvni projekt do Engeto Online Python Akademie

author: Jaroslav Prudík
email: prudik.j@seznam.cz
discord: Jarek#3498
"""
# import textů z task_template.py
from task_template import TEXTS

oddelovac = "-" * 60

# zadaní úživatelé ve slovníku
uzivatele = {'bob': "123", 'ann': "pass123", 'mike': "password123", 'liz': "pass123"}

# vstupy uživatele
uzivatel = input("Username:")
heslo = input("Password:")
print(oddelovac)

# vybrat jen registrované
if uzivatel in uzivatele.keys() and heslo in uzivatele.get(uzivatel):
    print(f"Welcome to the app {uzivatel}, We have 3 texts to be analyzed.")
else:
    print(f" User: {uzivatel} \n Password: {heslo} \n unregistered user, terminating the program.")
    quit()
print(oddelovac)

# zadat číslo textu a ověřit jestli je v rozsahu 1-3 a je číslo
cislo_textu = input("Enter a number btw. 1 and 3 to select:")
if cislo_textu.isnumeric():
    nove_cislo = int(cislo_textu)
    if nove_cislo in range(1, 4):
        print(oddelovac)
    else:
        print("Selected number is uncorect.")
        quit()
else:
    print("Selected number is uncorect.")
    quit()

# vyčištění vybraného textu od jiných znaků
vycistena_slova = list()
for slovo in TEXTS[int(cislo_textu)-1].split():
    vycistena_slova.append(slovo.strip(",.:;"))

# slova s malými, prvním velkým, velkými písmeny a čísla
slova_malymi = []
slova_1velke = []
slova_velkymi = []
cisla = []
for slovo in vycistena_slova:
    if slovo.islower():
        slova_malymi.append(slovo)
    elif slovo.istitle():
        slova_1velke.append(slovo)
    elif slovo.isupper():
        slova_velkymi.append(slovo)
    elif slovo.isnumeric():
        cisla.append(int(slovo))

# vytištění požadovaných statistik
print(f"There are {len(vycistena_slova)} words in the selected text")
print(f"There are {len(slova_1velke)} titlecase words in the selected text")
print(f"There are {len(slova_velkymi)} uppercase words in the selected text")
print(f"There are {len(slova_malymi)} lowercase words in the selected text")
print(f"There are {len(cisla)} numeric strings in the selected text")
print(f"The sum of all tne numpers {sum(cisla)}")
print(oddelovac)

# první řádek (hlavička) grafu (tabulky)
lenx = "LEN"
occurences = "     OCCURENCES     "
nr = "NR."
print(lenx, "|", occurences, "|", nr)
print(oddelovac)

# graf - seznam - počet písmen ve slovech. Seřazeno vzestupně
pocet_pismen = []
for slovo in vycistena_slova:
    slovo = len(slovo)
    pocet_pismen.append(slovo)
    pocet_pismen.sort()

# graf - slovník - četnost slov se stejným počtem písmen
cetnost_slov = {}
for slovo in pocet_pismen:
    if slovo not in cetnost_slov:
        cetnost_slov[slovo] = 1
    else:
        cetnost_slov[slovo] = cetnost_slov[slovo] + 1

# seznam z hodnot slovníku cetnost_slov
hodnoty_cetnost_slov = list(cetnost_slov.values())
for index, symbol in enumerate(hodnoty_cetnost_slov):
    hvezdicka = "*" * int(symbol)
    # výpis zformátované tabulky
    print(f"{str(index + 1).rjust(len(lenx))} | {hvezdicka.ljust(len(occurences))} | {str(symbol).ljust(len(nr))}")
