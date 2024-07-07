from settings import *
from button import *
from floor import *
from timer import *
from elevator import *
import time

class Building:
    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.num_elevators = num_elevators
        self.floors = []
        self.elevators = []
        self.init_floors()
        self.init_elevators()
        self.time = Timer(time.time())


    # Initializing an array of floors
    def init_floors(self):
        location_y = WINDOW_WIDTH - FLOOR_HEIGHT
        for num_floor in range(self.num_floors):
            button = Button(LOCATION_X_FLOOR, location_y + ADD_TO_Y, WIDTH_BUTTON, HEIGHT_BUTTON, str(num_floor), FONT_BUTTON, GRAY, BLACK)
            self.floors.append(Floor(num_floor, LOCATION_X_FLOOR, location_y, button))
            location_y -= FLOOR_HEIGHT
    

    # Initializing an array of elevator
    def init_elevators(self):          
        x = FLOOR_WIDTH + ADD_TO_LOCAYION_X
        for _ in range(self.num_elevators):
            self.elevators.append(Elevator(x, ELEV_LOCATION_Y, self.floors[0]))
            x += ELEV_WIDTH
    
    # draw the floor and the elevator
    def draw_building(self, screen):
        for floor in self.floors:
            floor.draw_floor(screen)
        for elevator in self.elevators:
            elevator.draw_elevator(screen)

        
    # Calculates the minimum time of an elevator to this floor
    def elevator_controller(self, floor):
        min_time = float('inf')
        for index, elevator in enumerate(self.elevators):
            time_elev = elevator.calc_elev_time(floor)
            if time_elev < min_time:
                min_time = time_elev
                min_idx = index
        if not floor.is_pressed:
            floor.is_pressed = True
            floor.timer.reaching_time = min_time
            self.elevators[min_idx].orders.append(floor)

    
    def update_building(self):
        self.time.elapsed_time = self.time.elapsed_time_update() # calculate the timer and the elevator moovmenet the time that past 
        for floor in self.floors:
            floor.update_floor(self.time.elapsed_time)
        for elevator in self.elevators:
            elevator.update_elevator() # Updates the status of the elevator
            elevator.update_position(self.time.elapsed_time)
    

    # Manages the game of elevators
    def run_game(self):
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("building") # the name of the screen
        run = True
        while run:
            screen.fill(WHITE)
            self.update_building()
            self.draw_building(screen)  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # check if floor is pressed
                for floor in self.floors:
                    if floor.button.is_clicked(event): 
                        if not floor.is_pressed: # if floor isn't pressed invite elevator to floor
                            self.elevator_controller(floor)
            pygame.display.update()
        pygame.quit()



