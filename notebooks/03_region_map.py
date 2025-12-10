"""
Radial structure of the Null Ring Chronology Bubble (conceptual).
"""

import matplotlib.pyplot as plt

regions = [
    ("Region D\nChronology Bubble", 0, 1.0),
    ("Region C\nChronology Horizon", 1.0, 1.4),
    ("Region B\nStrong Frame Drag", 1.4, 2.5),
    ("Region A\nAsymptotic Zone", 2.5, 4.0),
]

colors = ["red", "orange", "yellow", "green"]

fig, ax = plt.subplots(figsize=(6, 6))

for (label, r0, r1), color in zip(regions, colors):
    ax.barh(0, r1 - r0, left=r0, color=color, edgecolor="black")
    ax.text((r0 + r1)/2, 0, label, ha="center", va="center")

ax.set_xlim(0, 4)
ax.set_ylim(-0.5, 0.5)
ax.set_xlabel("Radial coordinate")
ax.set_yticks([])
ax.set_title("Conceptual NRCB Radial Structure")
plt.show()
