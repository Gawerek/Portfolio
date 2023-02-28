# -*- coding: utf-8 -*-
from conftest import webdriver
from userInterFace.Pages import pages
import time
from constants import *
from selenium.webdriver.common.action_chains import ActionChains




def select_section_on_home_page(webdriver, section):
    home_page = pages.HomePage(webdriver)
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
    list_section_page = pages.ListsSectionPage(webdriver)
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
    element_list_page= pages.ListItemsElementsPage(webdriver)
    if element == "text_box":
        element_list_page.tex_box_btn.click()
        time.sleep(5)

