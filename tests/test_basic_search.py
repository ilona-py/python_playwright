from pytest_bdd import given, when, then, scenarios

scenarios("basic_search.feature")


@given("As an not logged user navigate to homepage https://www.kiwi.com/en/")
def step_navigate_to_homepage(home_page, page):
    home_page.navigate()
    page.wait_for_load_state('load')
    home_page.reject_all_button.click()


@when("I select one-way trip type")
def step_select_one_way_trip(home_page):
    home_page.choose_travel_mode("oneWay")
    assert home_page.travel_mode.text_content() == 'One-way'


@when("Set as departure airport RTM")
def step_set_departure_airport(home_page):
    home_page.fill_place_picker_input("RTM")
    home_page.select_place("RTM Rotterdam The Hague")
    assert 'Rotterdam RTM' in home_page.place_picker_text.text_content()


@when("Set the arrival Airport MAD")
def step_set_arrival_airport(home_page):
    home_page.fill_destination_input("MAD")
    home_page.select_place("MAD Adolfo Suárez Madrid–Barajas")
    assert 'Madrid MAD' in home_page.place_picker_text.nth(1).text_content()


@when("Set the departure time 1 week in the future starting current date")
def step_set_departure_time(home_page):
    home_page.set_departure_date_new()


@when("Uncheck the `Check accommodation with booking.com` option")
def step_uncheck_booking_option(home_page):
    home_page.booking_checkbox.click()


@when("Click the search button")
def step_click_search(home_page, page):
    home_page.explore.click()
    page.wait_for_load_state('load')


@then("I am redirected to search results page")
def step_verify_search_results(home_page):
    assert home_page.page.url.startswith("https://www.kiwi.com/en/search"), "Search results page not displayed"
