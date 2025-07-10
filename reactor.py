import controller
import math
import random

class Reactor:
   
   def __init__(self, temp,init_rod_height, kp, ki, kd, bad_weather, load):
      self.water_temp = temp
      self.control_rod_height = init_rod_height
      self.rod_temp = 350
      self.temp_log = [290,290]
      self.kp = kp
      self.ki = ki
      self.kd = kd
      self.secondary_temp = 175
      self.flow_rate = 1.0
      self.bad_weather = bad_weather
      self.heat_loss_log = [10,10]
      self.I = float()
      self.heat_loss = float()
      self.load = load

   def __str__(self):
       return f"Rods: {self.rod_temp}\tContr ht: {self.control_rod_height}\tWr temp: {self.water_temp}\tSec temp: {self.secondary_temp}\tflow: {self.flow_rate}"
   
   def exchange_heat(self):
       self.water_temp += .15*(self.rod_temp-self.water_temp)
       self.rod_temp += self.control_rod_height*25 - .15*(self.rod_temp - self.water_temp)

   def check_outside_temp(self):
       if self.bad_weather:
           return 100*math.sin(len(self.temp_log)/4)
       else:
           return 25
       
   def exchange_secondary(self):
       temp_diff = self.water_temp - self.secondary_temp
       heat_transfer = temp_diff * self.flow_rate * .1 # exchange constant
       self.heat_loss = 0.2*(self.secondary_temp - self.check_outside_temp())*self.flow_rate
       self.heat_loss_log.append(self.heat_loss)
       self.secondary_temp += heat_transfer - self.heat_loss  # let off into environment
       self.water_temp -= heat_transfer
   
   def update(self):
        self.exchange_heat()
        self.exchange_secondary()
        self.control_rod_height = controller.height_update(self.temp_log, 300, self.kp, self.ki, self.kd)
        self.temp_log.append(self.water_temp)
        kp = .04
        ki = .0014
        kd = 0.0001
        self.I += self.load[len(self.temp_log)-1] - self.heat_loss_log[-1]
        self.flow_rate = controller.flow_update(self.heat_loss_log,kp,ki,kd,self.I,len(self.temp_log), self.load)

   
   
            


        


