import matplotlib.pyplot as plt
import time
import random

packets = []

plt.ion()

while True:
    # Simulated data (replace later with real logs if needed)
    packets.append(random.randint(1, 50))

    if len(packets) > 20:
        packets.pop(0)

    plt.clf()
    plt.title("📊 Live Traffic Monitoring")
    plt.xlabel("Time")
    plt.ylabel("Packets")
    plt.plot(packets)

    plt.pause(1)
