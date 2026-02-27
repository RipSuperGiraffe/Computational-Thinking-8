import turtle, math, time, random
from utils import *
s1=create_sprite("steve",-250,0)


def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")

s2=create_sprite("ball",0,0)
s3=create_sprite("dooor",275,0)
# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []

# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    x = s2.xcor() + random.randint(-7,7)
    y = s2.ycor() + random.randint(-7,7)
    s2.goto(x,y)




    if get_distance (s1,s3) < 15:
        print("you win")
        break

    time.sleep(0.01)
    window.update()

    # for i in 100%


    # TODO - make an if statement for ending the game
    if get_distance (s1,s2) < 200:
        print("You lose")
        break
    
    time.sleep(0.01)
    window.update()
    
    if i % 200 ==0:
        x=(250)
        y=random.randint(-300,300)
        item=create_sprite("sodacan",x,400)
        item.setheading(180)
        sprite_list.append(item)
    for item in sprite_list:
        item.forward(5)

	
print("Game Over")

