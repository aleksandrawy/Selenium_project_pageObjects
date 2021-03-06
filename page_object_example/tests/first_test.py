from page_object_example.login_page import LoginPage
from page_object_example.main_page import MainPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Ie
from page_object_example.new_customer_page import NewCustomerPage
from page_object_example.customer_registered_successfully_page import CustomerRegisteredSuccessfullyPage
import time
from page_object_example.delete_customer_page import DeleteCustomerPage


driver = None
# to be filled in
manager_username = 'mngr88952'
manager_password = 'penEbYs'
new_customer_id = ''

def setup_module(module):
    global driver
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False
    driver = Ie(capabilities=caps)
    driver.get('demo.guru99.com/V4/')


def test_login():
    login_page = LoginPage(driver)
    login_page.login_user(username=manager_username, password=manager_password)
    main_page = MainPage(driver)
    assert manager_username in main_page.manager_id_label.text


def test_new_customer():
    new_customer_page = NewCustomerPage(driver)
    new_customer_page.open()
    new_customer_page.add_customer(data={'customer_name' : 'Name Surname',
                                         'gender' : 'female',
                                         'date_of_birth' : '01.03.1995',
                                         'address' : 'klonowa 4',
                                         'city' : 'Gdansk',
                                         'state' : 'randomstate',
                                         'pin' : '123456',
                                         'mobile_number' : '111222333',
                                         'email' : 'mail' + time.strftime("%H%M%S") + '@mail.pl',
                                         'password' : manager_password})

    customer_registered_page = CustomerRegisteredSuccessfullyPage(driver)
    assert customer_registered_page.get_title() == 'Customer Registered Successfully!!!'
    global new_customer_id
    new_customer_id = customer_registered_page.get_customer_id()


def test_delete_customer_success():
    delete_customer_page = DeleteCustomerPage(driver)
    delete_customer_page.open()
    alert_text = delete_customer_page.delete_customer(customer_id=new_customer_id)
    assert alert_text == 'Customer deleted Succesfully'


def test_delete_customer_fail():
    delete_customer_page = DeleteCustomerPage(driver)
    delete_customer_page.open()
    alert_text = delete_customer_page.delete_customer(customer_id=new_customer_id)
    assert alert_text == 'Customer does not exist!!'


def teardown_module(module):
    global driver
    # driver.quit()
    driver = None
