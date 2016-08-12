def shift_left(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the left, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)  # no return value
    print(numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    if n > len(lst):
       for i in range(len(lst)):
           lst[i] = fill_value

    elif n > 0 and n <= len(lst):
        x = 0
        for i in range(len(lst) - n):
            lst[x] = lst[i + n]
            x += 1
        for i in range(n):
            lst[-1 - i] = fill_value


def shifted_left(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the left, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_left(numbers, 2)
    print(shifted_numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """
    new_list = []
    if n > len(lst):
       for i in range(len(lst)):
           new_list.append(fill_value)
    else:
        new_list.extend(lst[n:])
        for i in range(n):
            new_list.append(fill_value)

    return new_list


def shift_right(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the right, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)  # no return value
    print(numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    temp_list = []
    for i in range(len(lst)):
        temp_list.append(lst[i])
    x = 0
    if n > len(lst):
       for i in range(len(lst)):
           lst[i] = fill_value

    elif n >= 0 and n < len(lst):
        for i in range(n):
            lst[i] = fill_value
        for i in range(n, len(lst)):
            lst[n + x] = temp_list[x]
            x += 1


def shifted_right(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the right, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_right(numbers, 2)
    print(shifted_numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """

    new_list = []
    if n > len(lst):
       for i in range(len(lst)):
           new_list.append(fill_value)
    elif n < 0:
        new_list.extend(lst)
    elif n >= 0 and n <= len(lst):
        for i in range(n):
            new_list.append(fill_value)
        new_list.extend(lst[:len(lst) - n])

    return new_list

def fill(lst, fill_value=0):
    """Fills an existing list, lst, with the value, fill_value.

    numbers = [1, 2, 3, 4]
    fill(numbers)
    print(numbers) # [0, 0, 0, 0]

    :param lst: the list to be filled with values
    :type lst: list
    :param fill_value: the value to fill the list with
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    for i in range(len(lst)):
        lst[i] = fill_value

def filled(lst, fill_value=0):
    """Creates a new list with the same length as the list passed in, lst,
    and fills it with the value, fill_value.

    numbers = [1, 2, 3, 4]
    filled_list = fill(numbers)
    print(filled_list) # [0, 0, 0, 0]

    :param lst: the list to use as the basis for the length of the new list
    :type lst: list
    :param fill_value: the value to fill the new list with
    :type fill_value: any
    :return: the new list filled with fill_value
    :rtype: list
    """
    new_list = []
    for i in range(len(lst)):
        new_list.append(fill_value)
    return new_list

def mean(lst):
    """Calculates and returns the average of all numbers in incoming list, lst.

    print(mean([12, 4, 14])) # --> 10

    :param lst: list of numeric types
    :type lst: list
    :return: the average of all numbers in lst
    :rtype: float
    """
    sum = 0
    for i in range(len(lst)):
        sum += int(lst[i])
    return sum / len(lst)

def median(lst):
    """Calculates the median of incoming list, lst.

    :param lst: list of numeric types
    :type lst: list
    :return: the median of all numbers in lst
    :rtype: int or float
    """
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 == 0:
        if len(lst) == 2:
            median = (lst[0] + lst[1]) / 2
        else:
            median = (sorted_list[int(len(lst) / 2 - 1)] + sorted_list[int((len(lst) / 2))]) / 2
    else:
        median = sorted_list[int((len(lst) / 2))]
    return median

def std_dev(lst):
    """Calculates the standard deviation of the sample for the incoming list, lst.

    :param lst: list of numeric types
    :type lst: list
    :return: the standard devation of numbers in incoming list, lst
    :rtype: float
    """
    mean_difference = []
    mean_number = mean(lst)
    for number in lst:
        mean_difference.append((int(number) - mean_number) ** 2)
    sum = 0
    for i in range(len(mean_difference)):
        sum += mean_difference[i]
    difference_mean = (1 / (len(lst) - 1)) * sum
    return difference_mean ** .5

if __name__ == '__main__':
    print("put your test cases here")
    print("\nshift_left\n=====")
    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_left(numbers, 5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_left(numbers, -5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_left(numbers, 1, None)
    print(numbers)
    print("\nshifted_left\n=====")
    numbers = [1, 2, 3, 4]
    print(shifted_left(numbers, 2))
    print(shifted_left(numbers, 5))
    print(shifted_left(numbers, -5))
    print(shifted_left(numbers, 1, None))
    print("\nshift_right\n=====")
    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_right(numbers, 5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_right(numbers, -5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_right(numbers, 1, None)
    print(numbers)
    print("\nshifted_right\n=====")
    numbers = [1, 2, 3, 4]
    print(shifted_right(numbers, 2))
    print(shifted_right(numbers, 5))
    print(shifted_right(numbers, -5))
    print(shifted_right(numbers, 1, None))
    print("\nfill\n=====")
    numbers = [1, 2, 3, 4]
    fill(numbers)
    print(numbers)
    numbers = [1, 2, 3, 4]
    fill(numbers, fill_value=None)
    print(numbers)
    print("\nfilled\n=====")
    numbers = [1, 2, 3, 4]
    print(filled(numbers))
    print(filled(numbers, fill_value=None))
    print("\nmean\n====")
    print(mean([1, 2, 3, 4, 5]))
    print(mean([7, 11, 9, 18, 15, 12]))
    print("\nmedian\n=====")
    print(median([1, 2, 3, 4]))
    print(median([1, 2, 3]))
    print(median([1, 2]))
    print("\nstd_dev\n=====")
    print(std_dev([7, 11, 9, 18, 15, 12]))



