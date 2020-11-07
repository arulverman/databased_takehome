import p1,p2,p3,p4

class TestAll:
    def test_p1(self):
        assert p1.leastFactorial(17) == 24
        assert p1.leastFactorial(5) == 6
        assert p1.leastFactorial(106) == 120
        assert p1.leastFactorial(500) == -1
        assert p1.leastFactorial(-10) == -1

    def test_p2(self):
        assert p2.getTotalNumberOfLipsticks(5, 2) == 9
        assert p2.getTotalNumberOfLipsticks(15, 5) == 18
        assert p2.getTotalNumberOfLipsticks(2, 3) == 2
        assert p2.getTotalNumberOfLipsticks(15, 4) == 19
        assert p2.getTotalNumberOfLipsticks(20, 20) == 21
        assert p2.getTotalNumberOfLipsticks(0, 0) == 0
        assert p2.getTotalNumberOfLipsticks(-100, -300) == 0

    def test_p3(self):
        assert p3.getLastStudent(4, 6, 2) == 3
        assert p3.getLastStudent(5, 2, 1) == 2
        assert p3.getLastStudent(5, 2, 2) == 3
        assert p3.getLastStudent(7, 19, 2) == 6
        assert p3.getLastStudent(3, 7, 3) == 3
        assert p3.getLastStudent(4, 9, 2) == 2
        assert p3.getLastStudent(12250000, 90000000, 30) == 4250029
        assert p3.getLastStudent(0, 0, 30) == -1

    def test_p4(self):
        assert p4.peopleWatch([5.5, 4.5, 4, 6, 3.3]) == [3, 3, 3, None, None]
        assert p4.peopleWatch([6, 4.5, 5.5, 4, 6, 3.3]) == [None, 2, 4, 4, None, None]
        assert p4.peopleWatch([2, 1, 4, 4, 5, 9]) == [2, 2, 4, 4, 5, None]