"""
This is a list of functions that should be completed.
"""
from typing import Any
from typing import List
import string


class OurAwesomeException(Exception):
 pass


def is_two_object_has_same_value(first: Any, second: Any) ->bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return first is second


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise TypeError

    Raises:
        TypeError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """

    if not isinstance(first_value, int) or not isinstance(second_value, int):
        raise TypeError("not int")
    return first_value * second_value



def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    try:
        if first_value or second_value == int or float or str:
            return int(float(first_value)) * int(float(second_value))
    except TypeError:
        raise ValueError("Not valid input data")




def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for search

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    return word in text.split()

print(is_word_in_text('hi','hi bla bla?urju'))



def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    numbers_1 = range(13)
    return[i for i in numbers_1 if not (i == 6 or i == 7)]


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """

    res = data[:]
    for i in data:
        if i < 0:
            res.remove(i)
    return res




def alphabet() -> dict:
    """
    Create dict which keys are alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}[2, 9, 6, 7, 3, 2, 1])
    """
    return{index: value for index, value in enumerate(string.ascii_lowercase, 1)}


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    """

    for i in range(0, len(data) - 1):
        while (data[i] > data[i + 1]) and i >= 0:
            data[i], data[i + 1] = data[i + 1], data[i]
            i -= 1
    return data

