import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2*np.pi, 800)

def heart(t):
    x = 16 * np.sin(t)**3
    y = (13 * np.cos(t)
         - 5 * np.cos(2*t)
         - 2 * np.cos(3*t)
         - np.cos(4*t))
    return x, y

x, y = heart(t)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor("black")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

lines = []
colors = ["#ff1a1a", "#ff4d4d", "#ff8080"]
widths = [3, 2, 1]

for c, w in zip(colors, widths):
    line, = ax.plot([], [], color=c, lw=w, alpha=0.8)
    lines.append(line)

def animate(frame):
    angle = frame * 0.08
    for i, line in enumerate(lines):
        a = angle - i * 0.15
        xr = x * np.cos(a) - y * np.sin(a)
        yr = x * np.sin(a) + y * np.cos(a)
        line.set_data(xr, yr)
    return lines

ani = FuncAnimation(fig, animate, frames=300, interval=40)
ani.save("heart.mp4", fps=30)
