#Prueba 1
from tkinter import*
from tkinter import ttk
from tkinter import font
import threading
import time
import winsound
mc= Tk()
nombres=Toplevel()
dif=Toplevel()
d = Canvas(dif, bg="black", height=685, width=1123)
d.place(x=0,y=0)
##def Play():
##    Reproducir= winsound.PlaySound("smb.wav",winsound.SND_ASYNC)
def mostrar(nombres): nombres.deiconify()
def ocultar(mc): mc.withdraw()
def ejecutar(f): mc.after(200,f)
def printn():
        jug1=Label(dif,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=925,y=30)
        mvl=Label(dif,text='Mario and Luigi',font=("Arcade",40),bg='black',fg='white').place(x=380,y=25)
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
Label(nombres,text="Mario and Luigi",bg='black',fg='white', font=titulop).place(x=145,y=20)
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
##Tortuga
#dificultades carac...
dif.geometry('1123x685+110+8')
dif.title('Juego Super Mario')
picm=Label(dif,image=mjug1,bd=0).place(x=5,y=10)
picl=Label(dif,image=ljug2,bd=0).place(x=1068,y=10)
d.create_image(0,115,image=Fondojue, anchor= NW)
dif.resizable(0,0)
##posicion inical mario
m=d.create_image(160,560,image=marioder, anchor= NW)
##posicion inical luigi
l=d.create_image(910,560,image=luigiiz, anchor= NW)
#plataformas
pabajo1= d.create_rectangle(1,496, 340, 521, fill=None)
pabajo2= d.create_rectangle(779, 496, 1123, 521, fill=None)
pmedio1= d.create_rectangle(1,412, 196, 386, fill=None)
pmedio2= d.create_rectangle(403,412,718,386,fill= None)
pmedio3= d.create_rectangle(923,412,1123,386, fill=None)
parriba1= d.create_rectangle(1,272, 368, 298, fill= None)
parriba2= d.create_rectangle(749, 272, 1123,298, fill=None)
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
estado2='iz'
sl=False
def caer():
        global m,s,a,Estado1
        if Estado1 == 'rg':
           while (a<=81):
                 x=int(d.coords(m)[0])
                 y=int(d.coords(m)[1])
                 d.move(m,0,5)
                 d.update()
                 if y+5==560:
                         break
                 if y+5==430:
                         break
                 if y+5==320:
                         break
                 mc.after(5)               
                 a+=3
        a=0
        if Estado1 == 'lf':
           while (a<=81):
                 x=int(d.coords(m)[0])
                 y=int(d.coords(m)[1])
                 d.move(m,0,5)
                 d.update()
                 if y+5==560:
                         break
                 if y+5==430:
                         break
                 if y+5==320:
                         break
                 mc.after(5)               
                 a+=3
        a=-1
        
def move(event):
        global m,Estado1
        tecla = repr(event.char)
        if (tecla == "'a'" or tecla=="'A'"):
                x=int(d.coords(m)[0])
                y=int(d.coords(m)[1])
                d.delete(m)
                Estado1= 'lf'
                m=d.create_image(x,y,image=marioiz, anchor=NW)
                d.move(m,-12,0)
                if d.coords(m)[0] < 0 :
                        d.coords(m,1120,y)
                elif y==430 and(x+2>=340 and x+2<=765):
                        caer()
                elif (y==320 and (x+2 >= 195 and x+2 <= 405)):
                        caer()
                elif (y==320 and (x+2 >= 923 and x+2 <= 925)):
                        caer()
                elif y==205 and (x+2 >= 368 and x+2 <=749):
                        caer()

        if (tecla == "'d'" or tecla== "'D'"):
                x=int(d.coords(m)[0])
                y=int(d.coords(m)[1])
                d.delete(m)
                Estado1= 'rg'
                m=d.create_image(x,y,image=marioder, anchor=NW)
                d.move(m,12,0)
                if d.coords(m)[0] > 1128 :
                        d.coords(m,2,y)
                elif y==430 and(x+2>=340 and x+2<=765):
                        caer()
                elif y==315 and (x+2>= 195 and x+2<= 405):
                        caer()
                elif y==315 and (x+2 >= 720 and x+2 <= 925):
                        caer()
                elif y==205 and (x+2 >= 368 and x+2 <=749):
                        caer()

        if ((tecla == "'w'" or tecla== "'W'")and a==-1):
                saltar()

a=-1
def movel(event):
        global l,sl,estado2
        if (event.keysym == 'Left'):
                x=int(d.coords(l)[0])
                y=int(d.coords(l)[1])
                d.delete(l)
                estado2= 'rg'
                l=d.create_image(x,y,image=luigiiz, anchor=NW)
                d.move(l,-12,0)
                if d.coords(l)[0] < 0 :
                        d.coords(l,1120,y)
                       
        if (event.keysym == 'Right'):
                x=int(d.coords(l)[0])
                y=int(d.coords(l)[1])
                d.delete(l)
                estado2= 'iz'
                l=d.create_image(x,y,image=luigider, anchor=NW)
                d.move(l,12,0)
                if d.coords(l)[0] > 1120 :
                        d.coords(l,2,y)
        if (event.keysym == 'Up'):
                saltarl()
a=-1
def saltar():
        global m,s,Estado1,a
        if Estado1=='rg':
                 a=0
                 while a<=81:
                        x=int(d.coords(m)[0])
                        y=int(d.coords(m)[1])
                        d.delete(m)
                        m=d.create_image(x,y,image=marioup, anchor=NW)
                        d.move(m,2,-5)
                        d.update()
                        mc.after(5)
                        a+=3
                        if y-5==520 and not (x+2>=340 and x+2<=765):
                              break
                        elif y-5==395 and (x+2 >= 1 and x+2 <= 196):
                                break
                        elif y-5==395 and (x+2 >= 405 and x+2 <= 725):
                                break
                        elif y-5==395 and (x+2 >= 915 and x+2 <= 1123):
                                break
                        elif y-5 ==300 and ((x+2 >= 1 and x+2 <=398)):
                                 break
                        elif y-5 ==300 and (x+2 >=749 and x+2 <= 1123):
                                 break
                        
                 a=0
                 while (a<=81):
                         x=int(d.coords(m)[0])
                         y=int(d.coords(m)[1])
                         d.delete(m)
                         m=d.create_image(x,y,image=marioup, anchor=NW)
                         d.move(m,2,5)
                         d.update()
                         mc.after(5)               
                         a+=3
                         if  y+5==560 or y+5==430 and not (x+2>=340 and x+2<=765) :
                                 break
                         elif y+5==320 and (x+2 >= 1 and x+2 <= 196):
                                break
                         elif y+5==320 and (x+2 >= 405 and x+2 <= 725):
                                break
                         elif y+5==320 and (x+2 >= 915 and x+2 <= 1123):
                                break
                         elif y+5 ==205 and (x+2 >= 1 and x+2 <=398):
                                 break
                         elif y+5 ==205 and (x+2 >=749 and x+2 <= 1123):
                                 break
                 x=int(d.coords(m)[0])
                 y=int(d.coords(m)[1])
                 d.delete(m)
                 m=d.create_image(x,y,image=marioder, anchor=NW)
                 
        elif Estado1=='lf':
                a=0
                while a<=81:
                        x=int(d.coords(m)[0])
                        y=int(d.coords(m)[1])
                        d.delete(m)
                        m=d.create_image(x,y,image=marioupiz, anchor=NW)
                        d.move(m,-2,-5)
                        d.update()
                        mc.after(5)
                        a+=3
                        if y-5==520 and not(x+2>=340 and x+2<=765):
                                break
                        elif y-5==395 and (x+2 >= 1 and x+2 <= 196):
                                break
                        elif y-5==395 and (x+2 >= 405 and x+2 <= 725):
                                break
                        elif y-5==395 and (x+2 >= 915 and x+2 <= 1123):
                                break
                        elif y-5 ==300 and (x+2 >= 1 and x+2 <=398):
                                 break
                        elif y-5 ==300 and (x+2 >=749 and x+2 <= 1123):
                                 break

                a=0
                while (a<=81):
                         x=int(d.coords(m)[0])
                         y=int(d.coords(m)[1])
                         d.delete(m)
                         m=d.create_image(x,y,image=marioupiz, anchor=NW)
                         d.move(m,-2,5)
                         d.update()
                         mc.after(5)               
                         a+=3
                         if  y+5==560 or y+5==430 and not (x+2>=340 and x+2<=765):
                                 break
                         elif y+5==320 and (x+2 >= 1 and x+2 <= 196):
                                break
                         elif y+5==320 and (x+2 >= 405 and x+2 <= 725):
                                break
                         elif y+5==320 and (x+2 >= 915 and x+2 <= 1123):
                                break
                         elif y+5 ==205 and (x+2 >= 1 and x+2 <=398):
                                 break
                         elif y+5 ==205 and (x+2 >=749 and x+2 <= 1123):
                                 break
                x=int(d.coords(m)[0])
                y=int(d.coords(m)[1])
                d.delete(m)
                m=d.create_image(x,y,image=marioiz, anchor=NW)
        a=-1
                 
        ##luigi
##def saltarl(x=0):
##        global cpla,cl,estado2,sl,l,posxl,posyl
##        if(sl==True) and (estado2=='rg'):
##                 if(x<=130):
##                         posyl-=10
##                         d.delete(l)
##                         l=d.create_image(posxl,posyl,image=luigiup, anchor= NW)
##                         d.update()
##                                                    
##                 if(x>=130):
##                         posyl+=10
##                         d.delete(l)
##                         l=d.create_image(posxl,posyl,image=luigider, anchor= NW)
##                         d.update()
##                
##                 x+=15
##                 print(x)
##                 if(x<=260):
##                        mc.after(20,saltarl(x))
##                 else:
##                        sl=False
##
##        elif (sl==True) or (estado2=='lf'):
##                 if(x<=130):
##                         posyl-=10
##                         d.delete(l)
##                         l=d.create_image(posxl,posyl,image=luigiupiz, anchor= NW)
##                         d.update()
##
##                 if(x>=130):
##                         posyl+=10
##                         d.delete(l)
##                         l=d.create_image(posxl,posyl,image=luigiiz, anchor= NW)
##                         d.update()
##                 x+=15
##                 print(x)
##                 if(x<=260):
##                        mc.after(20,saltarl(x))
##                 else:
##                        sl=False
##                        estado2='rg'

                        
    
d.focus_set()
d.bind_all('<KeyPress>',movel)
d.bind("<Key>",move)
d.mainloop()
mc.mainloop()

