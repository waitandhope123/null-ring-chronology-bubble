"""
Conceptual visualization of a rotating null (lightlike) ring.
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 400)
x = np.cos(theta)
y = np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y, linewidth=3, label="Null ring")

# Draw rotation arrows
for i in range(0, 360, 30):
    angle = np.deg2rad(i)
    plt.arrow(
        np.cos(angle),
        np.sin(angle),
        -0.2 * np.sin(angle),
        0.2 * np.cos(angle),
        head_width=0.05,
        length_includes_head=True
    )

plt.xlabel("x")
plt.ylabel("y")
plt.title("Rotating Null Stress–Energy Ring (Conceptual)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
