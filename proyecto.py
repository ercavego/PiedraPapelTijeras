# lo esencial
import tkinter
import random
juego = tkinter.Tk()
juego.title("Piedra, papel o tijeras!!")
juego.geometry("400x400")
juego.configure(bg="#50A8BF")
puntaje_jugador = 0
puntaje_computador = 0
imagen = tkinter.PhotoImage(file="/Users/ernestovegagomez/Downloads/piedrapapeltijeras.png")
imagen_label = tkinter.Label(juego,image=imagen, width=600, height=400 )
imagen_label.place(relx=.50,rely=.13)
#marco
marco= tkinter.LabelFrame(juego, text= "Piedra, papel o tijeras", font= ('Oswald 20 bold'),labelanchor= "n",bd=5,bg= "darkseagreen",width= 500, height= 450, cursor= "spider")
marco.grid(padx=100, pady=100)
#instrucciones
saludo = tkinter.Label(juego,text="Presiona uno de los botones para escoger piedra, papel o tijeras.",font="Oswalrd 16 bold", bg="midnightblue")
saludo.grid(row=1, column=0)
saludo2 = tkinter.Label(juego,text="Luego, clickea reset para volver a jugar. Disfruta!",font="Oswalrd 16 bold", bg="midnightblue")
saludo2.grid(row=2, column=0)

#labels jugador, computador, puntaje
l1= tkinter.Label(marco, text="Jugador", font= ('Helvetica 18 bold'))
l1.place(relx= .18, rely= .1)

l2= tkinter.Label(marco, text="Computador", font= ('Helvetica 18 bold'))
l2.place(relx= .38, rely= .1)

l3= tkinter.Label(marco, text="Suerte :)", font=("Helvetica 18 bold"))
l3.place(relx= .68, rely=.1)

l4= tkinter.Label(marco, text="PUNTAJE:", font=("Helvetica 18 bold"))
l4.place(relx=.40, rely=.4)

opciones=["Piedra","Papel","Tijeras"]

# funciones para cada opción
def scissors():
   value = random.choice(opciones)
   global puntaje_computador
   global puntaje_jugador
   if value == "Piedra":
      match_result = "Perdiste :("
      puntaje_computador +=1
   elif value == "Tijeras":
      match_result = "Empate"
   else:
      match_result = "Ganaste!!"
      puntaje_jugador +=1
   l1.config(text = "Tijeras")
   l2.config(text = value)
   l3.config(text = match_result)
   l4.config(text ="Jugador: %d\nComputador: %d"%(puntaje_jugador,puntaje_computador))
   boton_disable()

def paper():
   value = random.choice(opciones)
   global puntaje_jugador
   global puntaje_computador
   if value == "Tijeras":
      match_result = "Perdiste :("
      puntaje_computador +=1
   elif value == "Papel":
      match_result = "Empate"
   else:
      match_result = "Ganaste!!"
      puntaje_jugador +=1
   l1.config(text = "Papel")
   l2.config(text = value)
   l3.config(text = match_result)
   l4.config(text ="Jugador: %d\nComputador: %d"%(puntaje_jugador,puntaje_computador))
   boton_disable()

def rock():
   value = random.choice(opciones)
   global puntaje_computador
   global puntaje_jugador
   if value == "Papel":
      match_result = "Perdiste :("
      puntaje_computador +=1
   elif value == "Piedra":
      match_result = "Empate"
   else:
      match_result = "Ganaste!!"
      puntaje_jugador += 1
   l1.config(text = "Piedra")
   l2.config(text = value)
   l3.config(text = match_result)
   l4.config(text ="Jugador: %d\nComputador: %d"%(puntaje_jugador,puntaje_computador))
   boton_disable()

#reiniciamos los botones para volver a jugar
def reset():
    boton_tijeras.config(state= "active")
    boton_papel.config(state= "active")
    boton_piedra.config(state= "active")
    l1.config(text = "Jugador")
    l2.config(text = "Computadora")
    l3.config(text="Suerte :)")

#desactivar los botones despues de cada partida
def boton_disable():
   boton_papel.config(state= "disabled")
   boton_piedra.config(state= "disabled")
   boton_tijeras.config(state= "disabled")

#botones de cada opcion
boton_tijeras = tkinter.Button(juego, text="TIJERAS ✂", highlightbackground="yellow",pady="5",command=scissors)
boton_piedra = tkinter.Button(juego, text="PIEDRA 🪨",highlightbackground="yellow",pady="5",command=rock)
boton_papel = tkinter.Button(juego, text="PAPEL 📄",highlightbackground="yellow",pady="5",command=paper)
boton_reset = tkinter.Button(juego,text="RESET", fg="red", pady="5",command=reset)

boton_tijeras.place(relx= .58, rely= .62)
boton_piedra.place(relx=.25, rely= .62)
boton_papel.place(relx= .41,rely= .62)
boton_reset.place(relx=.75, rely=.62)

juego.mainloop()
