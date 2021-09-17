
import turtle
import time
import random
import numpy as np
color = list(np.random.choice(range(256), size=3))
delay = 0.1

#puntuacion 
score = 0
high_score = 0

#pantalla
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

#cabeza
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#comida
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

segments = []

#puntos actualizados
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 24, "normal"))

#funciones
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#teclado
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#loop
while True:
    wn.update()

    #colosion
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    
        for segment in segments:
            segment.goto(1000,1000) #out of range

        segments.clear()

    
        score = 0

       
        delay = 0.1

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    #al comer
    if head.distance(food) <20:
        # move the food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #crecer
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red","green")
        new_segment.penup()
        segments.append(new_segment)

       
        delay -= 0.001
       
        score += 1

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

    
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #autocomerse
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #reinicio  
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
wn.mainloop()   