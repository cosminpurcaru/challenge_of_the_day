"""
Given a list of integers, assume that every element in the list appears twice, except one. Determine the element that appears only once.
(You're meant to determine the element by traversing the list only once (no sort, etc.)


Examples:

# Input: [1, 9, 9, 5, 1]
# Output: 5

"""


def get_single_appearance_elem(numbers: list):
    """
    Determine the element that appears only once in a list of integers that contains elements that appear twice.

    :param numbers: List of integers
    :return: Number within list that appears only once
    """
    if not numbers:
        return None

    single = numbers[0]
    for i in range(1, len(numbers)):
        single = single ^ numbers[i]

    return single
  
