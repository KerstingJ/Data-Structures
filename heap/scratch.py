
def findMissing(arr):
    biggest = arr[len(arr)-1]

    for i in range(biggest):
        if arr[i] != i:
            return i

    return biggest + 1


def merge_n_lists(*arrs):

    sorted = []

    while len(arrs) > 1:  # we have more than 1 array in arrs with items

        small = []

        # for arr in arrs
        for arr in arrs:

            if len(arr) < 1:
                # if arr has no elements remove it from list
                # continue with next itr of loop
                arrs.remove(arr)
                continue
            # find biggest 0th of arrays;
            # if small hasn't been found small is now the current arr
            if len(small) < 1 or arr[0] < small[0]:
                # reference that array as small
                small = arr

        # pop value from smalles arr and add to sorted list
        sorted.append(small.pop(0))

    return sorted + arrs[0]
