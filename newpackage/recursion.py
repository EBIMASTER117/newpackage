def sum_array(array):
    '''
    Return sum of an array

    Args:
        n (array): list of mulpiple values that can added up

    Returns:
        int: sum of all the items of n

    Examples:
        >>> sum_array([1, 2, 3, 4, 5])
        15
        >>> sum_array([2, 4, 6, 8])
        20
        >>> sum_array([12, 6, 19, 47])
        84
    '''
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    '''
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    '''

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    '''
    Return n factorial. Raises ValueError if n is not integral or is negative.

    Args:
        n (int): number to get the factorial of.

    Returns:
        int: factorial of n

    Examples:
        >>> factorial(5)
        120
        >>> factorial(8)
        40320
        >>> factorial(10)
        3628800
    '''
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError("n should be a whole and positive integer")
    else:
        return n * factorial(n-1)

def reverse(word):
    '''
    Return a string that has been reversed

    Args:
        word (str): a string

    Returns:
        str: word string reversed and given backwards

    Examples:
        >>> reverse('cheese')
        'eseehc'
        >>> reverse('banana')
        'ananab'
        >>> reverse('awesome')
        'emosewa'
    '''
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverse(word[:-1])
