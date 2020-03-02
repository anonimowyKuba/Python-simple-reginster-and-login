from random import randrange
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewUserReg():
    def __init__(self, driver):
        self.driver = driver

    def fill_fields(self, password):

        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'uniform-id_gender1'))).click()

        driver.find_element_by_id("customer_firstname").send_keys("SomeName")
        driver.find_element_by_id("customer_lastname").send_keys("JakiesNazwisko")
        driver.find_element_by_id("passwd").send_keys(password)

        Select(driver.find_element_by_name('days')).select_by_value(str(randrange(1, 28)))
        Select(driver.find_element_by_name('months')).select_by_value(str(randrange(1, 12)))
        Select(driver.find_element_by_name('years')).select_by_value("1950")

        driver.find_element_by_id("address1").send_keys("SomeStreet")
        driver.find_element_by_id("city").send_keys("SomeCity")

        Select(driver.find_element_by_name("id_state")).select_by_visible_text("Hawaii")

        driver.find_element_by_id("postcode").send_keys("42000")
        driver.find_element_by_id("phone_mobile").send_keys("123456789")
