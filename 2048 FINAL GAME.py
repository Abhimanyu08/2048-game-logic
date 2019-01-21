"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSET = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    added  = False
    new_line = len(line)*[0]
    for ite in line:
        if ite == 0:
            continue
        elif sum(new_line) == 0:
            new_line[0] = ite
        else:
            if ite == new_line[new_line.index(0) - 1] and not added:
                    new_line[new_line.index(0) -1] += ite
                    added = True
            else:
                new_line[new_line.index(0)] = ite
                added  = False
            
    return new_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grh = grid_height
        self._grw = grid_width
        self.reset()
        self._map = {UP: [(0,dummy_idx) for dummy_idx in range(self._grw)],
                     DOWN: [(self._grh-1,dummy_idx) for dummy_idx in range(self._grw)],
                     LEFT: [(dummy_idx,0) for dummy_idx in range(self._grh)],
                     RIGHT: [(dummy_idx,self._grw-1) for dummy_idx in range(self._grh)]}
        self._smap = {UP: self._grh,DOWN: self._grh,LEFT:self._grw,RIGHT:self._grw}
                          
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[0 for dummy_idx in range(self._grw)] for dummy_jdx in range(self._grh)]
        self.new_tile()
        self.new_tile()
         

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        stri = ""
        for idx in range(self._grh):
            stri += str(self._grid[idx]) + '\n'
        return stri

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grh

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grw

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        changed = False
        for idx in self._map[direction]:
            lst= [(idx[0]+dummy_jdx*OFFSET[direction][0],idx[1]+ dummy_jdx*OFFSET[direction][1]) for dummy_jdx in range(self._smap[direction])]
            temp = [self._grid[lst[dummy_idx][0]][lst[dummy_idx][1]] for dummy_idx in range(len(lst))]
            merged = merge(temp)
            if merged != temp:
                changed = True
                for jdx in range(len(merged)):
                    self._grid[lst[jdx][0]][lst[jdx][1]] = merged[jdx]
        if changed:
            self.new_tile()
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        tiles = [2,2,2,2,2,2,2,2,2,4]
        found = False
        
        while not found:
            idx = random.choice(range(self._grh))
            jdx = random.choice(range(self._grw))
            if self._grid[idx][jdx] == 0:
                self._grid[idx][jdx] = random.choice(tiles)
                found = True
            else:
                continue
                     

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
