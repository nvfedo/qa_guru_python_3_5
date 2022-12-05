from selene.support.shared import browser
import pytest

@pytest.fixture()
def practice_form_open_browser():
    #browser.config.hold_browser_open = True
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()