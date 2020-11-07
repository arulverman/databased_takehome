# Problem 3 - Student and Treats

def getLastStudent(numberOfStudents, treats, startingChair):

    if numberOfStudents>0 and startingChair>0 and startingChair<=numberOfStudents and treats>0:
        n = startingChair + ((treats-1)*1)
        idx = n % numberOfStudents

        if idx == 0:
            return startingChair

        return idx

    # invalid constraints return -1
    else:
        return -1


# Uncomment to print test cases
'''
print(getLastStudent(4, 6, 2))
print(getLastStudent(5, 2, 1))
print(getLastStudent(5, 2, 2))
print(getLastStudent(7, 19, 2))
print(getLastStudent(3, 7, 3))
print(getLastStudent(4, 9, 2))
print(getLastStudent(12250000, 90000000, 30))
print(getLastStudent(0, 0, 30))
'''