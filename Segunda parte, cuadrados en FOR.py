from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

posiciones_de_partida = [(0, 0), (-20, 0), (-40, 0)]

for posicion in posiciones_de_partida:  # Vamos a ir por cada una de las posiciones
    tortugas = Turtle(shape="square")
    tortugas.color("white")
    tortugas.goto(posicion)  # Cada tortuga creada va a ir a una posicion diferente de la anterior





screen.exitonclick()
