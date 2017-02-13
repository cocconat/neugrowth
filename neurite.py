from geometry import difference2D,sum2D
import logging
import dynamics
logger = logging.getLogger(__name__)
class neurite():
    '''
    neurite element
    init values:
        str _type
        (x,y) head starting position
        int gridSize PBC implemented
    '''
    def __init__(self,_type,gridSize,env,head=(0,0)):
        logger.info("a {} neurite has been created".format(_type))
        self.element=_type
        if head:
            self.head=head
        else:
            self.head=(0,0)
        self.points=[self.head]
        self.gridSize=gridSize
        self.avoidPoints=[]
        self.env=env
        self.env.addNeurite(self)
    def setHeadPosition(self,x,y):
        self.head=(x,y)

    def chooseDirection(self):
        '''
        this function choose the next cell of the neurite,
        it s the function which interacts with the environment
        cell with 7 are forbidden
             x=random.choice([self.head[0]+i for i in [-1,0,1]])
            y=random.choice([self.head[1]+i for i in [-1,0,1]])
        '''
        dx,dy=difference2D(self.head,self.points[-1])
        if self.element=='dendrite':
            dx,dy=dynamics.quasiRandomDynamic(dx,dy)
        if self.element=='axon':
            dx,dy=dynamics.fieldAttractive(self.head,self.env)
        logger.debug("next step has direction {}".format(dx,dy))
        return dx,dy
    def move(self):
        '''
        self avoiding moving is implemented, the standing move is allowed
        '''
        (x,y)=sum2D(self.chooseDirection(),self.head)
        #pbc implemented
        (x,y)=(x%self.gridSize,y%self.gridSize)
        if (self.env.freeCell((x,y))):
            logging.critical("synapse to be implemented!")
        if ((x,y) in self.points):
            logging.critical("backwarding move")
        logger.debug("next head position in {}".format((x,y)))
        if self.head!=(x,y):
            self.points.append(self.head)
            self.head=(x,y)
        #if __debug__:
        #    print ("head in {}".format(self.head))


#class branch():

