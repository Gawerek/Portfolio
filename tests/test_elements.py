import time
import pytest

from userInterFace.Actions.actions import *
from constants import *
from data.structure.test_data import *


# How it could work with @pytest.mark.parametrize

# @pytest.mark.parametrize("element", [text_box, radio_button, broken])
# def test_elements_text_box(webdriver, element):
#     webdriver.get(base_url)
#     select_section_on_home_page(webdriver, section=elements)
#     select_list_to_show_items(webdriver, section=elements)
#     select_element_on_elements_list(webdriver, element=element)
#     time.sleep(5)

def test_elements_text_box(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=text_box)
    this_text_box_data = TextBoxData(full_name=text_box_dict["full_name"], current_address=text_box_dict["current_address"], \
                                     email=text_box_dict["email"], permanent_address=text_box_dict["permanent_address"])
    fill_text_box_with_data(webdriver, this_text_box_data)
    print(this_text_box_data.__dict__)





def test_elements_check_box(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=check_box)


def test_elements_radio_button(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=radio_button)


def test_elements_web_tables(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=web_tables)


def test_elements_buttons(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=buttons)


def test_elements_links(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=links)


def test_elements_broken_links(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=broken_links)


def test_elements_upload_download(webdriver):
    webdriver.get(base_url)
    select_section_on_home_page(webdriver, section=elements)
    select_list_to_show_items(webdriver, section=elements)
    select_element_on_elements_list(webdriver, element=upload_download)


# def test_elements_dynamic(webdriver):
#     webdriver.get(base_url)
#     select_section_on_home_page(webdriver, section=elements)
#     select_list_to_show_items(webdriver, section=elements)
#     select_element_on_elements_list(webdriver, element=dynamic)
