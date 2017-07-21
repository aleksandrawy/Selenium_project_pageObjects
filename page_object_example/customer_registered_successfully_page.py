from page_object_example.base_page import BasePage


class CustomerRegisteredSuccessfullyPage(BasePage):

    @property
    def title_label(self):
        return self.driver.find_element_by_class_name('heading3')

    @property
    def customer_id_label(self):
        return self.driver.find_element_by_xpath('.//td[text()="Customer ID"]/following-sibling::td') #sasiada bierzemy

    def get_title(self):
        return self.title_label.text

    def get_customer_id(self):
        return self.customer_id_label.text