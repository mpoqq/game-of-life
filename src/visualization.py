from state import State
from calculation import compute_next_generation
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class UpdateGrid(object):

    def __init__(self, im, grid, state):
        self.state = state
        self.im = im
        self.grid = grid

    def init(self):
        self.im.set_array([[]])
        return self.im,

    # update the grid
    def __call__(self, i):
        if self.state.value == State.STOP:
            plt.close()
        if not self.state.value == State.PAUSE and not self.state.value == State.WAIT:
            new_grid = compute_next_generation(self.grid)
            self.grid = new_grid
            self.im.set_array(self.grid)
            if self.state.value == State.STEPWISE:
                self.state.value = State.WAIT
        return self.im,


def visualize_grid(grid, speed, state, save):
    fig = plt.figure()
    # set color to white black -> gray
    viridis = plt.get_cmap('gist_gray', 10)
    newcolors = viridis(np.linspace(0, 1, 10))
    white = np.array([1, 1, 1, 1])
    newcolors[:1, :] = white
    newcmp = ListedColormap(newcolors[:5, :])

    im = plt.imshow(grid, animated=True, cmap=newcmp, vmin=0, vmax=5)
    ud = UpdateGrid(im, grid, state)
    ani = animation.FuncAnimation(fig, ud, frames=save[1], interval=speed.value, blit=True)
    # TODO fix the delay and show the saved frames also in the plot
    if save[0] is not None:
        ani.save(filename=save[0] + '.mp4')
    plt.show()
