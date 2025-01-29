import logging
from playwright.sync_api import Page
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.reject_all_button = page.get_by_role("button", name="Reject all")
        self.travel_mode = page.locator('[data-test*="SearchFormModesPicker"] button').nth(0)
        self.place_picker_input = page.locator('[data-test="PlacePickerInput-origin"] input')
        self.place_picker_text = page.locator('[data-test="PlacePickerInputPlace"]')
        self.place_destination_input = page.locator('[data-test="PlacePickerInput-destination"] input')
        self.popup = page.locator('[data-test="ModesPopup"]')
        self.popup_origin = page.locator('[data-test="PlacepickerModalOpened-origin"]')
        self.popup_destination = page.locator('[data-test="PlacepickerModalOpened-destination"]')
        self.date_picker = page.locator('input[name="search-outboundDate"]')
        self.place_selector = page.locator('[data-test="PlacePickerRow-station"]')
        self.choose_day = page.locator("[data-test='CalendarDay']")
        self.booking_checkbox = page.locator('[data-test="bookingCheckbox"] svg')
        self.set_dates = page.locator("[data-test='SearchFormDoneButton']")
        self.explore = page.locator("[data-test='LandingSearchButton']")
        self.new_data_picker_open = page.locator("[data-test='NewDatePickerOpen']")

    def navigate(self):
        logging.info("Navigating to homepage")
        self.page.goto("https://www.kiwi.com/en/")

    def fill_place_picker_input(self, text: str):
        logging.info(f"Filling departure picker input with: {text}")
        self.place_picker_input.fill(text)
        self.page.keyboard.press("Enter")
        self.popup_origin.wait_for(state="visible")

    def fill_destination_input(self, text: str):
        logging.info(f"Filling destination picker input with: {text}")
        self.place_destination_input.fill(text)
        self.page.keyboard.press("Enter")
        self.popup_destination.wait_for(state="visible")

    def select_place(self, place_name: str):
        option = self.place_selector.filter(has_text=place_name)
        option.click()

    def choose_travel_mode(self, mode: str):
        """
        Selects a travel mode (e.g., 'oneWay', 'return', 'multicity', or 'nomad').
        """
        self.travel_mode.click()
        valid_modes = ["oneWay", "return", "multicity", "nomad"]
        if mode not in valid_modes:
            raise ValueError(f"Invalid mode '{mode}'. Supported modes are: {', '.join(valid_modes)}")
        logging.info(f"Choosing travel mode: {mode}")
        mode_locator = self.page.locator(f'[data-test="ModePopupOption-{mode}"]')
        self.popup.wait_for(state="visible")
        mode_locator.click()
        self.popup.wait_for(state="hidden")

    def set_departure_date_new(self, days_in_future: int = 7):
        """
        Selects a departure date based on the exact `data-value` attribute.
        """
        today = datetime.today()
        target_date = today + timedelta(days=days_in_future)
        target_date_str = target_date.strftime("%Y-%m-%d")
        logging.info(f"Setting departure date to: {target_date_str}")
        self.date_picker.click()
        self.new_data_picker_open.wait_for(state="visible")
        day_locator = self.page.locator(f'[data-value="{target_date_str}"]')
        day_locator.click()

        self.set_dates.click()
        self.new_data_picker_open.wait_for(state="hidden")
