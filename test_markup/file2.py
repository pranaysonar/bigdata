
class Test002:

    def test_sum_005(self):
        a = 1
        b = 3
        sum = a + b
        print("sum of a + b =" + str(sum))
        if sum == 4:
            assert True
        else:
            assert False

    def test_mul_006(self):
        a = 2
        b = 2
        mul = a * b
        print("Mul of a * b =" + str(mul))
        if mul == 5:
            assert True
        else:
            assert False

    def sub_007(self):
        a = 20
        b = 2
        sub = a - b
        print("sub of a - b =" + str(sub))
        if sub == 18:
            assert True
        else:
            assert False


    def test_sub_008(self):
        a = 20
        b = 2
        sub = a - b
        print("sub of a - b =" + str(sub))
        if sub == 18:
            assert True
        else:
            assert False


# root folder but make sure your cmd is pointed at project
# 1 command --> pytest testCases/test_file1.py
# using abs path --> command
# 2 command -- > pytest "D:\Credence Class Notes\CredenceBatches\Credence_Automation_Jul 24\Pytest_Demo\testCases\test_file1.py"

# pytest : it will search all the pytest file in folder and in folders also, this is  to run all testCases in project
# 3 command --> pytest

# 4 command --> pytest -v -s
# verbose and std output for more detailing of test run


