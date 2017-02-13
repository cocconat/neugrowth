import matplotlib.pyplot as plt

def plotGrid(env,keep=True):
    '''
    plot an heatmap of the grid
    '''
    plt.ion()
    fig, ax = plt.subplots()
    ax.pcolor(env.grid)
    plt.pause(0.05)
    ax.set_ylim(ax.get_ylim()[::-1])        # invert the axis
    ax.set_xlim(ax.get_xlim()[::-1])        # invert the axis

    while keep:
        plt.pause(0.05)

