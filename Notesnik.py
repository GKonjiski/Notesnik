from datetime import datetime
import json


zvezek = {}
try:
    with open("zapiski.json", "r") as f:
        zvezek = json.load(f)
        file_found = True
        
except FileNotFoundError:
    file_found = False
    

st_vnosov = 0

def vnos():
    
    global st_vnosov
    st_vnosov+=1

    zdaj = datetime.now()
    zdaj = zdaj.strftime("%d.%m.%Y %H:%M")
    naslov = input("Naslov: ")
    vsebina = input("Vsebina: ")


    zvezek[naslov]= {"datum": zdaj, "vsebina": vsebina}
    return zvezek

def poglej_ključe():
    for key in zvezek:
        print(f"{key} : {zvezek[key]["datum"]}")

def preberi_zapis():
    ključ = input("Kateri zapisek želiš prebrati?").lower()
    if ključ not in list(zvezek.keys()):
        print("Tega zapiska ni v zvezku.")
    for key in zvezek:
        if key.lower() == ključ:
            print(zvezek[key]["vsebina"])
        

def izbrisi_zapis():
    ključ = input("Kateri zapiske želiš zbrisat? ")
    if ključ not in zvezek.keys():
        print("Tega zapiska ni v zvezku.")
    for key in list(zvezek.keys()):
        if key() == ključ:
            del zvezek[key]
            print(f"Zapisek {key} izbrisan")
        


while True:
    if st_vnosov == 0:
        zvezek = vnos()
    else:
        x = input("Želiš dodati še en vnos (vnos)? Želiš pregledati naslove (naslovi)? Želiš prebrati zapisek (zapisek)? Za izhod vtipkaj izhod  ").lower()
        if x == "vnos":
            zvezek.update(vnos())

        elif x == "naslovi":
            poglej_ključe()

        elif x == "zapisek":
            preberi_zapis()

        elif x == "izbris":
            izbrisi_zapis()

        elif x == "izhod":
            with open("zapiski.json", "w") as f:
                json.dump(zvezek, f)

            break
        else:
            print("Napačen vnos.")






#poglej_ključe()

#print(zvezek.keys())

