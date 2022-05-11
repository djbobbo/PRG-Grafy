from os.path import basename, splitext
import numpy as np
import tkinter as tk 
import matplotlib.pyplot as plt
from math import pi
import random
from tkinter import  CENTER,  E, LEFT, TOP,  N,W, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Grafy"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        #Počáteční hodnoty
        self.t = 0
        self.u = 0

        #Jméno grafu
        self.labelframe = tk.LabelFrame(self , text="Zadej jméno grafu")
        self.labelframe.grid(row=1,column=0, sticky = W)
        
        self.EntryJmeno = tk.Entry (self.labelframe )
        self.EntryJmeno.grid()
        
        #Frekvence
        self.labelframe1 = tk.LabelFrame(self , text="Zadej Frekvenci")
        self.labelframe1.grid(row=2,column=0, sticky = W)
        
        self.EntryFrekvence = tk.Entry (self.labelframe1 )
        self.EntryFrekvence.grid()
        
        #Amplituda
        self.labelframe2 = tk.LabelFrame(self , text="Zadej Amplitudu")
        self.labelframe2.grid(row=3,column=0, sticky = W)
        
        self.EntryAmplituda = tk.Entry (self.labelframe2 )
        self.EntryAmplituda.grid()
        
        #Perioda
        self.labelframe3 = tk.LabelFrame(self , text="Zadej počet period")
        self.labelframe3.grid(row=4,column=0, sticky = W)
        
        self.EntryDoba = tk.Entry (self.labelframe3 )
        self.EntryDoba.grid()
        
        #Posun osy y 
        self.labelframe4 = tk.LabelFrame(self , text="Zadej posun osy y")
        self.labelframe4.grid(row=5,column=0, sticky = W)
        
        self.EntryOffsety = tk.Entry (self.labelframe4 )
        self.EntryOffsety.grid()
        
        #Fázový posun
        self.labelframe5 = tk.LabelFrame(self , text="Zadej fázový posun")
        self.labelframe5.grid(row=6,column=0, sticky = W)
        
        self.EntryPosun = tk.Entry (self.labelframe5 )
        self.EntryPosun.grid()
        
        #Tlacitko
        self.Btn1 = tk.Button(self, text="Vykreslit graf", command=self.vykresleni_grafu )
        self.Btn1.grid(row= 7, column=0)

        #Label na oddeleni tlacitek
        self.LabelVypln = tk.Label(self)
        self.LabelVypln.grid(row= 8, column=0)
       
       
        #Dalsi Tlacitko
        self.Btn2 = tk.Button(self, text="Graf ze souboru ", command=self.Nacteni_ze_souboru )
        self.Btn2.grid(row= 9, column=0)

        #Label na prazdne misto 
        self.LabelVypln = tk.Label(self)
        self.LabelVypln.grid(row= 10, column=0)


        #Získání hodnot z Entry
    
    def zisk_hodnot(self):
        self.jmeno = self.EntryJmeno.get()
        self.doba = self.EntryDoba.get()
        self.frekvence = self.EntryFrekvence.get()
        self.amplituda = self.EntryAmplituda.get()
        self.posun = self.EntryPosun.get()
        self.offsety = self.EntryOffsety.get()

        #Rovnice 
        self.t = np.linspace(0, int(self.doba)*1/int(self.frekvence), int(self.frekvence)*10000)
        self.u = int(self.amplituda) * (np.sin(2*pi*int(self.frekvence)*self.t) + np.deg2rad(int(self.posun))) + int(self.offsety)

       
        #Vykreslení grafu 
    def vykresleni_grafu(self):
        self.zisk_hodnot()
        plt.plot(self.t, self.u)
        plt.xlabel 
        plt.grid()
        
        plt.legend([self.jmeno], loc='upper right')
        plt.show()


        self.osaX = []      # osa X
        self.osaY = []      # osa Y 
    
    
        #Vykreslení grafu hodnot ze souboru 
    def Nacteni_ze_souboru(self):
        f = open("soubor-ux.txt", "r")
        self.osaX = []                            # nacteni
        self.osaY = []
        while 1:
            radek=f.readline()      
            if radek=='':
                break
            cisla=radek.split()
            self.osaX.append( float(cisla[0]))
            self.osaY.append(float(cisla[1]))
    
        plt.plot(self.osaX, self.osaY)            # samotne vykresleni grafu 
        plt.grid()
        plt.show()


app = Application()
app.mainloop()        