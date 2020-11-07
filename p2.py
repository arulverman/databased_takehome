# Problem 2 - Recycling Lipstick

def getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):

    # corner case when inputs are invalid
    if numberOfLeftoversNeeded <= 0 or numberOfLipsticks <= 0:
        return 0

    total = numberOfLipsticks
    newLipsticks = 0

    while numberOfLipsticks >= numberOfLeftoversNeeded:
        createLipstick = int(numberOfLipsticks/numberOfLeftoversNeeded)
        unusedLeftover = (numberOfLipsticks % numberOfLeftoversNeeded)
        numberOfLipsticks = createLipstick + unusedLeftover
        newLipsticks += createLipstick

    return total+newLipsticks


# Uncomment to print test cases
'''
print(getTotalNumberOfLipsticks(5, 2))
print(getTotalNumberOfLipsticks(15, 5))
print(getTotalNumberOfLipsticks(2, 3))
print(getTotalNumberOfLipsticks(15, 4))
print(getTotalNumberOfLipsticks(20, 20))
print(getTotalNumberOfLipsticks(0, 0))
print(getTotalNumberOfLipsticks(-100, -300))
'''