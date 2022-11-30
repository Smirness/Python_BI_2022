def sequential_map(*args):
    """
    The function implements sequentially any number of functions on the container
    :param args:
    :return con:
    """
    funcs = args[:-1]
    container = args[-1]
    for i in range(len(funcs)):
        container = list(map(funcs[i], container))
    res = container
    print(res)


def consensus_filter(*args):
    """
    The function returns a list of values that give True when the container is passed.
    :param args:
    :return :
    """

    result = []
    ind_res = []
    index_list = []
    passed_list = []

    funcs = args[:-1]
    container = args[-1]
    for i in range(len(funcs)):
        res = tuple(map(funcs[i], container))
        result.append(res)

    for line in result:
        for i in range(len(line)):
            if line[i] is True:
                index_list.append(i)

    for index in index_list:
        if index_list.count(index) == len(funcs) and index not in ind_res:
            ind_res.append(index)

    for index in ind_res:
        res = container[index]
        passed_list.append(res)
    print(passed_list)


def conditional_reduce(func_1, func_2, container):
    """
    Reduce of numbers in container, which are passed through func_1 with True.
    :param func_1:
    :param func_2:
    :param container:
    :return reduce:
    """

    index_list = []
    index_true_list = []

    # making index list
    for i in range(len(container)):
        index_list.append(i)

    # taking info which nums are passed
    tf_list = list(map(func_1, container))

    # taking indexes of nums with True result
    for i in index_list:
        if tf_list[i] is True:
            index_true_list.append(i)

    # making container with passed nums
    container_pased = list(map(lambda x: container[x], index_true_list))

    # reduce function. Prefix is 1st num. The loop sums prefix with next num and save result as prefix.
    container_prefix = [container_pased[0]]
    for i in range(len(container_pased) - 1):
        container_prefix = list(map(func_2, container_prefix, container_pased[i + 1:len(container_pased)]))
    reduce = container_prefix

    print(reduce)


def func_chain(*args):
    """
    The function returns a function that joins everything and executes sequentially
    :param args: functions list and int
    :return com_func:
    """
    def com_func(x):
        for func in args:
            x = func(x)
        print(x)

    return com_func


def sequential_map_chain(*args):
    """
    The function returns a function that joins everything and executes sequentially
    :param args: functions list and int list
    :return com_func:
    """

    def com_func(container):
        for i in range(len(args)):
            container = list(map(args[i], container))
        print(container)

    return com_func


def multiple_partial(*args, **kwargs):
    x = args[0]
    print(x)
    return x

# import numpy as np
# # ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)
# ax1_mean = multiple_partial(np.mean, np.max, np.sum, axis=1)
# arr = [[14, 17, 12, 33, 44],
#        [15, 6, 27, 8, 19],
#        [23, 2, 54, 1, 4]]
# print(ax1_mean(arr))
