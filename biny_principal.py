#!/usr/bin/python

from tkinter import *
import os
from main_agenda import * 
import sys
import subprocess
import sysconfig
import math
import time
import progressbar


    

def CmdMeuComputador():
    
    subprocess.call('explorer.exe')

def CmdAbreChrome():
    
    subprocess.call('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')




janela_principal = Tk()
janela_principal.wm_title("BINY - Assistent")
janela_principal.geometry("800x600")
janela_principal.resizable(FALSE,FALSE)



logotipo = PhotoImage (file='C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/biny_logo.png')
imgbgbtn = PhotoImage (file='C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/35.png')


Logo = Label(janela_principal, image=logotipo, borderwidth=0, justify=CENTER)
Logo.place(x=0, y=0, relwidth=1, relheight=1)
   
   
btn_MeuComputador = Button(janela_principal, text="Meu Computador", command=CmdMeuComputador)
btn_MeuComputador.config(background="black", fg="white", borderwidth=1, height=2, width=20)
btn_MeuComputador.grid(row=5, column=3, pady=10)

btn_AbreChrome = Button(janela_principal, text="Abre Chrome", command=CmdAbreChrome)
btn_AbreChrome.config(background="black", fg="white", borderwidth=1, height=2, width=20)
btn_AbreChrome.grid(row=6, column=3, pady=10)

btn_AbreCalc = Button(janela_principal, text="Abre Calculadora", command=main_agenda.principal)
btn_AbreCalc.config(background="black", fg="white", borderwidth=1, height=2, width=20)
btn_AbreCalc.grid(row=7, column=3, pady=10)
        
     
janela_principal.mainloop()
   


      

