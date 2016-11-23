from tkinter import*
from tkinter import font
import time
import winsound
mc= Tk()
nombres=Toplevel()
dif=Toplevel()
d = Canvas(dif, bg="black", height=685, width=1123)
d.place(x=0,y=0)
global puntuacionm,puntuacion
def Play():
    Reproducir= winsound.PlaySound("smb.wav",winsound.SND_ASYNC)
def mostrar(nombres): nombres.deiconify()
def ocultar(mc): mc.withdraw()
def ejecutar(time,f): mc.after(time,f)
#Ventana principal
mc.geometry('900x600+220+50')
mc.configure(bg = 'black')
mc.title('Super Mario Proyecto MCL')
mario=PhotoImage(file="mcl2.gif")
fondo=Label(mc,image=mario).place(y=1)
mc.resizable(0,0)
##puntuaciones
puntuacion=0
puntuacionm=0
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
turder=PhotoImage(file="TurL1.png")
turiz=PhotoImage(file="TurL1iz.png")
turvol=PhotoImage(file="Tvol.png")
##turdead=PhotoImage(file="VOLT.png")
turder2=PhotoImage(file="TurL3.png")
turiz2=PhotoImage(file="TurL3iz.png")
##turdead2=PhotoImage(file="VOLT3.png")
turder3=PhotoImage(file="TurL5.png")
turiz3=PhotoImage(file="TurL5iz.png")
##turdead3=PhotoImage(file="VOLTM.png")
##tubo
tubo=PhotoImage(file="tubo.png")
tubo2=PhotoImage(file="tubo2.png")
#dificultades carac...
dif.geometry('1123x685+110+8')
dif.title('Juego Super Mario')
picm=Label(dif,image=mjug1,bd=0).place(x=5,y=10)
picl=Label(dif,image=ljug2,bd=0).place(x=1068,y=10)
tu=d.create_image(1,115,image=tubo, anchor=NW)
tu2=d.create_image(886,115,image=tubo2, anchor=NW)
d.create_image(0,115,image=Fondojue, anchor= NW)
dif.resizable(0,0)
##posicion inical mario
m=d.create_image(160,560,image=marioder, anchor= NW)
##posicion inical luigi
l=d.create_image(910,560,image=luigiiz, anchor= NW)
##posicion inicial tortuga
tor=d.create_image(195,140,image=turder, anchor=NW)
tor1=d.create_image(890,140,image=turiz, anchor=NW)
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
entrada = Button(mc,text="Empezar",cursor="hand2",bg='orange',font= btn,command=lambda: mostrar(nombres) or (ocultar(mc)),activeforeground="white",bd=10).place(x=410, y=390)#boton ventana principal
#Variables
Estado1='rg'
estado2='iz'
def caer():
        global m,a,Estado1
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
        
def move():
        global m,Estado1,Mov,tor,tor1
        if (Mov["a"]==True):
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
                elif (y==320 and (x+2 >= 720 and x+2 <= 925)):
                        caer()
                elif y==205 and (x+2 >= 368 and x+2 <=749):
                        caer()
                if (d.coords(tor))==(x and y):
                    d.delete(m)
                elif (d.coords(tor1))==(x and y):
                    d.delete(m)

        if (Mov["d"]==True):
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
                elif y==320 and (x+2>= 195 and x+2<= 405):
                        caer()
                elif y==320 and (x+2 >= 720 and x+2 <= 925):
                        caer()
                elif y==205 and (x+2 >= 368 and x+2 <=749):
                        caer()
                if (d.coords(tor))==(x and y):
                    d.delete(m)
                elif (d.coords(tor1))==(x and y):
                    d.delete(m)

        if ((Mov["w"]==True)and a==-1):
                saltar()
        d.after(100,move)

a=-1
def saltar():
        global m,Estado1,a
        if Estado1=='rg':
                 a=0
                 while a<=81:
                        x=int(d.coords(m)[0])
                        y=int(d.coords(m)[1])
                        d.delete(m)
                        m=d.create_image(x,y,image=marioup, anchor=NW)
                        d.move(m,2,-5)
                        d.update()
                        mc.after(1)
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
                         mc.after(1)               
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
                        mc.after(1)
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
                         mc.after(1)               
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
###########MOVIMIENTO LUIGI############
def movel():
        global l,estado2,Mov,tor,tor1
        if (Mov['Left']==True):
                xl=int(d.coords(l)[0])
                yl=int(d.coords(l)[1])
                d.delete(l)
                estado2= 'iz'
                l=d.create_image(xl,yl,image=luigiiz, anchor=NW)
                d.move(l,-12,0)
                if d.coords(l)[0] < 0 :
                        d.coords(l,1120,yl)
                elif yl==430 and(xl+2>=340 and xl+2<=765):
                        caerl()
                elif (yl==320 and (xl+2 >= 195 and xl+2 <= 405)):
                        caerl()
                elif (yl==320 and (xl+2 >= 720 and xl+2 <= 925)):
                        caerl()
                elif yl==205 and (xl+2 >= 368 and xl+2 <=749):
                        caerl()
                if (d.coords(tor))==(xl and yl):
                    d.delete(l)
                elif (d.coords(tor1))==(xl and yl):
                    d.delete(l)
        if (Mov['Right']==True):
                xl=int(d.coords(l)[0])
                yl=int(d.coords(l)[1])
                d.delete(l)
                estado2= 'rg'
                l=d.create_image(xl,yl,image=luigider, anchor=NW)
                d.move(l,12,0)
                if d.coords(l)[0] > 1120 :
                        d.coords(l,2,yl)
                elif yl==430 and(xl+2>=340 and xl+2<=765):
                        caerl()
                elif (yl==320 and (xl+2 >= 195 and xl+2 <= 405)):
                        caerl()
                elif (yl==320 and (xl+2 >= 720 and xl+2 <= 925)):
                        caerl()
                elif yl==205 and (xl+2 >= 368 and xl+2 <=749):
                        caerl()
                if (d.coords(tor))==(xl and yl):
                    d.delete(l)
                elif (d.coords(tor1))==(xl and yl):
                    d.delete(l)
        if (Mov['Up']==True) and al==-1:
                saltarl()
        d.after(100,movel)
al=-1
def saltarl():
        global l,estado2,al
        if estado2=='rg':
                 al=0
                 while al<=81:
                        xl=int(d.coords(l)[0])
                        yl=int(d.coords(l)[1])
                        d.delete(l)
                        l=d.create_image(xl,yl,image=luigiup, anchor=NW)
                        d.move(l,2,-5)
                        d.update()
                        mc.after(1)
                        al+=3
                        if yl-5==520 and not (xl+2>=340 and xl+2<=765):
                              break
                        elif yl-5==395 and (xl+2 >= 1 and xl+2 <= 196):
                                break
                        elif yl-5==395 and (xl+2 >= 405 and xl+2 <= 725):
                                break
                        elif yl-5==395 and (xl+2 >= 915 and xl+2 <= 1123):
                                break
                        elif yl-5 ==300 and ((xl+2 >= 1 and xl+2 <=398)):
                                 break
                        elif yl-5 ==300 and (xl+2 >=749 and xl+2 <= 1123):
                                 break
                        
                 al=0
                 while (al<=81):
                         xl=int(d.coords(l)[0])
                         yl=int(d.coords(l)[1])
                         d.delete(l)
                         l=d.create_image(xl,yl,image=luigiup, anchor=NW)
                         d.move(l,2,5)
                         d.update()
                         mc.after(1)               
                         al+=3
                         if  yl+5==560 or yl+5==430 and not (xl+2>=340 and xl+2<=765) :
                                 break
                         elif yl+5==320 and (xl+2 >= 1 and xl+2 <= 196):
                                break
                         elif yl+5==320 and (xl+2 >= 405 and xl+2 <= 725):
                                break
                         elif yl+5==320 and (xl+2 >= 915 and xl+2 <= 1123):
                                break
                         elif yl+5 ==205 and (xl+2 >= 1 and xl+2 <=398):
                                 break
                         elif yl+5 ==205 and (xl+2 >=749 and xl+2 <= 1123):
                                 break
                 xl=int(d.coords(l)[0])
                 yl=int(d.coords(l)[1])
                 d.delete(l)
                 l=d.create_image(xl,yl,image=luigider, anchor=NW)
                 
        elif estado2=='iz':
                al=0
                while al<=81:
                        xl=int(d.coords(l)[0])
                        yl=int(d.coords(l)[1])
                        d.delete(l)
                        l=d.create_image(xl,yl,image=luigiupiz, anchor=NW)
                        d.move(l,-2,-5)
                        d.update()
                        mc.after(1)
                        al+=3
                        if yl-5==520 and not(xl+2>=340 and xl+2<=765):
                                break
                        elif yl-5==395 and (xl+2 >= 1 and xl+2 <= 196):
                                break
                        elif yl-5==395 and (xl+2 >= 405 and xl+2 <= 725):
                                break
                        elif yl-5==395 and (xl+2 >= 915 and xl+2 <= 1123):
                                break
                        elif yl-5 ==300 and (xl+2 >= 1 and xl+2 <=398):
                                 break
                        elif yl-5 ==300 and (xl+2 >=749 and xl+2 <= 1123):
                                 break

                al=0
                while (al<=81):
                         xl=int(d.coords(l)[0])
                         yl=int(d.coords(l)[1])
                         d.delete(l)
                         l=d.create_image(xl,yl,image=luigiupiz, anchor=NW)
                         d.move(l,-2,5)
                         d.update()
                         mc.after(1)               
                         al+=3
                         if  yl+5==560 or yl+5==430 and not (xl+2>=340 and xl+2<=765):
                                 break
                         elif yl+5==320 and (xl+2 >= 1 and xl+2 <= 196):
                                break
                         elif yl+5==320 and (xl+2 >= 405 and xl+2 <= 725):
                                break
                         elif yl+5==320 and (xl+2 >= 915 and xl+2 <= 1123):
                                break
                         elif yl+5 ==205 and (xl+2 >= 1 and xl+2 <=398):                                                                                                
                                 break
                         elif yl+5 ==205 and (xl+2 >=749 and xl+2 <= 1123):
                                 break
                xl=int(d.coords(l)[0])
                yl=int(d.coords(l)[1])
                d.delete(l)
                l=d.create_image(xl,yl,image=luigiiz, anchor=NW)
        al=-1
def caerl():
        global l,al,estado2
        if estado2 == 'rg':
           while (al<=81):
                 xl=int(d.coords(l)[0])
                 yl=int(d.coords(l)[1])
                 d.move(l,0,5)
                 d.update()
                 if yl+5==560:
                         break
                 if yl+5==430:
                         break
                 if yl+5==320:
                         break
                 mc.after(5)               
                 al+=3
        al=0
        if estado2 == 'iz':
           while (al<=81):
                 xl=int(d.coords(l)[0])
                 yl=int(d.coords(l)[1])
                 d.move(l,0,5)
                 d.update()
                 if yl+5==560:
                         break
                 if yl+5==440:
                         break
                 if yl+5==320:
                         break
                 mc.after(5)               
                 al+=3
        al=-1
##########MOVIMIENTO TORTUGA###############
def turtle(tur,v1):
        global tor,v,tur1
        v=v1
        tur1=tur
        d.delete(tor)
        tor=d.create_image(170,140,image=tur, anchor=NW)
        turtleM()
def turtleM():
        global tor,v,tdiriz,m,puntuacion,tur1,l,puntuacionm
        xt=int(d.coords(tor)[0])
        yt=int(d.coords(tor)[1])
        y=int(d.coords(m)[1])
        yl=int(d.coords(l)[1])
        who=[y,yl]
        d.move(tor,v,0)
        if xt < 0 :
                        d.coords(tor,1122,yt)
        if xt > 1122 :
                        d.coords(tor,2,yt)
        if xt > 1120 and yt>=560:
            d.delete(tor)
            tor=d.create_image(170,140,image=tur1, anchor=NW)
        if (xt==210 or xt==198 or xt==188 or xt==850 or xt==858 or xt==849) and yt==140:
                         caert()
        if yt==215 and (xt>= 368 and xt<=749):
                        caert()
        if yt==435 and(xt>=340 and xt<=700):
                        caert()
        if yt==325 and (xt>= 195 and xt<= 350):
                        caert()
        if yt==325 and (xt>= 720 and xt<= 925):
                        caert()
        if (yt==215 and not (xt>= 368 and xt<=735)) and (y==300 or yl==300):
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor)
            tor=d.create_image(890,140,image=tur1, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            else:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)
        elif (yt==325 and not (xt>= 195 and xt<= 350)) and (y==400 or yl==400):
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor)
            tor=d.create_image(890,140,image=tur1, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            else:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)
        elif (yt==325 and not (xt>= 740 and xt<= 925)) and (y==400 or yl==400):
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor)
            tor=d.create_image(890,140,image=tur1, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            else:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)
        elif (yt==435 and not (xt>=350 and xt<=700)) and (y==520 or yl==520):
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor)
            tor=d.create_image(890,140,image=tur1, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            elif who==who[1]:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)

                        
       
        
        d.after(20,turtleM)
at=-1
def caert():
        global tor,at
        while (at<=81):
                 xt=int(d.coords(tor)[0])
                 yt=int(d.coords(tor)[1])
                 d.move(tor,0,5)
                 d.update()
                 if yt==205:
                         d.move(tor,0,5)
                         break
                 elif yt==315:
                         d.move(tor,0,5)
                         break                         
                 elif yt==425:
                         d.move(tor,0,5)
                         break
                 elif yt==560:
                     break
                 mc.after(5)               
                 at+=3
        at=0
#####TORTUGA DOS######
def turtle2(tur2,v2):
        global tor1,vel,turtle
        vel=v2
        turtle=tur2
        d.delete(tor1)
        tor1=d.create_image(870,140,image=tur2, anchor=NW)
        turtleM2()
def turtleM2():
        global tor1,vel,m,puntuacion,turtle,l,puntuacionm
        xt=int(d.coords(tor1)[0])
        yt=int(d.coords(tor1)[1])
        yl=int(d.coords(l)[1])
        y=int(d.coords(m)[1])
        who=[y,yl]
        d.move(tor1,-v,0)
        if xt < 0 :
                        d.coords(tor1,1122,yt)
        if xt > 1122 :
                        d.coords(tor1,2,yt)
        if xt > 1120 and yt>=560:
            d.delete(tor1)
            tor1=d.create_image(870,140,image=turtle, anchor=NW)
        if (xt==850 or xt==858 or xt==849 or xt==210 or xt==198 or xt==188)and yt==140:
                         caert2()
        if yt==215 and (xt>= 368 and xt<=735):
                        caert2()
        if yt==435 and(xt>=350 and xt<=700):
                        caert2()
        if yt==325 and (xt>= 195 and xt<= 330):
                        caert2()
        if yt==325 and (xt>= 740 and xt<= 925):
                        caert2()
        if (yt==215 and not (xt>= 368 and xt<=735)) and (y==300 or yl==300) :
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor1)
            tor1=d.create_image(870,140,image=turtle, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            else:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)
        elif (yt==325 and not (xt>= 195 and xt<= 350)) and (y==400 or yl==400):
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor1)
            tor1=d.create_image(870,140,image=turtle, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            else:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)
        elif (yt==325 and not (xt>= 740 and xt<= 925)) and (y==400 or yl==400):
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor1)
            tor1=d.create_image(870,140,image=turtle, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            else:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)
        elif (yt==435 and not (xt>=350 and xt<=700)) and (y==520 or yl==520):
            dead=d.create_image(xt,yt+30,image=turvol, anchor=NW)
            d.delete(tor1)
            tor1=d.create_image(870,140,image=turtle, anchor=NW)
            if who==who[2]:
                puntuacion=puntuacion+100
            else:
                puntuacionm=puntuacionm+100
            print (puntuacion,puntuacionm)

                        
       
        
        d.after(20,turtleM2)
at2=-1
def caert2():
        global tor1,at2
        while (at2<=81):
                 xt=int(d.coords(tor1)[0])
                 yt=int(d.coords(tor1)[1])
                 d.move(tor1,0,5)
                 d.update()
                 if yt==205:
                         d.move(tor1,0,5)
                         break
                 elif yt==315:
                         d.move(tor1,0,5)
                         break                         
                 elif yt==425:
                         d.move(tor1,0,5)
                         break
                 elif yt==560:
                     break   
                 mc.after(5)               
                 at2+=3
        at2=0

def key(event):
        global Pre,Ac,Mov
        tecla = event.keysym
        Tec=["w","a","d",'Up','Right','Left']
        if (tecla in Tec):
                Mov[tecla]=True

def keyReleased(event):
        global Pre,Ac,Mov
        tecla = event.keysym
        Tec=["w","a","d",'Up','Right','Left']
        if (tecla in Tec):
                Mov[tecla]=False

Mov={"w":False,"a":False,"d":False,'Up':False,'Right':False,'Left':False}
##etiquetas de nombres, puntuacion y vida
def printn():
        jug1=Label(dif,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=925,y=30)
        mvl=Label(dif,text='Mario and Luigi',font=("Arcade",40),bg='black',fg='white').place(x=380,y=25)
        puntosm=Label(dif,text=puntuacionm,font=("Arcade",32),bg='black',fg='white').place(x=60,y=60)
        puntosl=Label(dif,text=puntuacion,font=("Arcade",32),bg='black',fg='white').place(x=925,y=60)
nivel1dif = Button(nombres,text="Nivel 1",cursor="hand2",bg='blue', fg='white',command=lambda: mostrar(dif) or move() or movel() or (ocultar(nombres))or printn() or turtle(turder,3) or turtle2(turiz,3) or Play(),activeforeground="#F50743").place(x=75,y=250)#boton dificultad 1
nivel2dif = Button(nombres,text="Nivel 2",cursor="hand2",bg='blue', fg='white',command=lambda: mostrar(dif) or move() or movel() or (ocultar(nombres))or printn()or turtle(turder,4) or turtle2(turiz,4)or Play(),activeforeground="#F50743").place(x=150,y=250)#2
nivel3dif = Button(nombres,text="Nivel 3",cursor="hand2",bg='blue', fg='white',command=lambda: mostrar(dif) or move() or movel() or (ocultar(nombres))or printn()or turtle(turder2,5) or turtle2(turiz2,5)or Play(),activeforeground="#F50743").place(x=225,y=250)#3
nivel4dif = Button(nombres,text="Nivel 4",cursor="hand2",bg='blue', fg='white',command=lambda: mostrar(dif) or move() or movel() or (ocultar(nombres))or printn()or (turtle(turder2,6)) or turtle2(turiz2,6)or Play(),activeforeground="#F50743").place(x=300,y=250)#4
nivel5dif = Button(nombres,text="Nivel 5",cursor="pirate",bg='blue', fg='white',command=lambda: mostrar(dif) or move() or movel() or (ocultar(nombres))or printn()or (turtle(turder3,7)) or turtle2(turiz3,7)or Play(),activeforeground="#F50743").place(x=375,y=250)#5

d.focus_set()
d.bind_all('<KeyPress>',key)
d.bind("<KeyRelease>",keyReleased)
d.mainloop()
mc.mainloop()

