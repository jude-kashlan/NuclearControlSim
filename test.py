import math
import random
from reactor import Reactor

def test_min():
    sums = []
    consts = []
    for x in range(100):
        for y in range(100): 
            for z in range(100):
                sum = 0.0
                constList = [x/1000,y/1000,z/1000]
                new_reactor = Reactor(300,.5,constList[0],constList[1],constList[2])
                for i in range(50):
                    new_reactor.temp_log.append(new_reactor.update())
                    sum += abs(new_reactor.temp_log[-1]-600)
                sums.append(sum)
                consts.append(constList)
    return consts[sums.index(min(sums))]

