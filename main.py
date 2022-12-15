#https://www.patreon.com/posts/45998588

# import libraries
# turtle is library for graphics
import turtle
# 
import random
# 
import time
# 
import os

# access to files...
game_folder = os.path.dirname(__file__)

bgimg = os.path.join(game_folder, )

limg= Label(master, i=bgimg)
limg.pack()
master.mainloop()


#make the screen
screen = turtle.screen()
screen.title('Joey Snake Game')
screen.setup(width = 850, height = 850)
screen.tracer(0)
turtle.bgcolor('green')

#create borders

turtle.speed(10)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#scoring
score = 0
delay = 0.2


#snake information
snake = turtle.Turtle()
snake.speed(20)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'


#food information
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30,30)

old_fruit=[]

#scoring information
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Courier",24,"bold"))


#control instructions
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# direction information
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

#actual game

while True:
        screen.update()
            #snake and fruit coliisions
        if snake.distance(fruit)< 20:
                x = random.randint(-290,270)
                y = random.randint(-240,240)
                fruit.goto(x,y)
                scoring.clear()
                score+=1
                scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
                delay-=0.001
                
                ## creating new_ball
                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape('square')
                new_fruit.color('red')
                new_fruit.penup()
                old_fruit.append(new_fruit)
                

        #adding their score and the actual apple on the snake
        
        for index in range(len(old_fruit)-1,0,-1):
                a = old_fruit[index-1].xcor()
                b = old_fruit[index-1].ycor()

                old_fruit[index].goto(a,b)
                                     
        if len(old_fruit)>0:
                a= snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a,b)
        snake_move()

        #when the game ends   
        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        ## snake collision
        for food in old_fruit:
                if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('turquoise')
                        scoring.goto(0,0)
                        scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"Times New Roman"))


                
        time.sleep(delay)

turtle.Terminator()

