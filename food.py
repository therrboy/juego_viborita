from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Forma de la comida
        self.penup()  # Asi la comida no deja marcas de dibujo
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)  # Tamaño de la "comida"
        self.color("green")  # Color
        self.speed("fastest")  # Velocidad
        self.refrescar()  # Llamamos a una funcion


    def refrescar(self):
        random_x = random.randint(-280, 280)  # Numero al azar entre -280 y 280 para valor X
        random_y = random.randint(-280, 280)  # Igual que arriba solo que con Y
        self.goto(random_x, random_y)
