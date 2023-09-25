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

            if (event.key == SDLK_LEFT):

            if (event.key == SDLK_UP):

            if (event.key == SDLK_DOWN):

            if (event.key == SDLK_SPACE):
