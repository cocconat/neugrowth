import random
import geometry
import logging
import numpy as np

logger = logging.getLogger(__name__)
#logger.setLevel(10)

def quasiRandomDynamic(dx,dy):
    '''
    keep the direction on almost 1 ax
    move following inertia
    '''
    changeDir=random.choice(['dx','dy',None,None,None,None,None,None])
    if changeDir=='dx':
        dx=random.choice([-1,0,1])
    if changeDir=='dy':
        dy=random.choice([-1,0,1])
    return dx,dy

def fieldAttractive(head,env):
    '''
    move towards minimal potential cells
    '''
    x,y=head
    local=geometry.neighbors(env.grid,x,y,1)-1
    assert local.dtype==np.int8
    x,y= np.unravel_index(local.argmax(), local.shape)
    logger.debug("field attrractive matrix is:\n {}\
                 and the maximum is in {}".format(local,(x-1,y-1)))
    return x-1,y-1

def fieldRepulsive(head,env):
    return True

