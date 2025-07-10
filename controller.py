"""PID Controller"""
import electricLoad as el

def height_update(temp_log, target_temp, kp, ki, kd):
    error = target_temp - temp_log[-1]
    new_height = kp*error - ki*(sum(temp_log) - target_temp*len(temp_log)) + kd*(temp_log[-2]-temp_log[-1])
    return max(0,min(1.0,new_height))

def flow_update(heat_loss, kp, ki, kd,I , t, load):
    error = load[t-1] - heat_loss[-1]
    I += error
    D = (load[t-1]-heat_loss[-1]) - (load[t-2]-heat_loss[t-2])
    flow = kp*error + ki*I + kd*D #find way to include derivative
    # print(error,I,D,sep='\t')
    return max(0,min(1.0,flow))