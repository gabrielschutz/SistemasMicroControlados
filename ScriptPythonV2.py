import tkinter
import tkinter.messagebox
import serial
import time
import customtkinter
from tkinter import *
from tkinter import filedialog

port_opened=False

def set_port():
    global port_opened,arduino
    com_port= entradaPorta.get()
    arduino=serial.Serial('COM4',9600)
    port_opened=True
    print ("PORTA SETADA PARA: "+com_port)

def send_positions(position):
    message = "{0:0=3d}".format(position[0])+"{0:0=3d}".format(position[1])+"{0:0=3d}".format(position[2])+"\n"
    arduino.write(message.encode())
    print(message, end='')
    time.sleep(0.2)

saved_positions = []

def save_positions():
    saved_positions.append([int(servo1_slider.get()), int(servo2_slider.get()), int(servo3_slider.get())]);
    print("Posições Salvas: "+str(saved_positions))

def play_positions():
    for position in saved_positions:
        print("Rodando: "+str(position))
        send_positions(position);
        time.sleep(1)

def clear_all_positions():
    global saved_positions
    saved_positions = []
    print("Limpado todas as Posições")

def clear_last_positions():
    global saved_positions
    removed = saved_positions.pop()
    print("Removido: "+str(removed))
    print("Posições Salvas: "+str(saved_positions))

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

JanelaControl = customtkinter.CTk()
JanelaControl.geometry("500x680")
JanelaControl.title("Controle de Servos V2.0")


margem = customtkinter.CTkFrame(master=JanelaControl)
margem.pack(pady=20, padx=60, fill="both", expand=True)

TituloPrincial = customtkinter.CTkLabel(master=margem,text="Controle Servos V2.0" ,justify=tkinter.LEFT,text_font=("C059",24))
TituloPrincial.pack(pady=12, padx=10)

TextoPorta = customtkinter.CTkLabel(master=margem,text="Porta Arduino" ,justify=tkinter.LEFT)
TextoPorta.pack(pady=1, padx=10)

entradaPorta = customtkinter.CTkEntry(master=margem,placeholder_text="Ex: 'COM4'")
entradaPorta.pack(pady=12,padx=10)

BotaoArduinoSet = customtkinter.CTkButton(master=margem,text="Confirmar" ,command=set_port)
BotaoArduinoSet.pack(pady=12, padx=10)

TextoSlider1 = customtkinter.CTkLabel(master=margem,text="Servo 1" ,justify=tkinter.LEFT)
TextoSlider1.pack(pady=1, padx=10)

servo1_slider = customtkinter.CTkSlider(master=margem,from_=0, to=180, variable=customtkinter.IntVar())
servo1_slider.pack(pady=12, padx=10)

TextoSlider2 = customtkinter.CTkLabel(master=margem,text="Servo 2" ,justify=tkinter.LEFT)
TextoSlider2.pack(pady=1, padx=10)

servo2_slider = customtkinter.CTkSlider(master=margem,from_=0, to=180,variable=tkinter.IntVar())
servo2_slider.pack(pady=12, padx=10)

TextoSlider3 = customtkinter.CTkLabel(master=margem,text="Servo 2" ,justify=tkinter.LEFT)
TextoSlider3.pack(pady=1, padx=10)

servo3_slider = customtkinter.CTkSlider(master=margem,from_=0, to=180,variable=tkinter.IntVar())
servo3_slider.pack(pady=12, padx=10)

BotaoSave = customtkinter.CTkButton(master=margem,text="Salvar Posiçoẽs" ,command=save_positions)
BotaoSave.pack(pady=12, padx=10)

BotaoLimpar = customtkinter.CTkButton(master=margem,text="Limpar Posiçoẽs" ,command=clear_all_positions)
BotaoLimpar.pack(pady=12, padx=10)

BotaoLimparultima = customtkinter.CTkButton(master=margem,text="Limpar Ultima Posição" ,command=clear_last_positions)
BotaoLimparultima.pack(pady=12, padx=10)

BotaoRodar = customtkinter.CTkButton(master=margem,text="Rodar Posiçoẽs" ,command=play_positions)
BotaoRodar.pack(pady=12, padx=10)


JanelaControl.mainloop()
