'''
enviroment class, create a grid of int values
'''

import numpy as np
import matplotlib.pyplot as plt
import logging
logger = logging.getLogger(__name__)
from geometry import neighbors, updatePBC
class environment ():
    '''
    environment class,
    each point is a np.int8
    initial values are [0...0]
    Each elemnt has to be added to the environment in order its steps are tracked
    '''
    def __init__(self,N):
        logger.debug("A new environment is created")
        self.grid= np.zeros((N,N),dtype=np.int8)
        self.size=N
        self.neurites=[]
    def setZero(self):
        '''
        set the whole grid to zero
        '''
        self.grid[:,:]=0
    #def update()
    def freeCell(self,point):
        '''
        verify cell is free from neurites
        point = (x,y) tuple and returns bool
        '''
        if self.grid[point[0],point[1]] != 7:
            return True
        else:
            return False
    def addNeurite(self,neurite):
        '''
        add the neurite elemnent to the environment
        '''
        self.neurites.append(neurite)
        logger.info("{} in enviroment ".format(neurite.element))

    def computeField(self,head):
        logger.debug("computing field")
        x,y = head
        ## interaction range
        n=5
        xarea= np.arange(x-n+1,x+n,1)
        yarea= np.arange(y-n+1,y+n,1)
        #logger.debug("selected area\n {},\n {}".format(xarea,yarea))
        xx,yy=np.meshgrid(xarea,yarea)
        distance=int(7/((xx-x)**2+(yy-y)**2))
        logger.debug("computed distance is {}".format(distance))
        update=np.maximum(neighbors(self.grid,x,y,n-1),distance)
        self.grid=updatePBC(self.grid,update,x,y,n-1)

    def update(self):
        '''
        update the grid with elements on it:
            all the elements in self.neurites are computed
        this function is a base part of the program since it update
        the environment to allow the neurites to interact.
        '''
        def headToGrid(self,head):
            self.grid[head[0],head[1]]=7
        logger.debug("environment updating")
        for neurite in self.neurites:
            headToGrid(self, neurite.head)
            self.computeField(neurite.head)

#    def searchNeurite(self,point):
#        '''
#        set all points belonging to neurite to 7
#        periodic boundary condition are implemented
#        '''
#        for x,y in neurite.points:
#            self.grid[x%self.size,y%self.size]=7



    def plotGrid(self):
        '''
        plot an heatmap of the grid
        '''
        fig, ax = plt.subplots()
        ax.pcolor(self.grid)
        plt.show()
