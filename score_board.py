from turtle import Turtle

alineacion = "center"  # Colocamos las modificaciones que quisieramos hacer mas adelante, aca arriba para que sea mas facil de ubicar
fuente = ("Arial", 15, "normal")




class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.marcador = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.puntitos = 0
        self.marcador_pantalla()


    def limite_pantalla(self):
        self.goto(-290, 290)
        self.pendown()
        for i in range(4):
            self.forward(580)
            self.right(90)


    def marcador_pantalla(self):
        with open("puntuacion_maxima.txt") as data:
            puntaje_maximo = int(data.read())

        self.penup()
        self.goto(0, 300)
        self.write(f"Puntos = {self.marcador} \nMaxima puntuacion anterior= {puntaje_maximo}", align="center", font=fuente)

    def contador(self):
        self.marcador += 1  # Como ya esta funcion corre si o si cuando comemos, automaticamente decimos que aumente en 1
        self.clear()
        self.marcador_pantalla()

    def puntuacion_maxima(self, puntos):
        with open("puntuacion_maxima.txt") as data:
            puntaje_maximoooooooo = int(data.read())
        if puntaje_maximoooooooo < puntos:
            with open("puntuacion_maxima.txt", mode="w") as file:
                file.write(f"{puntos}")

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", align=alineacion, font=fuente)



