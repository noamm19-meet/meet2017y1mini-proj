import turtle

import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE= 20
START_LENGHT= 1
pos_list=[]
stamp_list=[]
food_list= []
food_stamps=[]
food_pos = []

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
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP= 100
SPACEBAR="space"


UP=0
LEFT=1
DOWN=2
RIGHT=3
direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction=UP 
    print('you pressed up')

def left():
    global direction
    direction=LEFT
    print('you pressed left')

def down():
    global direction
    direction=DOWN
    print('you pressed down')

    
def right():
    global direction
    direction=RIGHT
    print('you pressed right')

turtle.onkeypress(up , UP_ARROW)
turtle.onkeypress(left , LEFT_ARROW)
turtle.onkeypress(down , DOWN_ARROW)   
turtle.onkeypress(right , RIGHT_ARROW)
turtle.listen()

def make_food():
    min_x= -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x= int(SIZE_X/2/SQUARE_SIZE)-1
    min_y= -int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y= int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
   
    food.goto(food_x , food_y)
    food_pos.append(food.pos())
    random_food= food.stamp()
    food_stamps.append(random_food)  
                
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('you moved right')
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos) 
        print('you moved left')
    elif direction==UP:
        snake.goto(x_pos ,SQUARE_SIZE + y_pos)
        print('you moved up')
    else:
         snake.goto(x_pos , y_pos - SQUARE_SIZE)
         print('you moved down')

         
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    global food_stamp, food_pos
    if snake.pos() in food_pos:
        food_ind= food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        make_food()
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)

        x_pos= snake.pos()[0]
        y_pos= snake.pos()[1]
        x_pos+=SQUARE_SIZE
        my_pos= (x_pos, y_pos)
        snake.goto(x_pos, y_pos)
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
       
        

    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print('GAME OVER!')
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print('GAME OVER')
        quit()
    elif new_y_pos >= UP_EDGE:
        print('GAME OVER')
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print('GAME OVER')
        quit()
        
    if pos_list[-1] in pos_list[0:-1]:	
        quit()

    turtle.ontimer(move_snake, TIME_STEP)

turtle.register_shape('trash.gif')

food= turtle.clone()
food.shape('trash.gif')




##food.hideturtle()
##for this_food_pos in food_pos:
##    food.goto(this_food_pos)    
##    new_food=food.stamp()
##    food_stamps.append(new_food)
    

move_snake()
make_food()
 
    

    
    
