import time 

class Timer:

    def __init__(self, d_time):
        self.start_time = time.time()
        self.end = time.time()
        self.time_left = d_time
        self.duration_time = d_time
        

    def update_stop_time(self):
        current_time = time.time()
        self.time_left = self.duration_time - (current_time - self.start_time)
        if self.time_left < 0:
            self.time_left = 0
    
    # Calculates the elapsed time
    def elapsed_time_update(self):
        start = self.end
        self.end = time.time()
        return self.end - start
