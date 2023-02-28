import time

from userInterFace.Actions.actions import *
from constants import *

def test_elements_text_box(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element="text_box")
    time.sleep(5)

