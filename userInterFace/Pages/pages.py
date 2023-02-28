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
    tex_box_btn = ClickableElement(By.XPATH, '//*[@id="item-0"]')
    check_box_btn = ClickableElement(By.XPATH,'//*[@id="item-1"]')
    radio_button_btn = ClickableElement(By.XPATH, '//*[@id="item-2"]')
    web_tables_btn = ClickableElement(By.XPATH,'//*[@id="item-3"]')
    buttons_btn = ClickableElement(By.XPATH,'//*[@id="item-4"]')
    links_btn = ClickableElement(By.XPATH, '//*[@id="item-5"]')
    broken_links_btn = ClickableElement(By.XPATH, '//*[@id="item-6"]')
    upload_download_btn = ClickableElement(By.XPATH, '//*[@id="item-7"]')
    dynamic_btn = ClickableElement(By.XPATH, '//*[@id="item-8"]')