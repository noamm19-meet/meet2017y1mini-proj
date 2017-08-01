import turtle

import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE= 20
START_LENGHT= 6
pos_list=[]
stamp_list=[]
food_list= []
food_stamp=[]

snake= turtle.clone()
snake.shape('square')

turtle.hideturtle()

for num in range(0,START_LENGHT):
    x_pos= snake.pos()[0]
    y_pos= snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos= (x_pos, y_pos)
    snake.goto(x_pos, y_pos)
    pos_list.append(my_pos)
    new_stamp= snake.stamp()
    stamp_list.append(new_stamp)
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"
UP=0

UP=0
LEFT=1
DOWN=2
RIGHT=3

def up():
    global direction
    direction=UP
    move_snake()
    print('you pressed up')

def left():
    global direction
    direction=LEFT
    move_snake()
    print('you pressed left')

def down():
    global direction
    direction=DOWN
    move_snake()
    print('you pressed down')

    
    

    
    
    
    
    
    
