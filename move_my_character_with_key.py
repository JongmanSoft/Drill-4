from pico2d import *

stand_ysize = ((0,118),(118,115),(233,119),(352,124),(476,114))
walk_ysize = ((0,121),(121,117),(238,144),(382,120),(502,120))
vh = ('v', 'h')

def handle_event():
    global xdir, ydir
    global state  #0 : stand 1: walk 2:run
    global dir #0: up, 1:upleft 2:left 3:downleft 4:down
    global vhdir
    global leftdown, rightdown, updown, downdown , spacedown

    events = get_events()
    for event in events:
        if (event.type == SDL_KEYDOWN):
            if (event.key == SDLK_RIGHT):
                vhdir = 1
                rightdown = 1
                xdir += 1
            if (event.key == SDLK_LEFT):
                vhdir = 0
                leftdown = 1
                xdir -= 1
            if (event.key == SDLK_UP):
                updown = 1
                ydir += 1
            if (event.key == SDLK_DOWN):
                downdown = 1
                ydir -= 1
            if (event.key == SDLK_SPACE):
                spacedown =1
        elif (event.type == SDL_KEYUP):
            if (event.type == SDL_KEYDOWN):
                if (event.key == SDLK_RIGHT):
                    rightdown = 0
                    xdir -= 1
                if (event.key == SDLK_LEFT):
                    leftdown = 0
                    xdir += 1
                if (event.key == SDLK_UP):
                    updown = 0
                    ydir -= 1
                if (event.key == SDLK_DOWN):
                    downdown = 0
                    ydir += 1
                if (event.key == SDLK_SPACE):
                    spacedown = 0
    if (spacedown and (updown or downdown or rightdown or leftdown)): state = 2
    elif (updown or downdown or rightdown or leftdown): state = 1
    else: state = 0

    if (updown and (leftdown or rightdown)):dir = 1
    elif (downdown and (leftdown or rightdown)): dir = 3
    elif ((leftdown or rightdown)) dir = 2
    elif (updown): dir = 0
    elif (downdown):dir = 4


stand = load_image()
walk = load_image()
