from page_object_example.base_page import BasePage


class NewCustomerPage(BasePage):

    @property
    def name_text_field(self):
        return self.driver.find_element_by_name('name')

    # @property
    # def gender_radio_button(self, g):
    #     if (g=='m'):
    #         return self.driver.find_element_by_xpath('html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]')
    #     else:
    #         return self.driver.find_element_by_xpath('html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]')

    @property
    def male_radio_button(self):
        return self.driver.find_element_by_xpath('html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]')

    @property
    def female_radio_button(self):
        return self.driver.find_element_by_xpath('html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]')

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
        self.driver.find_element_by_xpath('.//a[@href="addcustomerpage.php"]').click()

    def add_customer(self, data, click_submit=True, click_reset=False):
        if 'customer_name' in data.keys():
            self.name_text_field.send_keys(data['customer_name'])

        if 'gender' in data.keys():
            if data['gender']=='male':
                self.male_radio_button.click()
            elif data['gender']=='female':
                self.female_radio_button.click()

        if 'date_of_birth' in data.keys():
            self.date_of_birth_text_field.send_keys(data['date_of_birth'])

        if 'address' in data.keys():
            self.address_text_field.send_keys(data['address'])

        if 'city' in data.keys():
            self.city_text_field.send_keys(data['city'])

        if 'state' in data.keys():
            self.state_text_field.send_keys(data['state'])

        if 'pin' in data.keys():
            self.PIN_text_field.send_keys(data['pin'])

        if 'mobile_number' in data.keys():
            self.mobile_number_text_field.send_keys(data['mobile_number'])

        if 'email' in data.keys():
            self.email_text_field.send_keys(data['email'])

        if 'password' in data.keys():
            self.password_text_field.send_keys(data['password'])

        if click_submit:
            self.submit_button.click()
        elif click_reset:
            self.reset_button.click()