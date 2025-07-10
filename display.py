import matplotlib.pyplot as plt
import numpy as np
import electricLoad as el

def display(temp, energy, load):
    time = list(range(len(temp)))

    fig, axs = plt.subplots(3,1, sharex=True, figsize=(10, 6))
    
    axs[0].plot(time, temp, color='red')
    axs[0].set_title("Water Temp Over Time")

    axs[1].plot(time, energy, color='blue')
    axs[1].plot(time, load, color='orange')
    axs[1].set_title("Energy released")

    plt.tight_layout()
    plt.show()