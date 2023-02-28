from userInterFace.Actions.actions import *
from constants import *
import time

def test_application(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=application)



