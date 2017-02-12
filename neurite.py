
import numpy as np
import random

class neurite():
    '''
    neurite element
    init values:
        str _type
        (x,y) head starting position
        int gridSize PBC implemented
    '''
    def __init__(self,_type,gridSize,head=(0,0)):
        self.element=_type
        if head:
            self.head=head
        else:
            self.head=(0,0)
        self.points=[self.head]
        self.gridSize=gridSize
        self.avoidPoints=[]

    def setHeadPosition(self,x,y):
        self.head=(x,y)

    def avoidPath(self,point):
        self.avoidPoints.append(point)

    def move(self):
        '''
        self avoiding moving is implemented, the standing move is allowed
        '''
        while True:
            x=random.choice([self.head[0]+i for i in [-1,0,1]])
            y=random.choice([self.head[1]+i for i in [-1,0,1]])
            if ((x,y) not in self.avoidPoints):
                break
        if self.head!=(x,y):
            self.points.append(self.head)
            self.head=(x%self.gridSize,y%self.gridSize)
            self.avoidPath(self.points[-1])

        if __debug__:
            print ("head in {}".format(self.head))
