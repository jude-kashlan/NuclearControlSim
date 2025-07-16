import math
import random

def elec_load(t):
    return 11 + 8*abs(math.sin(t/(10*math.pi))) + 2*random.random()