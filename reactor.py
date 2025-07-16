import controller
import math


class Reactor:
   
   def __init__(self, temp,init_rod_height, kp, ki, kd, bad_weather, load):
      """initialize the variables of the reactor"""
      self.water_temp = temp
      self.control_rod_height = init_rod_height
      self.rod_temp = 350 #init fuel rod temp
      self.temp_log = [temp, temp]
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
      self.sec_kp = .04
      self.sec_ki = .0014
      self.sec_kd = 0.0001

   def __str__(self):
       """Return important attributes of the reactor as a string"""
       return f"Rods: {self.rod_temp}\tContr ht: {self.control_rod_height}\tWr temp: {self.water_temp}\tSec temp: {self.secondary_temp}\tflow: {self.flow_rate}"
   
   def exchange_heat(self):
       """Exchange heat between the fuel rods and the primary water, rods gain heat based on ctrl height"""
       self.water_temp += .15*(self.rod_temp-self.water_temp)
       self.rod_temp += self.control_rod_height*25 - .15*(self.rod_temp - self.water_temp)

   def check_outside_temp(self):
       """Changes ability to release heat based on temp swings"""
       if self.bad_weather:
           return 100*math.sin(len(self.temp_log)/4)
       else:
           return 25
       
   def exchange_secondary(self):
       """Simulates heat exchange between the primary and secondary loops"""
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

        self.I += self.load[len(self.temp_log)-1] - self.heat_loss_log[-1]
        self.flow_rate = controller.flow_update(self.heat_loss_log,self.sec_kp, self.sec_ki,self.sec_kd,self.I,len(self.temp_log), self.load)

   
   
            


        


