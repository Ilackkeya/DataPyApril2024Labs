# importing functions from numpy library

from numpy import random
from numpy import resize
from numpy import transpose


# Defining build_board function
def build_board(size):

    # creating a new board of shape 'size' by assigning checker strings randomly
    options = ["Empty", "Red", "Black"]
    checker_board = numpy.random.choice(options, (size, size))
    return checker_board


# Defining get_count function
def get_count(bd):
    # creating empty dictionary to store the count values
    count_items = {}
    for ele in bd:
        for i in ele:
            keys = count_items.keys()
            if i in keys:
                count_items[i] += 1
            else:
                count_items[i] = 1

    return count_items


# Defining change_size function
def change_size(bd, shape):
    board = numpy.resize(bd, (shape, shape))
    return board


# Defining pivot function
def pivot(bd):
    pivot_bd = numpy.transpose(bd)
    return pivot_bd


# Testing if it's running as main file
print(f"Testing out checker's __name__ variable. Here's what's in it: {__name__}.")

if __name__ == "__main__":
    print("This file is not intended to be run as a main program")
