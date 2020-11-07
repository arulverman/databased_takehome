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
getLastStudent(4, 6, 2)
getLastStudent(5, 2, 1)
getLastStudent(5, 2, 2)
getLastStudent(7, 19, 2)
getLastStudent(3, 7, 3)
getLastStudent(4, 9, 2)
getLastStudent(12250000, 90000000, 30)
getLastStudent(0, 0, 30)
'''