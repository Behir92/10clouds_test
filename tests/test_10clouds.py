import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.GoogleMain import GoogleMain
from page_objects.TenCloudsMain import TenCloudsMain
from page_objects.TenCloudsCaseStudiesPage import TenCloudsCaseStudiesPage


class Test10Clouds:
    @pytest.fixture
    def driver(self, request):
        driver_ = webdriver.Firefox(executable_path="./geckodriver")

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_glucose_mama_screenshot(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        # Opening Google and assigning it to the driver
        driver.get('https://google.com')
        google = GoogleMain(driver)
        # Searching for 10 clouds and clicking the link
        google.search_bar.input_text_and_press_enter('10clouds')
        sleep(1)
        assert '10Clouds' in google.correct_link.get_inner_text()
        google.correct_link.click_element()
        # Finding the button for View All Cases and clicking on it
        cookie_button = wait.until(ec.presence_of_element_located((By.ID, 'cookies-hide')))
        ten_clouds_main = TenCloudsMain(driver)
        driver.execute_script('arguments[0].scrollIntoView(true);', ten_clouds_main.cases_section.webelement)
        if cookie_button.is_displayed():
            cookie_button.click()
        ten_clouds_main.cases_section.all_cases_button.click_element()
        sleep(5)
        # Asserting that GlucoseMama is on the list
        ten_clouds_case_studies = TenCloudsCaseStudiesPage(driver)
        all_cases = ten_clouds_case_studies.get_all_cases()
        all_case_names = ten_clouds_case_studies.get_all_case_names()
        assert "GlucoseMama" in all_case_names
        # Scrolling to have GlucoseMama in the viewport and taking a screenshot
        for case in all_cases:
            if "GlucoseMama" in case.get_attribute('innerText'):
                driver.execute_script('arguments[0].scrollIntoView(true);', case)
                driver.execute_script('window.scrollBy(0, -450);')
                cookie_button = wait.until(ec.presence_of_element_located((By.ID, 'cookies-hide')))
                if cookie_button.is_displayed():
                    cookie_button.click()
                sleep(5)
                driver.get_screenshot_as_file('glucose_mama_screenshot.png')
                break
