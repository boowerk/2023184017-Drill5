from pico2d import *

open_canvas()

character = load_image('sprite_sheet.png')
background = load_image('TUK_GROUND.png')

def handle_events():
    pass

running = True

while running:
    clear_canvas()
    update_canvas()
    handle_events()
    pass


close_canvas()