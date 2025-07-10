from reactor import Reactor
import controller

class unidealReactor(Reactor):
    def __init__(self, temp,init_rod_height, kp, ki, kd, max_speed=.2, delay=1):
        super().__init__(temp,init_rod_height, kp, ki, kd)
        self.max_speed = max_speed
        self.delay = delay
        self.temporary = 0.5

    def update(self):
        self.exchange_heat()
        if abs(self.temporary - self.control_rod_height) < .2:
            self.control_rod_height = self.temporary
        else:
            self.control_rod_height += max(-1*self.max_speed,min(self.max_speed,self.temporary - self.control_rod_height))
        self.temporary = controller.height_update(self.temp_log, 600, self.kp, self.ki, self.kd)
        return self.rod_temp

    
        