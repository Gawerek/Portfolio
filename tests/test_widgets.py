from userInterFace.Actions.actions import *
from constants import *

def test_widgets_accordian(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=widgets)

