import reactor as r
import unidealReactor as ur
import display
import test
import electricLoad as el

# init the reactor object and data storage
kp = .013
ki = 0.002
kd = 0.03
bad_weather = False
sim_duration = 500
load = [10,10] + [el.elec_load(t) for t in range(0, sim_duration)]
rct = r.Reactor(290,.5, kp, ki, kd, bad_weather, load)
# print(test.test_min())

# simulate iterations
for num in range(0,sim_duration):
    rct.update()
    print(rct)

# display results
display.display(rct.temp_log, rct.heat_loss_log, load)
