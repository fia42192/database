import sys
import time


animals_list = ["Lev", "Tučňák", "Krokodýl", "Žralok"]
animals_dict = {
    "Lev":{
        "Třída": "savec",
        "Řád": "šelmy",
        "Rod": "Panthera"
    },

    "Tučňák":{
        "Třída": "ptáci",
        "Řád": "tučňáci",
        "Rod": "tučňák"
    },

    "Krokodýl":{
        "Třída": "plazi",
        "Řád": "krokodýli",
        "Rod": "krokodýl"
    },

    "Žralok":{
        "Třída": "paryby",
        "Řád": "obrouni",
        "Rod": "žralok"
    }
}
while True:
    otazka = int(input("Co chceš zvolit? (Napiš číslo)\n1. Vyhledat zvíře a zobrazit informace\n2. Přidat zvíře a jeho informace k tomu\n:"))
    #Volba výpisu detailů jednotlivých zvířat
    if otazka == 1:
        print("\nMůžeš si vybrat z následujicích zvířat:")
        print(*animals_list, sep=', ')
        zvire = str(input("\nZvol jedno z výše uvedených zvířat: "))
        if zvire in animals_list:
            zvire_detaily = animals_dict[zvire]
            print("Zde máš informace o daném zvířeti: ")
            time.sleep(0.5)
            for key, value in zvire_detaily.items():
                print(f"{key}: {value}")
            pokracovani_1 = str(input("Přeješ si pokračovat? (Ano/Ne) "))
            if pokracovani_1 == "Ano":
                continue
            else:
                sys.exit()
        else:
            print("Takové zvíře není na seznamu.")
            sys.exit()
    #Přidání zvířete s detaily
    elif otazka == 2:
        nazev_zvirete = str(input("Napiš název zvířete: "))
        animals_list.append(nazev_zvirete)
        nove_zvire_detaily = {}
        nove_zvire_detaily["Třída"] = str(input("Napiš Třídu: "))
        nove_zvire_detaily["Řád"] = str(input("Napiš řád: "))
        nove_zvire_detaily["Rod"] = str(input("Napiš Rod: "))
        animals_dict[nazev_zvirete] = nove_zvire_detaily
        print(f"Zvíře {nazev_zvirete} bylo úspěšně přidáno.")

        pokracovani = str(input("Přeješ si pokračovat? (Ano/Ne) "))
        if pokracovani == "Ano":
            continue
        else:
            sys.exit()
    



