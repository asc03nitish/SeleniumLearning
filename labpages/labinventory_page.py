from selenium.webdriver.common.by import By


class InventoryPage:

    PAGE_TITLE = (By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")

    LOGOUT_LINK = (By.XPATH, "//*[@id='loop-container']/div/article/div[2]/div/div/div/a")

    def get_page_title(self, driver):
        return driver.find_element(*self.PAGE_TITLE).text

    def logout(self, driver):
        driver.find_element(*self.LOGOUT_LINK).click()

    def get_current_url(self, driver):
        return driver.current_url