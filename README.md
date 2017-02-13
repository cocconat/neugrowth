Simple neurite growth 
====================

Discrete space simulator for neurite growth.
The environment is a 8bit values field where a self avoiding random walker moves

Simulation scheme:
-----------------
1. Set the environment: 
    * elements on the grid. Each neurite add itself to the grid when declared
    * Update grid: fieldCompute each cell in a range L from neurite's heads

2. Move each neurite:
    * Elements move with different dynamics defined in dynamic.py
    * Moves end up a cell, the cell is checked:
        1. It s occupied with a neurite -> implement synapse
        2. It s occupied from itself prevous points
        3. It s free

3. Update the field over the neurite's head, keeping only the minimum value for each cell, \
    should work

