from turtle import Turtle

posiciones_de_partida = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segmentos = []
        self.create_snake()
        self.head = self.segmentos[0]

    def create_snake(self):  # Crea la serpiente de 3 segmentos
        for posicion in posiciones_de_partida:  # Vamos a ir por cada una de las posiciones
            self.nuevo_cuerpo(posicion)

    def nuevo_cuerpo(self, posicion):
        nuevo_segmento = Turtle(shape="square")  # El segmento va a ser el cuadrado, esto crea la "Tortuga"
        nuevo_segmento.penup()  # Levanta el lapiz para no dibujar una linea por detras
        nuevo_segmento.color("white")
        nuevo_segmento.goto(posicion)  # La tortuga se movera a la posicion marcada en la variable posiciones de partida
        self.segmentos.append(nuevo_segmento)  # Aca con el self pedimos el valor del anterior, sin tener que llamar por fuera

    def añadir_cuerpo(self):
        self.nuevo_cuerpo(self.segmentos[-1].position())

    def move(self):
        for segmento_num in range(len(self.segmentos) - 1, 0, -1):  # Donde empieza, donde termina y los pasos a dar
            new_x = self.segmentos[segmento_num - 1].xcor()  # segmento de X del cuerpo numero 2 (empezamos con 2 pero al darle menos 1 posiciona)
            new_y = self.segmentos[segmento_num - 1].ycor()  # segmento de Y del cuerpo numero 2
            self.segmentos[segmento_num].goto(new_x, new_y)  # segmento X e Y de cuerpo numero 2 para cuerpo 3
        self.head.forward(move_distance)  # Ahora nuestra serpiente se mueve y el cuerpo sigue a donde va la cola

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






