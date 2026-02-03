import turtle, time, random
from utils import *
# SECRET there is a special reward when you get to 350 cookies, make sure to get 350 cookies to check it out
#once you get the reward go to line 56, ONLY DO THIS AFTER YOU GET THE REWARD
# Section 1 - setup
# TODO - set a background using set_background()
set_background("barn")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
#-----------------------------------------------------------------------------------------
#the goal of the game is to get a jar after you get 25 cookies
cookies = 1
jars = 0
cost = 25
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,200)
message_sprite.hideturtle()

create_sprite ("Cookie Clicker")

# Section 2 - controls
# TODO - define an action. ex: def my_control()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control
#this codes lets you buy a ajr when you reach 25 cookies
def get_cookies () :
    global cookies, jars, cost
    if cookies >= cost:
        cost = cost * 2
        jars += 1 
        x = random.randint (-200,200) 
        y = random.randint ( -200,200)
        create_sprite("jar")

window.onkeypress(get_cookies, "j")
#everytime you press c you get a cookie
def get_cookies():
    global cookies
    cookies += 1

window.onkeypress(get_cookies, "c")
# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    message_sprite.write(f" Cookies {cookies}")

    time.sleep(0.01)
    window.update()
#there was never a special reward, i was just wasting your time