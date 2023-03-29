import sqlite3
from tkinter import *
import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def formSaisie():
        window = Tk()
        
        l1 = Label (window, text ="identifient")
        l1.pack()
        
        v1 = StringVar()
        v1.set("jeanne")
        e1 = Entry(window,textvariable=v1)
        e1.pack()
        
        l2 = Label (window, text ="mot de passe")
        l2.pack()
        
        v2 = StringVar()
        v2.set("jeanne")
        e2 = Entry(window,textvariable=v2)
        e2.pack()
        
        b1 = Button(window, text="OK", command=lambda:verifId(window,e1.get(),e2.get()))
        b1.pack()
        
        b2 = Button(window, text="cancel", command=window.destroy)
        b2.pack()
        
        window.mainloop()
        
def formBadge(nom):
        windowx = Tk()
        l3 = Label (windowx, text ="passer votre badge")
        l3.pack()
        
        #reader = SimpleMFRC522()
        #try:
        #    id1, text = reader.read()
        #    print(id)
        #    print(text)
        #finally:
        #    GPIO.cleanup()
        id1 = 996305625869
        b3 = Button(windowx, text="OK", command=lambda:verifBadge(id1,nom, windowx))
        b3.pack()
        
def formRecoFacial():
        print("test")
    
def verifBadge(id1, nom, windowx):
        api_root="https://www.btssio-carcouet.fr/ppe4/public/badge/"+nom+"/"+str(id1)
        req = requests.get(api_root)
        wb = req.json()
        print(wb)
        if wb['status'] == "true" :
            print("ok")
            windowx.destroy()
            formRecoFacial()
        else :
            print("error")
def verifId(window,e1,e2):
        api_root="https://www.btssio-carcouet.fr/ppe4/public/connect2/"+e1+"/"+e2+"/infirmiere"
        req = requests.get(api_root)
        wb = req.json()
        print(wb)
        if not ('status' in wb is False):
            print("ok")
            window.destroy()
            formBadge(wb['nom'])
        else :
            print("error")
        
def MaBase(numPhase, identifient, numBadge, commentaire):
        con = sqlite3.connect('kliemie.db')
        c = con.cursor()
        c.execute("insert into logAcces(numPhase,identifiant,numBadge,commentaire) VALUES ("+str(numPhase)+",'"+identifient+"','"+numBadge+"','"+commentaire+"');")
        con.commit()

formSaisie()
