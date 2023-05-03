from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

posiciones_de_partida = [(0, 0), (-20, 0), (-40, 0)]

rafael = Turtle(shape="square")
rafael.color("white")

rafael1 = Turtle(shape="square")
rafael1.color("white")
rafael1.penup()
rafael1.goto(posiciones_de_partida[1])

rafael2 = Turtle(shape="square")
rafael2.color("white")
rafael1.penup()
rafael2.goto(posiciones_de_partida[2])

screen.exitonclick()
