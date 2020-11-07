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
getTotalNumberOfLipsticks(5, 2)
getTotalNumberOfLipsticks(15, 5)
getTotalNumberOfLipsticks(2, 3)
getTotalNumberOfLipsticks(15, 4)
getTotalNumberOfLipsticks(20, 20)
getTotalNumberOfLipsticks(0, 0)
getTotalNumberOfLipsticks(-100, -300)
'''