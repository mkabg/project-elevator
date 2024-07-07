from settings import *
from show_timer import *
from button import *

class Floor:

    def __init__(self, floor_number, x, y, button): 
        self.floor_number = floor_number
        self.x = x
        self.y = y
        self.button = button
        # In the begin of the game all elevator is in floor 0, so variable is_preesed = True 
        if self.floor_number == 0:
            self.is_pressed = True
        else:
            self.is_pressed = False
        self.timer = ShowTimer(self.x, self.y) # Timer for the arrival time of the elevator to the floor
        img_floor = pygame.image.load(FLOOR_IMG)
        self.img_floor = pygame.transform.scale(img_floor, (FLOOR_WIDTH, FLOOR_HEIGHT)) # Set the size of the floor image


    # Draw the floor
    def draw_floor(self, screen):
        screen.blit(self.img_floor, (self.x, self.y))
        self.draw_line(screen)
        self.timer.draw_timer(screen)
        self.button.draw_button(screen)


    # draw black line on floor expect of the last floor
    def draw_line(self, screen):
        if self.floor_number != NUM_FLOORS - 1:
            pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + FLOOR_WIDTH, self.y), LINE_HEIGHT)

    #
    def update_floor(self, elapsed_time):
        self.update_button_color()
        self.timer.update_timer(elapsed_time) # Updates the time left for the elevator to arrive

    # check if need to change the button color
    def update_button_color(self):
        if self.timer.reaching_time > 0:
            self.button.color = GREEN
        else:
            self.button.color = GRAY

    # if not elevator in floor
    def free_floor(self):
        self.is_pressed = False


