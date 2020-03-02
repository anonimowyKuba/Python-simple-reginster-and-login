import unittest
import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import datafile
from pages.reginsterpage import NewUserReg


class LoginTestsScenario(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox(executable_path='GECODRIVER_PATH_GOES_HERE/geckodriver.exe')
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("Stop")
        self.driver.close()

    def setUp(self):
        print(self._testMethodName)
        self.driver.get('http://automationpractice.com/index.php?controller=authentication')

    def tearDown(self):
        print("\n+++++++")
        if sys.exc_info()[0]:
            self.driver.save_screenshot("screenshots/failshot_%s.png" % self._testMethodName)


    def test_01createAccout(self):
        driver = self.driver

        driver.find_element_by_id("email_create").send_keys(datafile.email)
        driver.find_element_by_id("SubmitCreate").click()

        NewUserReg(driver).fill_fields(datafile.password)

        driver.find_element_by_id("submitAccount").click()

        self.assertEqual(driver.title, "My account - My Store")


    def test_02loginToAccount(self):
        driver = self.driver

        try:
            driver.find_element_by_class_name("logout").click()
        except (NoSuchElementException, TimeoutException):
            pass

        driver.find_element_by_id("email").send_keys(datafile.email)
        driver.find_element_by_id("passwd").send_keys(datafile.password)

        driver.find_element_by_id("SubmitLogin").click()

        self.assertEqual(driver.title, "My account - My Store")





