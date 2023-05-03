from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


posiciones_de_partida = [(0, 0), (-20, 0), (-40, 0)]

segmentos = []

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
    for segmento in segmentos:
        segmento.forward(20)

screen.exitonclick()