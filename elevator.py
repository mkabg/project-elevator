from settings import *
from timer import *


class Elevator:
    def __init__(self, x, y, floor):
        self.orders = []
        self.x = x
        self.y = y
        self.current_floor = floor 
        self.stop_time = Timer(0) # Timer for the waiting time on the floor
        self.wait_in_floor = False # Elevator waiting time on the floor
        self.in_use = False # Elevator in moving or in waiting time on the floor
        img_elev = pygame.image.load(IMG_ELEVATOR)
        self.img_elev = pygame.transform.scale(img_elev, (ELEV_WIDTH, ELEV_HEIGHT))

    # Calculates the time it will take for the elevator to reach the floor we received as a parameter
    def calc_elev_time(self, floor):
        if not self.orders: # order empty
            elev_time = self.calc_time(self.current_floor, floor)
            if not self.in_use: # If elevator is not in use
                return elev_time
            else:
                return elev_time + ELEVATOR_STOP_TIME - self.stop_time.time_left
        last_order = self.orders[-1]
        return self.calc_time(last_order, floor) + ELEVATOR_STOP_TIME
 
    # Time calculation of distance between floors
    def calc_time(self, current_floor, dest_floor):
        floor_distance = abs(current_floor.floor_number - dest_floor.floor_number)
        return floor_distance * SPEED_ELEVATOR + current_floor.timer.reaching_time 


    def update_elevator(self):
        if self.stop_time.time_left > 0: 
            self.stop_time.update_stop_time() # update the time left to the elevator waiting in the floor 
        if self.in_use:
            if self.current_floor.timer.reaching_time <= 0 and not self.wait_in_floor: # check if elevator come to floor then wait 2 secoend on the floor
                pygame.mixer.Sound(DING).play()
                self.stop_time = Timer(ELEVATOR_STOP_TIME) # start timer of 2 second
                self.wait_in_floor = True 
            if self.wait_in_floor and self.stop_time.time_left <= 0: # check if elevator finish waiting time in floor
                self.wait_in_floor = False
                self.in_use = False # free elevator
                self.current_floor.free_floor()
        if self.orders:
            if self.current_floor.timer.reaching_time <= 0 and not self.in_use: # check if elevator free to move 
                self.current_floor.free_floor()
                self.current_floor = self.orders.pop(0)
                self.in_use = True


    def update_position(self, elapsed_time):
        # update location y of the elevator 
        target_y = self.current_floor.y
        distance = target_y - self.y
        max_move = FLOOR_HEIGHT * elapsed_time / 0.5  # Maximum distance to move this frame
        if abs(distance) <= max_move:
            self.y = target_y  # If we're close enough, snap to the target
        else:
            direction = 1 if distance > 0 else -1
            self.y += direction * max_move


    def draw_elevator(self, screen):
        screen.blit(self.img_elev, (self.x, self.y))
    
