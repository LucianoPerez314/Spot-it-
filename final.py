"""
Code to implement the game of Spot it!

http://www.blueorangegames.com/spotit/

For each function, replace the return statement with your code.  Add
whatever helper functions you deem necessary.
"""

import comp140_module2 as spotit

def equivalent(point1, point2, mod):
    """
    Determines if the two given points are equivalent in the projective
    geometric space in the finite field with the given modulus.

    Each input point, point1 and point2, must be valid within the
    finite field with the given modulus.

    inputs:
        - point1: a tuple of 3 integers representing the first point
        - point2: a tuple of 3 integers representing the second point
        - mod: an integer representing the modulus
        

    returns: a boolean indicating whether or not the points are equivalent
    """
    list(point1)
    list(point2)
    if [(point1[1] * point2[2] - point1[2] * point2[1]) % mod, 
        (point1[2] * point2[0] - point1[0] * point2[2]) % mod, 
        (point1[0] * point2[1] - point1[1] * point2[0]) % mod] == [0, 0, 0]:
        return True
    else:
        tuple(point1)
        tuple(point2)
        return False

def incident(point, line, mod):
    """
    Determines if a point lies on a line in the projective
    geometric space in the finite field with the given modulus.

    The inputs point and line must be valid within the finite field
    with the given modulus.

    inputs:
        - point: a tuple of 3 integers representing a point
        - line: a tuple of 3 integers representing a line
        - mod: an integer representing the modulus

    returns: a boolean indicating whether or not the point lies on the line
    """
    list(point)
    list(line)
    if (point[0] * line[0] + point[1] * line[1] + point[2] * line[2]) % mod == 0:
        
        return True

    else:
        
        tuple(point)
        tuple(line)
    
        return False


def generate_every_point(mod):
    """
    Generates every points in the projective geometric space in
    the finite field with the given modulus including equivalent points.

    inputs:
        - mod: an integer representing the modulus

    Returns: a list of all points, each is a tuple of 3 elements
    """
    every_point = []
    for x_val in range(mod):
        for y_val in range(mod):
            for z_val in range(mod):
                every_point.append((x_val, y_val, z_val))
    every_point.remove((0,0,0))
          
    return every_point 

        
def generate_all_points(mod):
    """
    Generate all unique points in the projective geometric space in
    the finite field with the given modulus.

    inputs:
        - mod: an integer representing the modulus

    Returns: a list of unique points, each is a tuple of 3 elements
    """
   
    every_point = generate_every_point(mod)
    unique_points = []
    equivalent_points = []
    for point1 in every_point:
    # sifts through all the possible points
        if point1 not in equivalent_points:
            unique_points.append(point1)
    #adds it to unique points list if it's not equivalent to any other point
            for point2 in every_point:
                if equivalent(point1, point2, mod):
                    equivalent_points.append(point2)
    #checks if point is equivalent to any point already logged in the equivalent_points list.
    #if it is, then it is added to the equivalent_points list, 
    #if it is not then it's not added to the unique_points list.
    
    return unique_points

                

def create_cards(points, lines, mod):
    """
    Create a list of unique cards.

    Each point and line within the inputs, points and lines, must be
    valid within the finite field with the given modulus.

    inputs:
        - points: a list of unique points, each represented as a tuple of 3 integers
        - lines: a list of unique lines, each represented as a tuple of 3 integers
        - mod: an integer representing the modulus

    returns: a list of lists of integers, where each nested list represents a card.
    """
    deck = []
    for point in points:
        card = []
        for line in lines:
            if incident(point, line, mod):
                card.append(lines.index(line))
        deck.append(card)
            
    return deck


def run():
    """
    Create the deck and play the game.
    """
    # Prime modulus
    # Set to 2 or 3 during development
    # Set to 7 for the actual game
    modulus = 7

    # Generate all unique points for the given modulus
    points = generate_all_points(modulus)

    # Lines are the same as points, so make a copy
    lines = points[:]

    # Generate a deck of cards given the points and lines
    deck = create_cards(points, lines, modulus)

    # Run GUI - uncomment the line below after you have implemented
    #           everything and you can play your game.  The GUI does
    #           not work if the modulus is larger than 7.

    spotit.start(deck)

    # Uncomment the following line to run your game (once you have
    # implemented the run function.)
    

run()
