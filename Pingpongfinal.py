import turtle as t


import os

#iniciar marcador

player_a_score = 0
player_b_score = 0
win = t.Screen()   
win.title("Ping-Pong Game") 
win.bgcolor('black')    
win.setup(width=800,height=600) 
win.tracer(0)   

# izquierda
izquierda = t.Turtle()
izquierda.speed(0)
izquierda.shape('square')
izquierda.color('white')
izquierda.shapesize(stretch_wid=5,stretch_len=1)
izquierda.penup()
izquierda.goto(-350,0)

# derecha

derecha = t.Turtle()
derecha.speed(0)
derecha.shape('square')
derecha.shapesize(stretch_wid=5,stretch_len=1)
derecha.color('white')
derecha.penup()
derecha.goto(350,0)

# pelota

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball_dx = .3   # velocidad de la pelota
ball_dy = .3

# marcador

mar = t.Turtle()
mar.speed(0)
mar.color('white')
mar.penup()
mar.hideturtle()
mar.goto(0,260)
mar.write("Player A: 0                    Player B: 0 ",align="center",font=('Monaco',24,"normal"))


# movimiento hacia arriba izquierda

def paddle_left_up():
    y = izquierda.ycor()
    y = y + 15
    izquierda.sety(y)

# movimiento hacia abajo izquierda

def paddle_left_down():
    y = izquierda.ycor()
    y = y - 15
    izquierda.sety(y)

# movimiento hacia arriba derecha

def paddle_right_up():
    y = derecha.ycor()
    y = y + 15
    derecha.sety(y)

# movimiento hacia arriba izquierda

def paddle_right_down():
    y = derecha.ycor()
    y = y - 15
    derecha.sety(y)

# controles

win.listen()
win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")




# cuerpo

while True:
    win.update() 

    # movimiento pelota
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # propiedades de los bordes

    if ball.ycor() > 290:   
        ball.sety(290)
        ball_dy = ball_dy * -1


    if ball.ycor() < -290:  
        ball.sety(-290)
        ball_dy = ball_dy * -1


    if ball.xcor() > 390:   
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        mar.clear()
        mar.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: 
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        mar.clear()
        mar.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")


    # colisiones

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < derecha.ycor() + 40 and ball.ycor() > derecha.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < izquierda.ycor() + 40 and ball.ycor() > izquierda.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")