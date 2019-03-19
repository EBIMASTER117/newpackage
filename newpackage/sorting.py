def bubble_sort(items):
    """
    Return a list of items that has been sorted using the bubble sort method

    Args:
        items (list): a list of mulpiple values

    Returns:
        list: a list of multiple values that have been sorted in ascending value

    Examples:
        >>> bubble_sort([1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1])
        [1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 8]

    """
    out = items.copy()
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]

    return out

def merge_sort(items):
    """
    Return a list of items that has been sorted using the merge sort method

    Args:
        items (list): a list of mulpiple values

    Returns:
        list: a list of multiple values that have been sorted in ascending value

    Examples:
        >>> merge_sort([1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1])
        [1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 8]

    """

    if len(items) < 2:return items

    result,mid = [],int(len(items)/2)

    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result

def quick_sort(items):
    """
    Return a list of items that has been sorted using the quick sort method

    Args:
        items (list): a list of mulpiple values

    Returns:
        list: a list of multiple values that have been sorted in ascending value

    Examples:
        >>> quick_sort([1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1])
        [1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 8]

    """
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
