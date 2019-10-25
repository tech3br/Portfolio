import os
from tkinter import *
from tkinter.ttk import *
import sys
from tkinter import ttk



#processo principal da janela de inicio
def principal():
            
    #definindo a janela
    janela = Tk()
    janela.title("Drin Agenda")
    janela.geometry("357x250")
    janela.resizable(FALSE,FALSE)
    janela.configure(background="#C5E5F2")
                        
    #definindo icone da janela    
    janela.iconbitmap("C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/agenda_12_px.ico")

    #definindo logo    
    logotipo = PhotoImage (file='C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/facebook_cover_photo_1.png')
                    
    Logo = Label(image=logotipo, borderwidth=0)
    Logo.grid(row=1, columns=10, pady=20)
                    
                
    #botão criar contatos
    btn_criar_contato_imagem = PhotoImage(file = "C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/add_contato_12_px.png")
    btn_criar_contato = Button(janela, text="Adicionar Contatos", command=CriarContato, image=btn_criar_contato_imagem, compound = LEFT)
    btn_criar_contato.grid(row=2, column=2, sticky=S, pady=20)
                        

    #botão listar contatos  
    btn_listar_listar_contato_img = PhotoImage(file = "C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/connections.png")
    btn_listar_contato2 = Button(janela, text="Listar Contatos", command=ListaContato, image=btn_listar_listar_contato_img, compound = LEFT)
    btn_listar_contato2.grid(row=2, column=4, sticky=S, pady=20)
                    
                        
    #botão excluir contatos
    btn_excluir_contato_img = PhotoImage(file = "C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/eraser.png")
    btn_excluir_contato = Button(janela, text="Excluir Contatos", command=ExcluirContato, image=btn_excluir_contato_img, compound = LEFT)
    btn_excluir_contato.grid(row=2, column=6, sticky=S, pady=20)

    #botão sair de tudo
    btn_sair = Button(janela, text="Sair", command=FecharTudo)
    btn_sair.grid(row=3, column=6, sticky=E)

    janela.mainloop()

def CriarContato():

    TelaCriarContato = Tk()
    TelaCriarContato.title("Criar Contato")
    TelaCriarContato.geometry("357x250")

    TelaCriarContato.resizable(FALSE, FALSE) 
    #define o favicon da janela 
    TelaCriarContato.iconbitmap("C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/add_contato_12_px.ico")
                            
    #cria  a label dos campos
    Label(TelaCriarContato, text="Nome:").grid(row=3, column=3, sticky=E, padx=10)
    TelaCriarContato.e1 = Entry(TelaCriarContato)
    TelaCriarContato.e1.grid(row=3, column=5, sticky=E, pady=10)


    Label(TelaCriarContato, text="Telefone:").grid(row=7, column=3, sticky=E, padx=10)
    TelaCriarContato.e2 = Entry(TelaCriarContato)
    TelaCriarContato.e2.grid(row=7, column=5, sticky=E, pady=10)
                            
                            
    Label(TelaCriarContato, text="Email:").grid(row=9, column=3, sticky=E, padx=10)
    TelaCriarContato.e3 = Entry(TelaCriarContato)
    TelaCriarContato.e3.grid(row=9, column=5, sticky=E, pady=10)

    TelaCriarContato.cb = Checkbutton(TelaCriarContato, text="Adicionar à lista de favoritos")
    TelaCriarContato.cb.grid(row=11, column=5, sticky=E, pady=10)

    #faz a janela ficar no loop 
    TelaCriarContato.mainloop(1)
                    
def ListaContato():
                        
    TelaListarContatos = Tk()
    TelaListarContatos.title("Lista de Contatos")
    TelaListarContatos.geometry("400x200")
    TelaListarContatos.resizable(FALSE, FALSE)
    #define o favicon da janela
    TelaListarContatos.iconbitmap("C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/connections_12_px.ico")
    #faz a janela ficar no loop
    TelaListarContatos.mainloop()
                        
def ExcluirContato(): 
                        
    TelaExcluirContatos = Tk()
    TelaExcluirContatos.title("Excluir Contatos")
    TelaExcluirContatos.geometry("400x200")
    TelaExcluirContatos.resizable(FALSE, FALSE)
    #define o favicon da janela
    TelaExcluirContatos.iconbitmap("C:/Users/FIGGZ/Desktop/Programação/Drin_Agenda/img/eraser_12_px.ico")
    #faz a janela ficar no loop
    TelaExcluirContatos.mainloop()

def deucerto():
                
    print("deu certo")

def FecharTudo():
    os._exit(1)    

principal()
