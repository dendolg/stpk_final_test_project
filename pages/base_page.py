from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how_to_find, locator_to_find):
        try:
            self.browser.find_element(how_to_find, locator_to_find)
        except NoSuchElementException:
            return False
        else:
            return True
