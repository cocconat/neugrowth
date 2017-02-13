'''
enviroment class, create a grid of int values
'''

import numpy as np
import logging
logger = logging.getLogger(__name__)
from geometry import neighbors, updatePBC,computeDistance
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
        n=7
        xarea= np.arange(-n+1,n,1,dtype=np.int8)
        yarea= np.arange(-n+1,n,1,dtype=np.int8)
        #logger.debug("selected area\n {},\n {}".format(xarea,yarea))
        xx,yy=np.meshgrid(xarea,yarea,copy=False)
        assert xx.dtype==np.int8
        distance=computeDistance(xx,yy)
        logger.debug('computed distance matrix:\n\
                     matrix shape is {} \n \
                     matrix itself itself is {}\
                     '.format(distance.shape,distance))
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
            assert neurite.head
            headToGrid(self, neurite.head)
            if (neurite.element=='dendrite'):
                self.computeField(neurite.head)

#    def searchNeurite(self,point):
#        '''
#        set all points belonging to neurite to 7
#        periodic boundary condition are implemented
#        '''
#        for x,y in neurite.points:
#            self.grid[x%self.size,y%self.size]=7



