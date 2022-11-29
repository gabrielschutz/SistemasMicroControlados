from tkinter import *
from tkinter import filedialog
import serial
import time

port_opened=False

def set_port():
    global port_opened,arduino
    com_port= port_input.get()
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
    saved_positions.append([servo1_slider.get(), servo2_slider.get(), servo3_slider.get()]);
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

def open_file():
    global saved_positions
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file = open(filename, "r")
    data=file.read()
    saved_positions=eval(data)
    file.close()
    print("Aberto: "+filename)

def save_file():
    save_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    save_file.write(str(saved_positions))
    save_file.close()
    print("Arquivo Gravado")

window = Tk()
window.title("Controle de Servos 1.0")
window.minsize(380,300)
window.grid()

port_label=Label(window,text="Porta Arduino:");
port_label.place(x=120,y=10);
port_input=Entry(window)
port_input.place(x=120,y=35)
port_button=Button(window, text="Enter", command=set_port)
port_button.place(x=250,y=32)

servo1_slider = Scale(window, from_=180, to=0)
servo1_slider.place(x=70, y=100)
servo1_label=Label(window,text="Motor 1")
servo1_label.place(x=70, y=80)

servo2_slider = Scale(window, from_=180, to=0)
servo2_slider.place(x=140, y=100)
servo2_label=Label(window,text="Motor 2")
servo2_label.place(x=140, y=80)

servo3_slider = Scale(window, from_=180, to=0)
servo3_slider.place(x=210, y=100)
servo3_label=Label(window,text="Motor 3")
servo3_label.place(x=210, y=80)


save_button=Button(window, text="Salvar Posições", command=save_positions)
save_button.place(x=10,y=220)

clear_button=Button(window, text="Limpar ultima posição", command=clear_last_positions)
clear_button.place(x=120,y=220)

clear_button=Button(window, text="Limpar todas Posições", command=clear_all_positions)
clear_button.place(x=120,y=255)

play_button=Button(window, text="Rodar Posições", command=play_positions, height=3)
play_button.place(x=270,y=220)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Abrir", command=open_file)
filemenu.add_command(label="Salvar", command=save_file)
menubar.add_cascade(label="Arquivo", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Limpar ultima Posição", command=clear_last_positions)
editmenu.add_command(label="Limpar todas Posições", command=clear_all_positions)
menubar.add_cascade(label="Editar", menu=editmenu)


window.config(menu=menubar)

while True:
    window.update()
    if(port_opened):
        send_positions([servo1_slider.get(), servo2_slider.get(), servo3_slider.get()])
