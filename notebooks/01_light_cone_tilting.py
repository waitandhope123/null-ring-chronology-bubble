"""
Conceptual visualization of light cone tilting due to rotation/frame dragging.
This is NOT a GR calculation — it is a geometric illustration only.
"""

import numpy as np
import matplotlib.pyplot as plt

def draw_light_cone(ax, tilt=0.0, height=1.0):
    t = np.linspace(0, height, 100)
    left = -t + tilt * t
    right = t + tilt * t

    ax.plot(left, t, color='black')
    ax.plot(right, t, color='black')

fig, axes = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

tilts = [0.0, 0.3, 0.7, 1.2]
titles = ["Normal spacetime", "Frame dragging", "Near-critical", "CTC possible"]

for ax, tilt, title in zip(axes, tilts, titles):
    draw_light_cone(ax, tilt=tilt)
    ax.set_title(title)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0, 1.2)
    ax.set_xlabel("Space")
    ax.set_aspect("equal")
    ax.grid(True)

axes[0].set_ylabel("Time")

plt.suptitle("Conceptual Light Cone Tilting")
plt.tight_layout()
plt.show()
