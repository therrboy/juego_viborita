from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score
import time

screen = Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

puntos = 0
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

juego_on = True
while juego_on:
    screen.update()  # Tasa de refresco de la "pantalla", fuera del for para mover todo junto
    time.sleep(0.1)  # Tiempo que tardara de figura "cuadrada" en moverse y parar
    snake.move()

    # Detectar colision con limite de pantalla
    score.limite_pantalla()

    # Detectar colision con la tortuga/comida
    if snake.head.distance(food) < 15:
        score.contador()
        puntos += 1
        food.refrescar()
        snake.añadir_cuerpo()

    # Detectar colision con las paredes
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        juego_on = False
        score.game_over()

    # Detectar colision con cola
    for segmento in snake.segmentos[1:]:
        if snake.head.distance(segmento) < 10:
            juego_on = False
            score.game_over()

    if not juego_on:
        score.puntuacion_maxima(puntos)



screen.exitonclick()
