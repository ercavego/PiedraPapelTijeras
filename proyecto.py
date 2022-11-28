# lo esencial
import tkinter
import random
juego = tkinter.Tk()
juego.title("Piedra, papel o tijeras!!")
juego.geometry("400x400")
juego.configure(bg="#50A8BF")
puntaje_jugador = 0
puntaje_comptuador = 0

#marco
marco= tkinter.LabelFrame(juego, text= "Piedra, papel o tijeras", font= ('Oswald 20 bold'),labelanchor= "n",bd=5,bg= "goldenrod",width= 500, height= 350, cursor= "spider")
marco.grid(padx=100, pady=100)
#marco.pack(expand=True, fill="both")

saludo = tkinter.Label(juego,text="Bienvenido a piedra, papel o tijeras", bg="red")
#labels jugador, computador, puntaje
l1= tkinter.Label(marco, text="Jugador", font= ('Helvetica 18 bold'))
l1.place(relx= .18, rely= .1)

l2= tkinter.Label(marco, text="Computador", font= ('Helvetica 18 bold'))
l2.place(relx= .38, rely= .1)

l3= tkinter.Label(marco, text="Suerte", font=("Helvetica 18 bold"))
l3.place(relx= .68, rely=.1)

l4= tkinter.Label(marco, text="PUNTAJE:", font=("Helvetica 18 bold"))
l4.place(relx=.40, rely=.4)

opciones=["piedra","papel","tijeras"]

# funciones para cada opción
def scissors():
   value = random.choice(opciones)
   global puntaje_comptuador
   global puntaje_jugador
   if value == "piedra":
      match_result = "Perdiste :("
      puntaje_comptuador +=1
   elif value == "tijeras":
      match_result = "Empate"
   else:
      match_result = "Ganaste!!"
      puntaje_jugador +=1
   l1.config(text = "tijeras")
   l2.config(text = value)
   l3.config(text = match_result)
   l4.config(text ="Jugador: %d\nComputador: %d"%(puntaje_jugador,puntaje_comptuador))
   boton_disable()


def paper():
   value = random.choice(opciones)
   global puntaje_jugador
   global puntaje_comptuador
   if value == "tijeras":
      match_result = "Perdiste :("
      puntaje_comptuador +=1
   elif value == "papel":
      match_result = "Empate"
   else:
      match_result = "Ganaste!!"
      puntaje_jugador +=1
   l1.config(text = "papel")
   l2.config(text = value)
   l3.config(text = match_result)
   l4.config(text ="Jugador: %d\nComputador: %d"%(puntaje_jugador,puntaje_comptuador))
   boton_disable()

def rock():
   value = random.choice(opciones)
   global puntaje_comptuador
   global puntaje_jugador
   if value == "papel":
      match_result = "Perdiste :("
      puntaje_comptuador +=1
   elif value == "piedra":
      match_result = "Empate"
   else:
      match_result = "Ganaste!!"
      puntaje_jugador += 1
   l1.config(text = "piedra")
   l2.config(text = value)
   l3.config(text = match_result)
   l4.config(text ="Jugador: %d\nComputador: %d"%(puntaje_jugador,puntaje_comptuador))
   boton_disable()

#reiniciamos los botones para volver a jugar
def reset():
    boton_tijeras.config(state= "active")
    boton_papel.config(state= "active")
    boton_piedra.config(state= "active")
    l1.config(text = "Jugador")
    l2.config(text = "Computadora")
    l3.config(text="Buena suerte")

#desactivar los botones despues de cada partida
def boton_disable():
   boton_papel.config(state= "disabled")
   boton_piedra.config(state= "disabled")
   boton_tijeras.config(state= "disabled")

#problema con los colores en macOS
#botones de cada opcion
boton_tijeras = tkinter.Button(juego, text="TIJERAS ✂", highlightbackground="yellow",pady="5",command=scissors)
boton_piedra = tkinter.Button(juego, text="PIEDRA 🪨",highlightbackground="yellow",pady="5",command=rock)
boton_papel = tkinter.Button(juego, text="PAPEL 📄",highlightbackground="yellow",pady="5",command=paper)
boton_reset = tkinter.Button(juego,text="RESET", fg="red", command=reset)

boton_tijeras.place(relx= .58, rely= .62)
boton_piedra.place(relx=.25, rely= .62)
boton_papel.place(relx= .41,rely= .62)
boton_reset.place(relx=.8, rely=.62)

juego.mainloop()