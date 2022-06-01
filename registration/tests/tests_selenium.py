from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By


class RegistrationPage(StaticLiveServerTestCase):

    def setUp(self):
        opts = ChromeOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                       chrome_options=opts)
        self.wait = WebDriverWait(self.driver, 30)

    def test_registration_page(self):

        self.driver.get(self.live_server_url + "/registration/")

        self.wait.until(cond.presence_of_all_elements_located)

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_username"]'
                                 ).send_keys("TestFirstname")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_first_name"]'
                                 ).send_keys("TestFirstname")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_last_name"]'
                                 ).send_keys("TestLastname")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_email"]'
                                 ).send_keys("TestUser@mail.com")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_password1"]'
                                 ).send_keys("deigibefopn465")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_password2"]'
                                 ).send_keys("deigibefopn465")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="registration-form"]/input[2]'
                                 ).click()
        self.wait.until(cond.url_changes)

        assert self.driver.current_url == self.live_server_url +\
            "/registration/login/"

    def tearDown(self):
        self.driver.close()
