from tkinter import *
import json
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
import os
import sys


#zvezek




def get_data_path():
    
   
    base_dir = os.path.join(os.path.expanduser("~"), "Documents", "Notesnik")
    os.makedirs(base_dir, exist_ok=True)  
    return base_dir

direktorij = get_data_path()
direktorij_json = os.path.join(direktorij, "zapiski.json")

print("Shranjujem zapiske v:", direktorij_json)






zvezek = {}

try:
    with open(direktorij_json, "r") as f:
        zvezek = json.load(f)
        file_found = True

except FileNotFoundError:
    file_found = False

print(zvezek)


okno= Tk()

okno.title("NOTESNIK")

try:
    
    ikona = PhotoImage(file="C:\\python\\Notesnik\\fotke\\zvezek.png")
    okno.iconphoto(True, ikona)

except:
    pass


okno.config(background="#35353a")

#okno.geometry("500x500")

taglavn_naslov =Label(okno,
              text="ZAPISKI",
              font=("Bahnschrift", 30),
              fg="black",
              bg="#888fac",
              relief=RAISED,
              bd=4)

if len(zvezek.keys()) <= 1:
    x = 0
else:
    x = 1


taglavn_naslov.grid(row=0, column=x,columnspan=2)


#ZAPISKI
zvezek = {}



try:
    with open(direktorij_json, "r") as f:
        zvezek = json.load(f)
        file_found = True

except FileNotFoundError:
    file_found = False

print(zvezek)




def odpri_zapisek(vsebina,k):
    def izbriši_zapisek(k):
        if k in zvezek:
            del zvezek[k]
            prikaži_zapiske()
            zapisek.destroy()
            sejvej_slovar()
    def shrani_spremenjen_zapisek():
        #naslov_zapisek2=naslov_zapisek1.get()
        vsebina_zapisek2=vsebina_zapisek.get(1.0, END)
        zdaj=datetime.now()
        zdaj = zdaj.strftime("%d.%m.%Y %H:%M")
        zvezek[k]={"datum": zdaj, "vsebina":vsebina_zapisek2}
        prikaži_zapiske()
        zapisek.destroy()
        sejvej_slovar()
    zapisek=Toplevel()
    zapisek.config(background="#35353a")

    naslov_zapisek1=Label(zapisek, text=k,
                        font=("Bahnschrift", 15),
                        fg="black",
                        bg="#888fac",
                        relief=RAISED,
                        bd=4)
    #naslov_zapisek1.insert(0,k)
    naslov_zapisek1.pack(side=TOP,expand=True, fill=BOTH)
    vsebina_zapisek=Text(zapisek,bg="#d8dae6", font=("Times New Roman", 12))
    vsebina_zapisek.insert(1.0,vsebina)
    vsebina_zapisek.pack(side=TOP,expand=True, fill=BOTH)
    odpri_zapisek_shrani_knof=Button(zapisek, text="SHRANI", command=shrani_spremenjen_zapisek,
                                    font=("Bahnschrift", 10),
                                    fg="black",
                                    bg="#888fac",
                                    relief=RAISED,
                                    bd=4)
    odpri_zapisek_shrani_knof.pack(side="left")
    izbriši_zapisek_knof=Button(zapisek,text="IZBRIŠI ZAPISEK", command=lambda: izbriši_zapisek(k),
                                font=("Bahnschrift", 10),
                                fg="black",
                                bg="#888fac",
                                relief=RAISED,
                                bd=4)
    izbriši_zapisek_knof.pack(side="left")
   

 


def prikaži_zapiske():
    grid_collumn=-1
    grid_row=1 
    
    for widget in okno.winfo_children():
        if isinstance(widget, Button):
            widget.destroy()


    for key in list(zvezek.keys()):
        
        grid_collumn+=1

        if grid_collumn>=4:    
            grid_collumn=0
            grid_row+=1
        
        knof=Button(okno,
                    text=key,
                    command=lambda k=key: odpri_zapisek(zvezek[k]["vsebina"], k),
                    width=20,
                    height=10,
                    font=("Bahnschrift", 12),
                    fg="black",
                    bg="#5D5F6D",
                    relief=RAISED,
                    bd=4)
        knof.grid(row=grid_row,column=grid_collumn)
        print("NARDU KNOF")
    nov_zapisek_knof=Button(okno, text="Nov zapiskek", width=20, command=dodaj_zapisek,
                            font=("Bahnschrift", 12),
                            fg="black",
                            bg="#888fac",
                            relief=RAISED,
                            bd=4)
    nov_zapisek_knof.grid(row=grid_row+1, column=0)

    print(okno.winfo_children)


#nov zapisek

def dodaj_zapisek():

    def shrani_nov_zapisek():

        naslov_nov_zapisek2=naslov_nov_zapisek1.get()
        vsebina_nov_zapisek2=nov_zapisek_tekst1.get(1.0, END)

        if naslov_nov_zapisek2 in zvezek:
            messagebox.showerror(title="NAPAKA", message="Ta naslov že obstaja")
            

        else:
            zdaj=datetime.now()
            zdaj = zdaj.strftime("%d.%m.%Y %H:%M")
            zvezek[naslov_nov_zapisek2]={"datum": zdaj, "vsebina":vsebina_nov_zapisek2}
            prikaži_zapiske()
            nov_zapisek.destroy()
            sejvej_slovar()
    nov_zapisek=Toplevel()
    nov_zapisek.config(background="#35353a")
    naslov_nov_zapisek1=Entry(nov_zapisek,
                            font=("Bahnschrift", 15),
                            fg="black",
                            bg="#888fac",
                            relief=RAISED,
                            bd=4)
    naslov_nov_zapisek1.insert(0,"Tu napiši željeni naslov.")
    naslov_nov_zapisek1.pack(side=TOP,expand=True, fill=BOTH)
    nov_zapisek_tekst1=Text(nov_zapisek,bg="#d8dae6",font=("Times New Roman", 12))
    nov_zapisek_tekst1.pack(side=TOP,expand=True, fill=BOTH)

    shrani_knof=Button(nov_zapisek, text="SHRANI", command=shrani_nov_zapisek,
                       font=("Bahnschrift", 10),
                                    fg="black",
                                    bg="#888fac",
                                    relief=RAISED,
                                    bd=4)
    shrani_knof.pack()


def sejvej_slovar():
    with open(direktorij_json, "w") as f:
        json.dump(zvezek,f)



print(os.path.dirname(os.path.abspath(__file__)))





prikaži_zapiske()
okno.mainloop()


#pyinstaller --onefile --windowed --icon="C:\python\Notesnik\ICON.ico" NotesnikGUI.py

