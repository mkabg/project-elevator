from settings import *


class ShowTimer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reaching_time = 0
        self.rect = pygame.Rect(x, y, RECT_WIDTH_FOR_TIMER, RECT_HEIGHT_FOR_TIMER)
        self.font = FONT_TIME
        
    # Calculates the time left for the elevator to reach the floor
    def update_timer(self, elapsed_time):
        if self.reaching_time > 0:
            self.reaching_time -= elapsed_time


    def draw_timer(self, screen):
        if self.reaching_time > 0: # If timer isn't over draw the timer
            timer_str = f'{round(self.reaching_time, 1):.1f}' # format time
            text = self.font.render(timer_str, True, BLACK)
            screen.blit(text, (TIMER_X,  self.y + ADD_Y))
