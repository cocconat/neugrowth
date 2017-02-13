'''
environment class, create a grid of int values
'''

from environment import environment
from neurite import neurite
import graphic
import argparse,logging
logger = logging.getLogger(__name__)

def parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--head', dest='headStart', nargs=2, type=int)
    parser.add_argument('--size',  nargs='?',const=10,type=int,default=10)
    parser.add_argument('--step',  nargs='?',const=10, type=int, default=10)
    parser.add_argument('--log',type=str, default='info')
    return parser

args=parse().parse_args()
#logging setting
##############################################
LEVELS = { 'debug':logging.DEBUG,
            'info':logging.INFO,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'critical':logging.CRITICAL,
                      }
logging.basicConfig(level=LEVELS[args.log])
logger = logging.getLogger("MAIN")
fh = logging.FileHandler("new_snake.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
##############################################

headStart=tuple(args.headStart)
gridSize=args.size
step=args.step

logger.info("simulation is starting")
env=environment(gridSize)
axon=neurite('axon',gridSize,env,headStart)
dendrite=neurite('dendrite',gridSize,env,(50,50))
env.addNeurite(axon)
env.addNeurite(dendrite)
for elems in env.neurites:
    logger.debug("neurit {} has head in {}".format(elems.element,headStart))

env.update()

for i in range(step):
    for elems in env.neurites:
        elems.move()
    env.update()
#    if i%20==0:
#        graphic.plotGrid(env,False)

logger.debug("neurite {} points in {}".format(axon.element,axon.points))
logger.debug("the axon did {} steps".format(len(axon.points)))
graphic.plotGrid(env)
