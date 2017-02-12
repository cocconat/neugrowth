'''
environment class, create a grid of int values
'''

from environment import environment
from neurite import neurite
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--head', dest='headStart', nargs=2, type=int)
parser.add_argument('--size',  nargs='?',const=10,type=int,default=10)
parser.add_argument('--step',  nargs='?',const=10, type=int, default=10)
args=parser.parse_args()

headStart=tuple(args.headStart)
gridSize=args.size
step=args.step


if __debug__:
    print (args.headStart)
env=environment(gridSize)
axon=neurite('axon',gridSize,headStart)

for i in range(step):
    axon.move()

if __debug__:
    print(axon.points)
env.neuriteToGrid(axon)
env.plotGrid()
