import os
import hashlib
import unittest
from adduser import add_user
from selenium import webdriver

class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        os.system("sqlite3 quiz.db < quiz.sql")
        add_user("jonas", hashlib.md5("jonas".encode()).hexdigest(), "user")


    def test_login_success(self):
        driver = self.driver
        driver.get("http://jonas:jonas@localhost")
        assert driver.find_element_by_id("navbarsExampleDefault")

    def test_login_fail(self):
        driver = self.driver
        driver.get("http://jonas:jonas1@localhost")

        assert driver.page_source == '<html><head></head><body></body></html>'

    def test_quiz_with_right_answer(self):
        driver = self.driver
        driver.get("http://jonas:jonas@localhost")

        with open("sample.py", 'w+') as file:
            file.write('''def desafio1(number): return 0''')
        
        driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/sample.py")
        driver.find_element_by_xpath('//button[text()="Enviar"]').click()
        assert driver.find_elements_by_tag_name("td")[2].text == 'OK!'

        os.system("rm sample.py")

    
    def test_quiz_with_wrong_answer(self):
        driver = self.driver
        driver.get("http://jonas:jonas@localhost")

        with open("sample.py", 'w+') as file:
            file.write('''def desafio1(number): return 1''')
        
        driver.find_element_by_id("resposta").send_keys(os.getcwd()+"/sample.py")
        driver.find_element_by_xpath('//button[text()="Enviar"]').click()
        assert driver.find_elements_by_tag_name("td")[2].text == 'Erro'

        os.system("rm sample.py")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    

