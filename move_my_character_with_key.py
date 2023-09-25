from pico2d import *

cut = ((1,32,48),(4,32,48),(4,100,100))
cs = (3,2,1,0,3,2,1,0)

open_canvas(800,600)
back = load_image('TUK_GROUND.png')
boy = load_image('boy.png')

x = 400
y = 300
xdir = 0
ydir =0
state = 0  # 0 : stand 1: walk 2:run
see = 0
leftdown = 0; rightdown=0 ;updown=0;downdown=0;spacedown =0
frame = 0


while(True):
    clear_canvas()
    back.draw(400,300,800,600)
    if (state < 2):boy.clip_composite_draw((cut[state][1]*(frame%cut[state][0])),400+(7-see)*cut[state][2],cut[state][1],cut[state][2],0,'n',x,y,2*cut[state][1],2*cut[state][2])
    else : boy.clip_composite_draw((cut[state][1]*(frame%cut[state][0])),(cs[see])*cut[state][2],cut[state][1],cut[state][2],0,'n',x,y,2*cut[state][1],2*cut[state][2])

    update_canvas()
    frame = frame + 1
    delay(0.05)
    events = get_events()
    for event in events:
        if (event.type == SDL_KEYDOWN):
            if (event.key == SDLK_RIGHT):
                rightdown = 1
                xdir += 1
            if (event.key == SDLK_LEFT):
                leftdown = 1
                xdir -= 1
            if (event.key == SDLK_UP):
                updown = 1
                ydir += 1
            if (event.key == SDLK_DOWN):
                downdown = 1
                ydir -= 1
            if (event.key == SDLK_SPACE):
                spacedown = 1
        elif (event.type == SDL_KEYUP):
            if (event.key == SDLK_RIGHT):
                print("오른쪽키업!")
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
    if (spacedown and (updown or downdown or rightdown or leftdown)):
        state = 2
    elif (updown or downdown or rightdown or leftdown):
        state = 1
    else:
        state = 0

    if (updown and leftdown):
        see = 5
    elif (updown and rightdown):
        see = 7
    elif (downdown and leftdown):
        see = 4
    elif (downdown and rightdown):
        see = 6
    elif (leftdown):
        see = 1
    elif (rightdown):
        see = 2
    elif (updown):
        see = 3
    elif (downdown):
        see = 0

    x += xdir * 5 * state
    if (x>800): x = 800
    if (x < 0 ): x = 0
    y += ydir * 5 * state
    if (y>600): y = 600
    if (y < 0): y = 0

