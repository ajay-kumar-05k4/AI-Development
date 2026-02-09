import numpy as np
import math
import matplotlib.pyplot as plt

def show(img, title="image", cmap="gray"):
    fig, ax = plt.subplots()
    ax.imshow(img, cmap=cmap, interpolation="nearest")
    ax.set_title(title)
    ax.axis("off")
    plt.show()

def checkerboard(n=8, tile=1):
    y = np.arange(n)[:, None]
    x = np.arange(n)[None, :]
    pattern = (x//tile + y//tile) % 2
    return (pattern * 255).astype(np.uint8)


img = checkerboard(8)
show(img, "Original")
