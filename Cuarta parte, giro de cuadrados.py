# En esta parte hacemos que la cabeza de la serpiente sea seguida por su cuerpo.
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


posiciones_de_partida = [(0, 0), (-20, 0), (-40, 0)]

segmentos = []

# Este segmento de codigo abajo, es donde nace nuestra "vivora" con 3 cuadrados como cuerpo

for posicion in posiciones_de_partida:  # Vamos a ir por cada una de las posiciones
    nuevo_segmento = Turtle(shape="square")  # El segmento va a ser el cuadrado, esto crea la "Tortuga"
    nuevo_segmento.color("white")
    nuevo_segmento.penup()  # Levanta el lapiz para no dibujar una linea por detras
    nuevo_segmento.goto(posicion)  # La tortuga se movera a la posicion marcada en la variable posiciones de partida
    segmentos.append(nuevo_segmento)


juego_on = True
while juego_on:
    screen.update()  # Tasa de refresco de la "pantalla", fuera del for para mover todo junto
    time.sleep(0.1)  # Tiempo que tardara de figura "cuadrada" en moverse y parar

    for segmento_num in range(len(segmentos) -1, 0, -1):  # Donde empieza, donde termina y los pasos a dar
        new_x = segmentos[segmento_num - 1].xcor()  # segmento de X del cuerpo numero 2 (empezamos con 2 pero al darle menos 1 posiciona)
        new_y = segmentos[segmento_num - 1].ycor()  # segmento de Y del cuerpo numero 2
        segmentos[segmento_num].goto(new_x, new_y)  # segmento X e Y de cuerpo numero 2 para cuerpo 3
    segmentos[0].forward(20) # Ahora nuestra serpiente se mueve y el cuerpo sigue a donde va la cola
    segmentos[0].right(90)

screen.exitonclick()