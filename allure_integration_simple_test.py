import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


class TestInternetPage():

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    @allure.story('Проверяем название вкладки Google')
    @allure.feature('Open Google')
    @allure.severity('Blocker')
    def test_chrome(self):
        self.driver.get('https://google.com')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert 'Google' in self.driver.title

    @allure.story('Проверяем название вкладки Yandex')
    @allure.feature('Open Yandex')
    @allure.severity('Critical')
    def test_yandex(self):
        self.driver.get('https://yandex.ru')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert 'Дзен' in self.driver.title, 'Ошибка в названии вкладки'

    @allure.story('Проверяем название вкладки Mail')
    @allure.feature('Open Mail')
    @allure.severity('Minor')
    def test_mail(self):
        self.driver.get('https://mail.ru')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert 'Mail' in self.driver.title
