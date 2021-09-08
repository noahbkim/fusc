import datetime
import time
from selenium import webdriver
from typing import Any


class ReservationDriver:
    """Stateful wrapper for Selenium interactions."""

    driver: webdriver.Firefox

    def __init__(self, driver_type: Any = webdriver.Firefox):
        """Create, set configuration."""

        self.driver = driver_type()
        self.driver.implicitly_wait(5)

    def login(self, username: str, password: str):
        """Go through authentication progress."""

        self.driver.get("https://myrecsports.usc.edu/booking")
        self.driver.find_element_by_id("loginLink").click()
        self.driver.find_element_by_id("frmExternalLogin")
        self.driver.execute_script("submitExternalLoginForm('Shibboleth')")
        self.driver.find_element_by_id("username").send_keys("noahbkim")
        self.driver.find_element_by_id("password").send_keys("she once was a true love of mine")
        self.driver.find_element_by_name("_eventId_proceed").click()
        self.driver.find_element_by_id("logoutForm")

    def set_reservation_target(self, uid: str):
        """Go to a specific reservation page."""

        self.driver.get(f"https://myrecsports.usc.edu/booking/{uid}")

    def reserve_slot(self, date: datetime.date, slot_number: str) -> bool:
        """Reserve a slot on the current page."""

        for option in self.driver.find_elements_by_class_name("single-date-select-button"):
            year = int(option.get_attribute("data-year"))
            month = int(option.get_attribute("data-month"))
            day = int(option.get_attribute("data-day"))

            if option.is_displayed() and year == date.year and month == date.month and day == date.day:
                option.click()
                time.sleep(1)

                for button in self.driver.find_elements_by_tag_name("button"):
                    if button.text.lower().strip() == "book now":
                        print(button.get_attribute("data-slot-number"))
                        if slot_number == button.get_attribute("data-slot-number"):
                            button.click()
                        time.sleep(0.5)
                        return True
                    else:
                        return False
