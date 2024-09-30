from pico2d import *

open_canvas()

character = load_image('sprite_sheet.png')
background = load_image('TUK_GROUND.png')

def handle_events():

    global running, dir, move_x, move_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_w:
                move_y += 10
                dir = 'up'
            elif event.key == SDLK_a:
                move_x -= 10
                dir = 'left'
            elif event.key == SDLK_s:
                move_y -= 10
                dir = 'down'
            elif event.key == SDLK_d:
                move_x += 10
                dir = 'right'
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                move_y -= 10
            elif event.key == SDLK_a:
                move_x += 10
            elif event.key == SDLK_s:
                move_y += 10
            elif event.key == SDLK_d:
                move_x -= 10




    pass

def check_boundarie():
    global x, y
    if x - sprite_width // 2 < 0:
        x = sprite_width // 2

running = True
sprite_width = 163
sprite_height = 141
frame = 0
dir = 'down'
x, y = 400, 300
move_x, move_y = 0, 0
dir_rows = {'down' : 0, 'left' : 1, 'right' : 2, 'up' : 3}

while running:
    clear_canvas()
    background.clip_draw(0, 0, 1280, 1080, 400, 300, 800, 600)
    current_row = dir_rows[dir]
    character.clip_draw(frame * sprite_width, (3 - current_row) * sprite_height, sprite_width, sprite_height, x, y)

    x += move_x
    y += move_y

    check_boundarie()

    update_canvas()
    handle_events()

    frame = (frame + 1) % 3
    delay(0.1)
    pass


close_canvas()