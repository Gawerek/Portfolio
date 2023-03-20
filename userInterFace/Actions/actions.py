# -*- coding: utf-8 -*-
from conftest import webdriver
from data.structure.test_data import TextBoxData
from userInterFace.Pages.pages import *
import time
from constants import *

from selenium.webdriver.common.action_chains import ActionChains




def select_section_on_home_page(webdriver, section):
    home_page = HomePage(webdriver)
    if section == elements:
        home_page.elements_btn.click()
    elif section == forms:
        home_page.forms_btn.click()
    elif section == alerts:
        home_page.alerts_frame_btn.click()
    elif section == widgets:
        home_page.widgets_btn.click()
    elif section == interactions:
        home_page.interactions_btn.click()
    elif section == application:
        webdriver.execute_script("arguments[0].scrollIntoView();", home_page.application_btn)
        home_page.application_btn.click()

def select_list_to_show_items(webdriver, section):
    list_section_page = ListsSectionPage(webdriver)
    if section == elements:
        list_section_page.elements2_btn.click()
    elif section == forms:
        list_section_page.forms2_btn.click()
    elif section == alerts:
        list_section_page.alerts2_frame_btn.click()
    elif section == widgets:
        list_section_page.widgets2_btn.click()
    elif section == interactions:
        list_section_page.interactions2_btn.click()
    elif section == application:
        list_section_page.application2_btn.click()



def select_element_on_elements_list(webdriver, element):
    element_list_page = ListItemsElementsPage(webdriver)
    if element == text_box:
        element_list_page.tex_box_btn.click()
    elif element == check_box:
        element_list_page.check_box_btn.click()
    elif element == radio_button:
        element_list_page.radio_button_btn.click()
    elif element == web_tables:
        element_list_page.web_tables_btn.click()
    elif element == buttons:
        element_list_page.buttons_btn.click()
    elif element == links:
        element_list_page.links_btn.click()
    elif element == broken_links:
        element_list_page.broken_links_btn.click()
    elif element == upload_download:
        element_list_page.upload_download_btn.click()
    elif element == dynamic:
        element_list_page.dynamic_btn.click()


def fill_text_box_with_data(webdriver, text_box_data: TextBoxData):
    text_box_page = TextBoxPage(webdriver)
    text_box_page.full_name_text_element = text_box_data.full_name
    text_box_page.email_text_element = text_box_data.email
    text_box_page.permanent_address_text_element = text_box_data.permanent_address
    text_box_page.current_address_text_element = text_box_data.current_address
    text_box_page.submit_btn.location_once_scrolled_into_view
    text_box_page.submit_btn.click()

    response_full_name = text_box_page.response_full_name_text_element
    response_full_name_text = response_full_name.text

    response_email = text_box_page.email_text_element
    response_email_text = response_email.get_attribute('value')

    response_current_address = text_box_page.response_current_address
    response_current_address_text = response_current_address.text

    response_permanent_address = text_box_page.response_permanent_address
    response_permanent_address_text = response_permanent_address.text

    full_name_value = text_box_page.full_name_text_element.get_attribute('value')
    email_value = text_box_page.email_text_element.get_attribute('value')
    current_address_value = text_box_page.current_address_text_element.get_attribute('value')
    permanent_address_value = text_box_page.permanent_address_text_element.get_attribute('value')


    assert fr"Name:{full_name_value}" == response_full_name_text
    assert f"{email_value}" == response_email_text
    assert f"Current Address :{current_address_value}" == response_current_address_text
    assert f"Permananet Address :{permanent_address_value}" == response_permanent_address_text


