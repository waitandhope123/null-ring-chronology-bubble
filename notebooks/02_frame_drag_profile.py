"""
Conceptual profile of frame-dragging strength versus radius.
Values are illustrative only.
"""

import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(1, 20, 400)
drag = 1 / r**3

critical = 0.05

plt.figure(figsize=(7, 4))
plt.plot(r, drag, label="Frame-dragging strength")
plt.axhline(critical, linestyle="--", label="Chronology threshold")

plt.xlabel("Radius (arbitrary units)")
plt.ylabel("Frame-dragging strength")
plt.title("Conceptual Frame Dragging vs Radius")
plt.legend()
plt.grid(True)
plt.show()
