from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 

#Criação da tela
jan = Tk() 
jan.title("Tela de login e cadastro") 
jan.geometry("1550x900") 
jan.configure(background = "#f6f3ec") 
jan.resizable(width = False, height = False) 

RegisterButton = ttk.Button(text = "Produtos", width = 40) 
RegisterButton.place(x = 100, y = 35) 

jan.mainloop()