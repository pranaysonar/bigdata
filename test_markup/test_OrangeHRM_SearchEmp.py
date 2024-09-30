import pytest

from test_markup.Add_Emp_Page import AddEmp_Class
from Pageobjects.Login_Page import LoginPage_Class
from Pageobjects.Search_Emp_Page import SearchEmp_Class
from utilities.LoggerFile import LogGenerator
from utilities.readConfigFile import ReadConfig_Class
import time

class Test_SearchEmp:
    username = ReadConfig_Class.getUsername()
    password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.regression
    @pytest.mark.group2
    def test_SearchEmp_006(self, setup):
        self.driver = setup
        self.log.info("Opening browser")
        time.sleep(5)
        self.lp = LoginPage_Class(self.driver)
        self.log.info("Enter Username")
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter Password")
        self.lp.Enter_Password(self.password)
        time.sleep(3)
        self.log.info("Click on login Button")
        self.lp.Click_LoginButton()
        self.ae = AddEmp_Class(self.driver)
        time.sleep(3)
        self.log.info("Click on PIM Button")
        self.ae.Click_PIM()
        time.sleep(2)
        self.se = SearchEmp_Class(self.driver)
        Emp_ID = "0456"
        self.se.Enter_EmpID(Emp_ID)
        time.sleep(2)
        self.se.Click_Search_Emp()
        if self.se.Search_Result() == Emp_ID:
            assert True
        else:
            assert False

# logs are pending for above testcase


# Add emp  --> params and excel
# search emp --> params and excel