# -*- coding: utf-8 -*-
from userInterFace.common import BasePage
from userInterFace.Elements.elements import TextElement, ClickableElement, BasePageElement, HoverableElement, \
    ListElement
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """A class representing the home page
        https://demoqa.com/"""
    elements_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    forms_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]')
    alerts_frame_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]')
    widgets_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]')
    interactions_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]')
    application_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]')

class ListsSectionPage(BasePage):
    elements2_btn = ClickableElement(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[1]')
    forms2_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[2]')
    alerts2_frame_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[3]')
    widgets2_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[4]')
    interactions2_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[5]')
    application2_btn = ClickableElement(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[6]')


class ListItemsElementsPage(BasePage):
    tex_box_btn = ClickableElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[1]')
    check_box_btn = ClickableElement(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[2]')
    radio_button_btn = ClickableElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[3]')
    web_tables_btn = ClickableElement(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[4]')
    buttons_btn = ClickableElement(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[5]')
    links_btn = ClickableElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[6]')
    broken_links_btn = ClickableElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[7]')
    upload_download_btn = ClickableElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[8]')
    dynamic_btn = ClickableElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[9]')

class TextBoxPage(BasePage):
    full_name_text_element = TextElement(By.XPATH, '//*[@id="userName"]')
    email_text_element = TextElement(By.XPATH,'//*[@id="userEmail"]')
    current_address_text_element = TextElement(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/textarea')
    permanent_address_text_element = TextElement(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/textarea')
    submit_btn = ClickableElement(By.XPATH,'//*[@id="submit"]')
    response_full_name_text_element = TextElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[1]')
    response_email_text_element = TextElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[2]')
    response_current_address = TextElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]')
    response_permanent_address = TextElement(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]')

