import unittest
from Test_case.test_res import TestRes
from Test_case.test_res import TICKETNO
import HTMLTestRunnerNew
from Common import read_path


sutie=unittest.TestSuite()
loader=unittest.TestLoader()
sutie.addTest(loader.loadTestsFromTestCase(TICKETNO))
#sutie.addTest(loader.loadTestsFromTestCase(TestRes))
with open(read_path.baogao_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,title='zq',description='zq',tester='zq')
    runner.run(sutie)


