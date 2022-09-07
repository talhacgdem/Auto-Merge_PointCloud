import sys


def get_distance(p, q):
    """
    Return euclidean distance between points p and q
    assuming both to have the same number of dimensions
    """
    # sum of squared difference between coordinates
    s_sq_difference = 0
    for p_i, q_i in zip(p, q):
        s_sq_difference += (p_i - q_i) ** 2

    # take sq root of sum of squared difference
    distance = s_sq_difference ** 0.5
    return distance


def findClosest(arr):
    min_val = sys.maxsize
    first = (arr[0][0], arr[0][1], arr[0][2])
    a = 1
    while a < len(arr):
        second = (arr[a][0], arr[a][1], arr[a][2])
        distance = get_distance(first, second)
        if distance < min_val:
            min_val = distance
            print("Closest point found on index : {} , Distance is : {}".format(a, distance))
        # else:
            # print("     ---> On index : {}".format(a))

        a += 1
# # 0.8055060521187908
# # check the function
# a = (1.62809, 1.43013, 1.75379)
# b = (2.04509, 1.63013, 1.62879)
# # distance b/w a and b
# d = get_distance(a, b)
# # display the result
# print(d)
