'''
enviroment class, create a grid of int values
'''

import numpy as np
import matplotlib.pyplot as plt

class environment ():
    '''
    environment class,
    each point is a np.int8
    initial values are [0...0]
    '''
    def __init__(self,N):
        self.grid= np.zeros((N,N),dtype=np.int8)
        self.size=N
    def setZero(self):
        '''
        set the whole grid to zero
        '''
        self.grid[:,:]=0
    #def update()
    def neuriteToGrid(self,neurite):
        '''
        set all points belonging to neurite to 7
        periodic boundary condition are implemented
        '''
        for x,y in neurite.points:
            self.grid[x%self.size,y%self.size]=7
    def plotGrid(self):
        '''
        plot an heatmap of the grid
        '''
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(self.grid)
        plt.show()
