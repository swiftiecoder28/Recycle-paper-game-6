import random
import pgzrun

WIDTH = 900
HEIGHT = 800
TITLE = "Recycle paper game"
center_x = WIDTH// 2
center_y = HEIGHT// 2
center = (center_x, center_y)
final_level = 8
start_speed = 10
ITEMS = ["bag", "battery", "bottle", "chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def select_items(num_of_extra_items):
    items_to_create = ["paper"]
    for i in range(num_of_extra_items):
        random_items = random.choice(ITEMS)
        items_to_create.append(random_items)
    return items_to_create

def create_actors(items_to_create):
    new_items = []
    for item in items_to_create:
        new_actor = Actor(item + "img")
        new_items.append(new_actor)
    return new_items

def layout_actors(items_to_layout):
    num_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH // num_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_position = gap_size *(index + 1)
        item.x = new_x_position


def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = start_speed - current_level
        item.anchor = ("center", "bottom")
        animation = animate(item, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)


def make_items(num_of_extra_items):
    items_to_create = select_items(num_of_extra_items)
    new_items = create_actors(items_to_create)
    layout_actors(new_items)
    animate_items(new_items)
    return new_items

def handle_game_over():
    global game_over
    game_over = True

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation. running:
            animation.stop()


def handle_game_complete():
    global items, current_level, animations, game_complete
    stop_animations(animations)
    if current_level == final_level:
        game_complete = True
    else:
        current_level += 1 
        items = []
        animations = []

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()


def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("Game over", "Try again next time.")
    elif game_complete:
        display_message("You win!", "Good job:)")
    else:
        for item in items:
            item.draw()

def display_message(main_msg, sub_msg):
    screen.draw.text(main_msg, fontsize = 60, color = "black", center = (center_x, center_y))
    screen.draw.text(sub_msg, fontsize = 30, color = "black", center = (center_x, center_y + 30))
    

def update():
    global items
    if len (items) == 0 :
        items = make_items(current_level)
    




pgzrun.go()

