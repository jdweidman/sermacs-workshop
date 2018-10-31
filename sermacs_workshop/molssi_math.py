"""
molssi_math.py
Sample repository for MolSSI Workshop at SERMACS

Misc. math functions
"""


def mean(num_list):
    """
    Computes the mean of a list

    Parameters
    ----------------
    num_list: list
        List to calculate mean of

    Returns
    ----------------
    mean: float
        Mean of list of numbers
    """

    #Check that input is type list
    if not isinstance(num_list, list):
        raise TypeError('Input must be type list')

    #Check that list has length
    if len(num_list) == 0:
        raise IndexError('Cannot apply mean function to empty list')

    #Check that list contains numbers
    #for num in num_list:
    #    if isinstance(num, int) or isinstance(num, float):
    #        pass
    #    else:
    #        raise TypeError('Input list must consist only of numbers')

    #sum = 0.0
    #for num in num_list:
    #    sum += num

    #mean = sum/len(num_list)
    #return mean

    try:
        mean = sum(num_list) / len(num_list)
    except TypeError:
        raise TypeError('Input list must consist only of ints or floats')

    return mean
