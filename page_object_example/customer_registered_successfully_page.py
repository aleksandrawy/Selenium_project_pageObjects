from page_object_example.base_page import BasePage


class CustomerRegisteredSuccessfullyPage(BasePage):

    @property
    def title_label(self):
        return self.driver.find_element_by_class_name('heading3')

    def get_title(self):
        return self.title_label.text

