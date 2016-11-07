from tkinter import*
from tkinter import ttk
import threading
import time
import winsound
mc= Tk()
nombres=Toplevel()
dif=Toplevel()
d = Canvas(dif, bg="black", height=685, width=1123)
d.place(x=0,y=0)
##def Play():
##   a = "smb.wav"
##   Reproducir= winsound.PlaySound(a,winsound.SND_FILENAME)
def mostrar(nombres): nombres.deiconify()
def ocultar(mc): mc.withdraw()
def ejecutar(f): mc.after(200,f)
def printn():
        jug1=Label(dif,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=925,y=30)
        mvl=Label(dif,text='Mario VS Luigi',font=("Arcade",40),bg='black',fg='white').place(x=405,y=25)
#Ventana principal
mc.geometry('900x600+220+50')
mc.configure(bg = 'black')
mc.title('Super Mario Proyecto MCL')
mario=PhotoImage(file="mcl2.gif")
fondo=Label(mc,image=mario).place(y=1)
mc.resizable(0,0)
#caracteristicas nombre de jugadores
nombres.geometry('500x300+465+200')
nombres.configure(bg = 'black')
titulop= font.Font(family="Helvetica", size=20, weight="bold")
Label(nombres,text="Mario VS Luigi",bg='black',fg='white', font=titulop).place(x=150,y=20)
seleccionar = Label(nombres,text="Selecciones su nivel de dificultad",bg='black', fg='white',font=16).place(x=130,y=205)
nom1= Label(nombres,text="Nombre primer jugardor",bg='black', fg='white',font=14).place(x=45,y=95)
jug01=StringVar()
txtnom1=Entry(nombres,textvariable=jug01).place(x=70,y=125)#nombre jugadores1
nom2 = Label(nombres,text="Nombre segundo jugador",bg='black', fg='white',font=14).place(x=285,y=95)
jug02=StringVar()
txtnom2=Entry(nombres,textvariable=jug02).place(x=310,y=125)#nombre jugadores2
nombres.title('Nombre de los jugadores')
nombres.resizable(0,0)
##Imagenes
mjug1=PhotoImage(file="mariojug1.gif")
ljug2=PhotoImage(file="luigijug2.gif")
Fondojue=PhotoImage(file="Fondo.gif")
marioder=PhotoImage(file="marioDER.png")
marioiz=PhotoImage(file="mario2iz.png")
marioup=PhotoImage(file="MarioSALT2DER.png")
marioupiz=PhotoImage(file="MarioSAL2iz.png")
luigider=PhotoImage(file="LuigiDER.png")
luigiiz=PhotoImage(file="LuigiIZ.png")
luigiup=PhotoImage(file="LuigiSALTDER.png")
luigiupiz=PhotoImage(file="LuigiSALTIZ.png")
#dificultades carac...
dif.geometry('1123x685+110+8')
dif.title('Juego Super Mario')
picm=Label(dif,image=mjug1,bd=0).place(x=5,y=10)
picl=Label(dif,image=ljug2,bd=0).place(x=1068,y=10)
d.create_image(0,115,image=Fondojue, anchor= NW)
dif.resizable(0,0)
##posicion inical mario
posx=160
posy=560
m=d.create_image(posx,posy,image=marioder, anchor= NW)
##posicion inicial luigi
posxl=910
posyl=560
l=d.create_image(posxl,posyl,image=luigiiz, anchor= NW)
#plataformas
posy1PLAT1=272
posy2PLAT1=298
pabajo1= d.create_rectangle(1,496, 340, 521, fill= None)
pabajo2= d.create_rectangle(779, 496, 1123, 521, fill=None)
pmedio1= d.create_rectangle(1,412, 196, 386, fill=None)
pmedio2= d.create_rectangle(403,412,718,386,fill= None)
pmedio3= d.create_rectangle(923,412,1123,386, fill=None)
parriba1= d.create_rectangle(1,posy1PLAT1, 368, posy2PLAT1, fill= None)
parriba2= d.create_rectangle(749, posy1PLAT1, 1123,posy2PLAT1, fill=None)
#Ocultar ventanas
nombres.withdraw()
dif.withdraw()
#Botones
btn= font.Font(family="Verdana", size=15)
entrada = Button(mc,text="Empezar",cursor="hand2",bg='orange',font= btn,command=lambda: ejecutar(mostrar(nombres)) or (ocultar(mc)),activeforeground="white",bd=10).place(x=410, y=390)#boton ventana principal
nivel1dif = Button(nombres,text="Nivel 1",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif)) or (ocultar(nombres))or printn() ,activeforeground="#F50743").place(x=75,y=250)#boton dificultad 1
nivel2dif = Button(nombres,text="Nivel 2",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=150,y=250)#2
nivel3dif = Button(nombres,text="Nivel 3",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=225,y=250)#3
nivel4dif = Button(nombres,text="Nivel 4",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=300,y=250)#4
nivel5dif = Button(nombres,text="Nivel 5",cursor="pirate",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=375,y=250)#5
#Variables
Estado1='rg'
s=False
def move(event):
        global posx,posy,m,s,Estado1,l,posxl,posyl
        tecla = repr(event.char)
        if (event.char == 'a'):
                d.delete(m)
                posx-=12
                Estado1= 'iz'
                m=d.create_image(posx,posy,image=marioiz, anchor= NW)
                if posx < 0 :
                        posx = 1100        
        if (event.char == 'd'):
                d.delete(m)
                posx+=12
                Estado= 'rg'
                m=d.create_image(posx,posy,image=marioder, anchor= NW)
                if posx > 1123 :
                        posx = 10
        if ((event.char == 'w')and s==False):
                s=True
                saltar()

        if (event.keysym == 'Left'):
                d.delete(l)
                posxl-=12
                l=d.create_image(posxl,posyl,image=luigiiz, anchor= NW)
                if posxl < 0 :
                        posxl = 1100        
        if (event.keysym == 'Right'):
                d.delete(l)
                posxl+=12
                l=d.create_image(posxl,posyl,image=luigider, anchor= NW)
                if posxl > 1123 :
                        posxl = 5

def saltar(y=0):
        global posx,posy,m,s,Estado1
        if(s==True) and (Estado1=='rg'):
                 if(y<=130):
                         posy-=11
                         d.delete(m)
                         m=d.create_image(posx,posy,image=marioup, anchor= NW)
                         d.update()
                         if d.coords(m)>d.coords(pabajo1):
                                 posy=(posy1PLAT1+2)
                                 d.delete(m)
                                 m=d.create_image(posx,posy,image=marioder, anchor= NW)
                        
                 if(y>=130):
                         posy+=11
                         d.delete(m)
                         m=d.create_image(posx,posy,image=marioder, anchor= NW)
                         d.update()
                
                 y+=10
                 print(y)
                 if(y<=260):
                        mc.after(10,saltar(y))
                 else:
                        s=False    
        elif (s==True) or (Estado1=='lf'):
                 if(y<=130):
                         posy-=11
                         d.delete(m)
                         m=d.create_image(posx,posy,image=marioupiz, anchor= NW)
                         d.update()

                 if(y>=130):
                         posy+=11
                         d.delete(m)
                         m=d.create_image(posx,posy,image=marioiz, anchor= NW)
                         d.update()
                 y+=10
                 print(y)
                 if(y<=260):
                        mc.after(10,saltar(y))
                 else:
                        s=False
                        Estado1='rg'
    
d.focus_set()
d.bind_all('<KeyPress>',move)
d.bind('<a>',move)
d.bind('<d>',move)
d.bind('<w>',move)
d.mainloop()
mc.mainloop()

