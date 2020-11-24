# Problem 4 - Cinnabon Line

# -- Assumptions --
# Duplicate values are allowed in list.
# Index starts from [0]


def peopleWatch(heightOfPeople):

    res = []
    start = 0
    end = len(heightOfPeople)-1
    store_idx = 0
    flg = False

    while(start<end):

        max_height = heightOfPeople[start]

        if heightOfPeople[end] > max_height:
            store_idx = end
            flg = True

        if end == start+1:
            if flg:
                res.append(store_idx)
            else:
                res.append(None)

            start = start + 1
            end = len(heightOfPeople)-1
            flg = False

        else:
            end = end-1

    # There will be no person taller after the person on last index
    res.append(None)

    return res


# Uncomment to print test cases
'''
print(peopleWatch([5.5, 4.5, 4, 6, 3.3]))
print(peopleWatch([6, 4.5, 5.5, 4, 6, 3.3]))
print(peopleWatch([2, 1, 4, 4, 5, 9]))
print(peopleWatch([12, 2, 1, 4, 9, 10, 2]))
'''
