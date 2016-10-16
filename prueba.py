#Prueba 1

from tkinter import*
from tkinter import font


mc= Tk()
nombres=Toplevel()
dif1=Toplevel()
d1 = Canvas(dif1, bg="black", height=655, width=1320).place(x=0,y=0)
dif2=Toplevel()
d2 = Canvas(dif2, bg="black", height=655, width=1320).place(x=0,y=0)
dif3=Toplevel()
d3 = Canvas(dif3, bg="black", height=655, width=1320).place(x=0,y=0)
dif4=Toplevel()
d4 = Canvas(dif4, bg="black", height=655, width=1320).place(x=0,y=0)
dif5=Toplevel()
d5 = Canvas(dif5, bg="black", height=655, width=1320).place(x=0,y=0)

def mostrar(nombres): nombres.deiconify()
def ocultar(mc): mc.withdraw()
def ejecutar(f): mc.after(200,f)
def printn():
        jug1=Label(dif1,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif1,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=1145,y=30)
        mvl=Label(dif1,text='Mario VS Luigi',font=("Arcade",40),bg='black',fg='white').place(x=480,y=25)
        jug1=Label(dif2,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif2,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=1145,y=30)
        mvl=Label(dif2,text='Mario VS Luigi',font=("Arcade",40),bg='black',fg='white').place(x=480,y=25)
        jug1=Label(dif3,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif3,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=1145,y=30)
        mvl=Label(dif3,text='Mario VS Luigi',font=("Arcade",40),bg='black',fg='white').place(x=470,y=25)
        jug1=Label(dif4,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif4,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=1145,y=30)
        mvl=Label(dif4,text='Mario VS Luigi',font=("Arcade",40),bg='black',fg='white').place(x=480,y=25)
        jug1=Label(dif5,text=jug01.get(),font=("Arcade",32),bg='black',fg='white').place(x=60,y=30)
        jug2=Label(dif5,text=jug02.get(),font=("Arcade",32),bg='black',fg='white').place(x=1145,y=30)
        mvl=Label(dif5,text='Mario VS Luigi',font=("Arcade",40),bg='black',fg='white').place(x=480,y=25)
#carateristicas ventana principal
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
##Imagenes jugadores
mjug1=PhotoImage(file="mariojug1.gif")
ljug2=PhotoImage(file="luigijug2.gif")
#dificultades carac...
dif1.geometry('1320x655+15+15')
dif1.title('Juego Super Mario-Dificultad 1')
picm=Label(dif1,image=mjug1,bd=0).place(x=5,y=10)
picl=Label(dif1,image=ljug2,bd=0).place(x=1265,y=10)
##
dif2.geometry('1320x655+15+15')
dif2.title('Juego Super Mario-Dificultad 2')
picm=Label(dif2,image=mjug1,bd=0).place(x=5,y=10)
picl=Label(dif2,image=ljug2,bd=0).place(x=1265,y=10)
##
dif3.geometry('1320x655+15+15')
dif3.title('Juego Super Mario-Dificultad 3')
picm=Label(dif3,image=mjug1,bd=0).place(x=4,y=10)
picl=Label(dif3,image=ljug2,bd=0).place(x=1265,y=10)
##
dif4.geometry('1320x655+15+15')
dif4.title('Juego Super Mario-Dificultad 4')
picm=Label(dif4,image=mjug1,bd=0).place(x=5,y=10)
picl=Label(dif4,image=ljug2,bd=0).place(x=1265,y=10)
##
dif5.geometry('1320x655+15+15')
dif5.title('Juego Super Mario-Dificultad 5')
picm=Label(dif5,image=mjug1,bd=0).place(x=5,y=10)
picl=Label(dif5,image=ljug2,bd=0).place(x=1265,y=10)

nombres.withdraw()
dif1.withdraw()
dif2.withdraw()
dif3.withdraw()
dif4.withdraw()
dif5.withdraw()
btn= font.Font(family="Verdana", size=15)
entrada = Button(mc,text="Empezar",cursor="hand2",bg='orange',font= btn,command=lambda: ejecutar(mostrar(nombres)) or (ocultar(mc)),activeforeground="white",bd=10).place(x=410, y=390)#boton ventana principal
nivel1dif = Button(nombres,text="Nivel 1",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif1)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=75,y=250)#boton dificultad 1
nivel2dif = Button(nombres,text="Nivel 2",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif2)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=150,y=250)#2
nivel3dif = Button(nombres,text="Nivel 3",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif3)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=225,y=250)#3
nivel4dif = Button(nombres,text="Nivel 4",cursor="hand2",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif4)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=300,y=250)#4
nivel5dif = Button(nombres,text="Nivel 5",cursor="pirate",bg='blue', fg='white',command=lambda: ejecutar(mostrar(dif5)) or (ocultar(nombres))or printn(),activeforeground="#F50743").place(x=375,y=250)#5
mc.mainloop()
