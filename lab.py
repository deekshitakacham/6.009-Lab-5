#!/usr/bin/env python3
"""6.009 Lab -- Six Double-Oh Mines"""

# NO IMPORTS ALLOWED!

def dump(game):
    """
    Prints a human-readable version of a game (provided as a dictionary)
    """
    for key, val in sorted(game.items()):
        if isinstance(val, list) and val and isinstance(val[0], list):
            print(f'{key}:')
            for inner in val:
                print(f'    {inner}')
        else:
            print(f'{key}:', val)


# 2-D IMPLEMENTATION


def new_game_2d(num_rows, num_cols, bombs):
    """
    Start a new game.

    Return a game state dictionary, with the 'dimensions', 'state', 'board' and
    'mask' fields adequately initialized.

    Parameters:
       num_rows (int): Number of rows
       num_cols (int): Number of columns
       bombs (list): List of bombs, given in (row, column) pairs, which are
                     tuples

    Returns:
       A game state dictionary

    >>> dump(new_game_2d(2, 4, [(0, 0), (1, 0), (1, 1)]))
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    mask:
        [False, False, False, False]
        [False, False, False, False]
    state: ongoing
    """
#    board = []
#    for r in range(num_rows):
#        row = []
#        for c in range(num_cols):
#            if [r,c] in bombs or (r,c) in bombs:
#                row.append('.')
#            else:
#                row.append(0)
#        board.append(row)
#    mask = []
#    for r in range(num_rows):
#        row = []
#        for c in range(num_cols):
#            row.append(False)
#        mask.append(row)
#    for r in range(num_rows):
#        for c in range(num_cols):
#            if board[r][c] == 0:
#                neighbor_bombs = 0
#                if 0 <= r-1 < num_rows:
#                    if 0 <= c-1 < num_cols:
#                        if board[r-1][c-1] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r < num_rows:
#                    if 0 <= c-1 < num_cols:
#                        if board[r][c-1] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r+1 < num_rows:
#                    if 0 <= c-1 < num_cols:
#                        if board[r+1][c-1] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r-1 < num_rows:
#                    if 0 <= c < num_cols:
#                        if board[r-1][c] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r < num_rows:
#                    if 0 <= c < num_cols:
#                        if board[r][c] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r+1 < num_rows:
#                    if 0 <= c < num_cols:
#                        if board[r+1][c] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r-1 < num_rows:
#                    if 0 <= c+1 < num_cols:
#                        if board[r-1][c+1] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r < num_rows:
#                    if 0 <= c+1 < num_cols:
#                        if board[r][c+1] == '.':
#                            neighbor_bombs += 1
#                if 0 <= r+1 < num_rows:
#                    if 0 <= c+1 < num_cols:
#                        if board[r+1][c+1] == '.':
#                            neighbor_bombs += 1
#                board[r][c] = neighbor_bombs
#    return {
#        'dimensions': (num_rows, num_cols),
#        'board' : board,
#        'mask' : mask,
#        'state': 'ongoing'}
    
    dimensions = (num_rows, num_cols)
    return new_game_nd(dimensions, bombs)




def dig_2d(game, row, col):
    """
    Reveal the cell at (row, col), and, in some cases, recursively reveal its
    neighboring squares.

    Update game['mask'] to reveal (row, col).  Then, if (row, col) has no
    adjacent bombs (including diagonally), then recursively reveal (dig up) its
    eight neighbors.  Return an integer indicating how many new squares were
    revealed in total, including neighbors, and neighbors of neighbors, and so
    on.

    The state of the game should be changed to 'defeat' when at least one bomb
    is visible on the board after digging (i.e. game['mask'][bomb_location] ==
    True), 'victory' when all safe squares (squares that do not contain a bomb)
    and no bombs are visible, and 'ongoing' otherwise.

    Parameters:
       game (dict): Game state
       row (int): Where to start digging (row)
       col (int): Where to start digging (col)

    Returns:
       int: the number of new squares revealed

    >>> game = {'dimensions': (2, 4),
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'mask': [[False, True, False, False],
    ...                  [False, False, False, False]],
    ...         'state': 'ongoing'}
    >>> dig_2d(game, 0, 3)
    4
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    mask:
        [False, True, True, True]
        [False, False, True, True]
    state: victory

    >>> game = {'dimensions': [2, 4],
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'mask': [[False, True, False, False],
    ...                  [False, False, False, False]],
    ...         'state': 'ongoing'}
    >>> dig_2d(game, 0, 0)
    1
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: [2, 4]
    mask:
        [True, True, False, False]
        [False, False, False, False]
    state: defeat
    """
    
    coordinate = (row, col)
    return dig_nd(game, coordinate)

#    if game['state'] == 'defeat' or game['state'] == 'victory':
#        game['state'] = game['state']  # keep the state the same
#        return 0
#
#    if game['board'][row][col] == '.':
#        game['mask'][row][col] = True
#        game['state'] = 'defeat'
#        return 1
#
#    bombs = 0
#    covered_squares = 0
#    for r in range(game['dimensions'][0]):
#        for c in range(game['dimensions'][1]):
#            if game['board'][r][c] == '.':
#                if  game['mask'][r][c] == True:
#                    bombs += 1
#            elif game['mask'][r][c] == False:
#                covered_squares += 1
#    if bombs != 0:
#        # if bombs is not equal to zero, set the game state to defeat and
#        # return 0
#        game['state'] = 'defeat'
#        return 0
#    if covered_squares == 0:
#        game['state'] = 'victory'
#        return 0
#
#    if game['mask'][row][col] != True:
#        game['mask'][row][col] = True
#        revealed = 1
#    else:
#        return 0
#    
#    
#    num_rows, num_cols = game['dimensions']
#    
#        
#
#    if game['board'][row][col] == 0:
#        num_rows, num_cols = game['dimensions']
#        if 0 <= row-1 < num_rows:
#            if 0 <= col-1 < num_cols:
#                if game['board'][row-1][col-1] != '.':
#                    if game['mask'][row-1][col-1] == False:
#                        revealed += dig_2d(game, row-1, col-1)
#        if 0 <= row < num_rows:
#            if 0 <= col-1 < num_cols:
#                if game['board'][row][col-1] != '.':
#                    if game['mask'][row][col-1] == False:
#                        revealed += dig_2d(game, row, col-1)
#        if 0 <= row+1 < num_rows:
#            if 0 <= col-1 < num_cols:
#                if game['board'][row+1][col-1] != '.':
#                    if game['mask'][row+1][col-1] == False:
#                        revealed += dig_2d(game, row+1, col-1)
#        if 0 <= row-1 < num_rows:
#            if 0 <= col < num_cols:
#                if game['board'][row-1][col] != '.':
#                    if game['mask'][row-1][col] == False:
#                        revealed += dig_2d(game, row-1, col)
#        if 0 <= row < num_rows:
#            if 0 <= col < num_cols:
#                if game['board'][row][col] != '.':
#                    if game['mask'][row][col] == False:
#                        revealed += dig_2d(game, row, col)
#        if 0 <= row+1 < num_rows:
#            if 0 <= col < num_cols:
#                if game['board'][row+1][col] != '.':
#                    if game['mask'][row+1][col] == False:
#                        revealed += dig_2d(game, row+1, col)
#        if 0 <= row-1 < num_rows:
#            if 0 <= col+1 < num_cols:
#                if game['board'][row-1][col+1] != '.':
#                    if game['mask'][row-1][col+1] == False:
#                        revealed += dig_2d(game, row-1, col+1)
#        if 0 <= row < num_rows:
#            if 0 <= col+1 < num_cols:
#                if game['board'][row][col+1] != '.':
#                    if game['mask'][row][col+1] == False:
#                        revealed += dig_2d(game, row, col+1)
#        if 0 <= row+1 < num_rows:
#            if 0 <= col+1 < num_cols:
#                if game['board'][row+1][col+1] != '.':
#                    if game['mask'][row+1][col+1] == False:
#                        revealed += dig_2d(game, row+1, col+1)
#                        
#        
#
#    bombs = 0  # set number of bombs to 0
#    covered_squares = 0
#    for r in range(game['dimensions'][0]):
#        # for each r,
#        for c in range(game['dimensions'][1]):
#            # for each c,
#            if game['board'][r][c] == '.':
#                if  game['mask'][r][c] == True:
#                    # if the game mask is True, and the board is '.', add 1 to
#                    # bombs
#                    bombs += 1
#            elif game['mask'][r][c] == False:
#                covered_squares += 1
#    bad_squares = bombs + covered_squares
#    if bad_squares > 0:
#        game['state'] = 'ongoing'
#        return revealed
#    else:
#        game['state'] = 'victory'
#        return revealed


def render_2d(game, xray=False):
    """
    Prepare a game for display.

    Returns a two-dimensional array (list of lists) of '_' (hidden squares), '.'
    (bombs), ' ' (empty squares), or '1', '2', etc. (squares neighboring bombs).
    game['mask'] indicates which squares should be visible.  If xray is True (the
    default is False), game['mask'] is ignored and all cells are shown.

    Parameters:
       game (dict): Game state
       xray (bool): Whether to reveal all tiles or just the ones allowed by
                    game['mask']

    Returns:
       A 2D array (list of lists)

    >>> render_2d({'dimensions': (2, 4),
    ...         'state': 'ongoing',
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'mask':  [[False, True, True, False],
    ...                   [False, False, True, False]]}, False)
    [['_', '3', '1', '_'], ['_', '_', '1', '_']]

    >>> render_2d({'dimensions': (2, 4),
    ...         'state': 'ongoing',
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'mask':  [[False, True, False, True],
    ...                   [False, False, False, True]]}, True)
    [['.', '3', '1', ' '], ['.', '.', '1', ' ']]
    """
    board_copy1 = [i.copy() for i in game['board']]
    board_copy2 = [i.copy() for i in game['board']]
    #make two copies of the board, one for the coords and one for the mask
    
    for i in range(len(game['board'])):
        for x in range(len(game['board'][i])): 
            #loop through the coordinates of the board
            if game['board'][i][x] == 0:
                board_copy1[i][x] = ' '
                #if val is 0, make a blanks spot
            board_copy1[i][x] = str(board_copy1[i][x])
            #make resulting value a string value
        
                
    if xray: 
        return board_copy1
    #if true, return the board value, otherwise:
    
    else: 
        for i in range(len(game['board'])):
            for x in range(len(game['board'][i])): 
                if game['mask'][i][x] == False:
                    board_copy2[i][x] = '_'
                    #if the mask value is false, return an empty space
                elif game['board'][i][x] == 0:
                    board_copy2[i][x] = ' '
                    #if the value is 0, return an empty space
                board_copy2[i][x] = str(board_copy2[i][x])
                    
        return board_copy2
    
#print(render_2d({'dimensions': (2, 4), 'state': 'ongoing', 'board': [['.', 3, 1, 0], ['.', '.', 1, 0]], 'mask':  [[False, True, True, False],[False, False, True, False]]}, True))
        
        

def render_ascii(game, xray=False):
    """
    Render a game as ASCII art.

    Returns a string-based representation of argument 'game'.  Each tile of the
    game board should be rendered as in the function 'render_2d(game)'.

    Parameters:
       game (dict): Game state
       xray (bool): Whether to reveal all tiles or just the ones allowed by
                    game['mask']

    Returns:
       A string-based representation of game

    >>> print(render_ascii({'dimensions': (2, 4),
    ...                     'state': 'ongoing',
    ...                     'board': [['.', 3, 1, 0],
    ...                               ['.', '.', 1, 0]],
    ...                     'mask':  [[True, True, True, False],
    ...                               [False, False, True, False]]}))
    .31_
    __1_
    """
    
    board = render_2d(game, xray)
    #access the board
    
    string_val = ''
    #if the string value is an empty
    for row in board: 
        for i in row: 
            string_val += (str(i))
            
        string_val += '\n'
        
    #\n creates a blank line at the end, make sure to remove it
    return string_val[0:-1]

        
            
#print(render_ascii({'dimensions': (2, 4), 'state': 'ongoing', 'board': [['.', 3, 1, 0], ['.', '.', 1, 0]], 'mask':  [[False, True, True, False],[False, False, True, False]]}, True))
               
        



# N-D IMPLEMENTATION
def value(array, coords):
    """
    Returns the value associated with an array at a coordinate value. 

    """
    if len(coords) == 1: 
        return array[coords[0]]     
    else: 
        #first parameter is getting next array (reduce size by using next coord)
        #second parameter goes through each dimension 
        return value(array[coords[0]], coords[1:]) 
            

def replace_val(array, coords, value):
    """
    given an array, replaces the value at coords
    """
    if len(coords) == 1: 
        array[coords[0]] = value 
            
    else: 
        #first parameter is getting next array (reduce size by using next coord)
        #second parameter goes through each dimension 
        
        replace_val(array[coords[0]], coords[1:], value) 
    
        
def create_nd_array(dimensions, value):
    """
    given an array and dimensions, returns a board filled with that value 
    """
    coord = len(dimensions)
    
    if coord == 1:
       return [value]*dimensions[0]
   
    else: 
        result = []
        #look at outer dimension and recurse downwards
        for i in range(dimensions[0]):
            #starting point 
            #move on the the rest of dimensions 
            result.append(create_nd_array(dimensions[1:], value)) 
            
            
    return result    

def return_state(game):
    """
    given a game, returns the state
    """
    return game['state']


def return_neighbors(game_dimensions, coords):
    """
    given an array, retunrs the neighbors
    """
 
    if len(coords) == 1:
        #if the len is 1
        
        result = [[coords[0]+1], [coords[0]], [coords[0]-1]]
        #three neighbors
        final_result = []
        for i in result: 
            if i[0] < 0:
                continue
            #if negative
            if i[0] >= game_dimensions[0]:
                #if greater than baard
                continue 
            
            final_result.append(i)
            
        return final_result
            
        
    else:
        result = []
        
        for i in range(coords[0]-1, coords[0]+2): 
        #first layer of tuple, gets neighbors
        
            if i < 0: 
                continue 
            
            if i >= game_dimensions[0]:
                continue 
        
            #gets neighbor-1, number itself, and neighhor+1
            for neighbor in return_neighbors(game_dimensions[1:], coords[1:]): 
                result.append([i]+neighbor)
                
        return result 
                
    
            
def all_coords(game_dimensions):
    """
    given dimensions, returns all the relevant coordinates at the board. Uses a generator 
    """
        
    if len(game_dimensions) == 1:
        #result = []
        for i in range(game_dimensions[0]):
            yield (i,)
            #result.append([i])
            
        #return result
    
    else: 
        
        #result = []
        for i in range(game_dimensions[0]):
            for neighbor in all_coords(game_dimensions[1:]):
                #result.append([i]+neighbor)
                yield (i,)+neighbor 

    
    
  

def new_game_nd(dimensions, bombs):
    """
    Start a new game.

    Return a game state dictionary, with the 'dimensions', 'state', 'board' and
    'mask' fields adequately initialized.


    Args:
       dimensions (tuple): Dimensions of the board
       bombs (list): Bomb locations as a list of lists, each an
                     N-dimensional coordinate

    Returns:
       A game state dictionary

    >>> g = new_game_nd((2, 4, 2), [(0, 0, 1), (1, 0, 0), (1, 1, 1)])
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    mask:
        [[False, False], [False, False], [False, False], [False, False]]
        [[False, False], [False, False], [False, False], [False, False]]
    state: ongoing
    """
    #make board an ND array of zeros 
    #when bombs added, also 
    board = create_nd_array(dimensions, 0)
    for bomb in bombs: 
        replace_val(board, bomb, '.')
        
        
    for bomb in bombs:

        for neighbor in return_neighbors(dimensions, bomb):
        
            val = value(board, neighbor)
            if val != '.':
                #if value not a bomb, add to value 
                replace_val(board, neighbor, val+1)
            
    mask = create_nd_array(dimensions, False)
    #make array mask 
    
    return {'dimensions': dimensions, 'board': board, 'mask': mask, 'state': 'ongoing'}
        


    
    

def dig_nd(game, coordinates):
    """
    Recursively dig up square at coords and neighboring squares.

    Update the mask to reveal square at coords; then recursively reveal its
    neighbors, as long as coords does not contain and is not adjacent to a
    bomb.  Return a number indicating how many squares were revealed.  No
    action should be taken and 0 returned if the incoming state of the game
    is not 'ongoing'.

    The updated state is 'defeat' when at least one bomb is visible on the
    board after digging, 'victory' when all safe squares (squares that do
    not contain a bomb) and no bombs are visible, and 'ongoing' otherwise.

    Args:
       coordinates (tuple): Where to start digging

    Returns:
       int: number of squares revealed

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'mask': [[[False, False], [False, True], [False, False], [False, False]],
    ...               [[False, False], [False, False], [False, False], [False, False]]],
    ...      'state': 'ongoing'}
    >>> dig_nd(g, (0, 3, 0))
    8
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    mask:
        [[False, False], [False, True], [True, True], [True, True]]
        [[False, False], [False, False], [True, True], [True, True]]
    state: ongoing
    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'mask': [[[False, False], [False, True], [False, False], [False, False]],
    ...               [[False, False], [False, False], [False, False], [False, False]]],
    ...      'state': 'ongoing'}
    >>> dig_nd(g, (0, 0, 1))
    1
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    mask:
        [[False, True], [False, True], [False, False], [False, False]]
        [[False, False], [False, False], [False, False], [False, False]]
    state: defeat
    """

    #replace mask at coords and its neighbors 
    neighbors = return_neighbors(game['dimensions'], coordinates)
    
    count = 0
    #keeps track of revealed neighbors
    val = value(game['board'], coordinates)
    #gets value 

    if game['state'] != 'ongoing':
        return count 
    #if victory or defeat, just return the count
    
    if val == '.':
        #if bomb, reveal mask and increase count, also change to defeat
        replace_val(game['mask'], coordinates, True)
        count += 1
        game['state'] = 'defeat'
        return count 
        
    #if true, return, return 0 
    if value(game['mask'], coordinates) == True:
        return 0 
    
    #if not 0, return 1
    if val != 0: 
        replace_val(game['mask'], coordinates, True)
        return 1
        
    #recurive step, increase count, replae val, and look through neighbors
    else: 
        count += 1 
        replace_val(game['mask'], coordinates, True)
        for neighbor in neighbors: 
            state = dig_nd(game, neighbor)
            count += state 
    
    #check entire state to see if all non-bombs revealed to see if you win (non-bomb squares have corresponding value of true)
    
    #check for victory
    all_coord = all_coords(game['dimensions'])
    for coord in all_coord:
        if value(game['board'], coord) != '.' and value(game['mask'], coord) == False:
            game['state'] = 'ongoing'
            
            return count 

         
    game['state'] = 'victory'
    return count 

    

def render_nd(game, xray=False):
    """
    Prepare the game for display.

    Returns an N-dimensional array (nested lists) of '_' (hidden squares),
    '.' (bombs), ' ' (empty squares), or '1', '2', etc. (squares
    neighboring bombs).  The mask indicates which squares should be
    visible.  If xray is True (the default is False), the mask is ignored
    and all cells are shown.

    Args:
       xray (bool): Whether to reveal all tiles or just the ones allowed by
                    the mask

    Returns:
       An n-dimensional array of strings (nested lists)

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'mask': [[[False, False], [False, True], [True, True], [True, True]],
    ...               [[False, False], [False, False], [True, True], [True, True]]],
    ...      'state': 'ongoing'}
    >>> render_nd(g, False)
    [[['_', '_'], ['_', '3'], ['1', '1'], [' ', ' ']],
     [['_', '_'], ['_', '_'], ['1', '1'], [' ', ' ']]]

    >>> render_nd(g, True)
    [[['3', '.'], ['3', '3'], ['1', '1'], [' ', ' ']],
     [['.', '3'], ['3', '.'], ['1', '1'], [' ', ' ']]]
    """
    
    board = create_nd_array(game['dimensions'], 0)
    
    all_coord = all_coords(game['dimensions'])
    
    #create theboard 
    
    for coord in all_coord: 
        if value(game['board'], coord) == 0:
            replace_val(board, coord, ' ')
            #replace the 0s 
        if xray == True: 
            if value(game['board'], coord) == 0:
                replace_val(board, coord, ' ')
                #if true, return blank space
            else: 
                replace_val(board, coord, str(value(game['board'], coord)))
                #else, replace with string vlaye 
        else: 
            if value(game['mask'], coord) == True: 
                if value(game['board'], coord) == 0:
                    replace_val(board, coord, ' ')
                    #otherwise replace valye 
                    
                else: 
                    replace_val(board, coord, str(value(game['board'], coord)))
                    
            else: 
                replace_val(board, coord, '_')
                #otherwise, empty space 
                
            
    return board 
        
    

if __name__ == "__main__":
    # Test with doctests. Helpful to debug individual lab.py functions.
    import doctest
    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags) #runs ALL doctests
    #g = new_game_nd((2, 4, 2), [(0, 0, 1), (1, 0, 0), (1, 1, 1)])
    #print(g)
#    a = return_neighbors((10, 20, 3), (5, 13, 0))
#    c = set()
#    for i in a:
#        c.add(tuple(i))
#        
#    b = set({(4,12,0),(5,12,0),(6,12,0),(4,13,0),(6,13,0),(4,14,0),(5,14,0),(6,14,0),(4,12,1),(5,12,1),(6,12,1),(4,13,1),(6,13,1),(4,14,1),(5,14,1),(6,14,1),(5,13,1)})
#    print(c-b)
#    print(b-c)
    g = {'dimensions': (2, 4, 2),
          'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
                    [['.', 3], [3, '.'], [1, 1], [0, 0]]],
          'mask': [[[False, False], [False, True], [False, False], [False, False]],
                   [[False, False], [False, False], [False, False], [False, False]]],
          'state': 'ongoing'}
    print(dig_nd(g, (0, 3, 0)))
    

    # Alternatively, can run the doctests JUST for specified function/methods,
    # e.g., for render_2d or any other function you might want.  To do so, comment
    # out the above line, and uncomment the below line of code. This may be
    # useful as you write/debug individual doctests or functions.  Also, the
    # verbose flag can be set to True to see all test results, including those
    # that pass.
    #
    doctest.run_docstring_examples(dig_nd, globals(), optionflags=_doctest_flags, verbose=False)
