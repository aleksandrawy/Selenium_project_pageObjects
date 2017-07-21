from page_object_example.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from page_object_example.new_customer_page import NewCustomerPage

class EditCustomerPage(BasePage, NewCustomerPage): #zrobic dziedziczenie!

    @property
    def customer_id_text_field(self):
        return self.driver.find_element_by_name('cusid')

    @property
    def submit_button(self):
        return self.driver.find_element_by_name('AccSubmit')

    @property
    def submit_form_button(self):
        return self.driver.find_element_by_name('sub')

    @property
    def reset_button(self):
        return self.driver.find_element_by_name('res')

    @property
    def date_of_birth_text_field(self):
        return self.driver.find_element_by_name('dob')

    @property
    def address_text_field(self):
        return self.driver.find_element_by_xpath('html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/textarea')

    @property
    def city_text_field(self):
        return self.driver.find_element_by_name('city')

    @property
    def state_text_field(self):
        return self.driver.find_element_by_name('state')

    @property
    def PIN_text_field(self):
        return self.driver.find_element_by_name('pinno')

    @property
    def mobile_number_text_field(self):
        return self.driver.find_element_by_name('telephoneno')

    @property
    def email_text_field(self):
        return self.driver.find_element_by_name('emailid')

    @property
    def password_text_field(self):
        return self.driver.find_element_by_name('password')

    @property
    def submit_button(self):
        return self.driver.find_element_by_name('sub')

    @property
    def reset_button(self):
        return self.driver.find_element_by_name('res')

    def open(self):
        WebDriverWait(self.driver, 10)#.until(EC.visibility_of_element_located((By.XPATH), './/a[@href="DeleteCustomerInput.php"]'))
        self.driver.find_element_by_xpath('.//a[@href="EditCustomer.php"]').click()
