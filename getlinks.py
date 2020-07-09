import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def get_links(links):
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get(links)
    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")
    no_of_pagedowns = 15

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns -= 1
    post_elems = browser.find_elements_by_class_name("job__spacing")

    list_of_links = []
    for elements in post_elems:
        a_element = elements.find_element_by_tag_name("a")
        link = a_element.get_attribute("href")
        list_of_links.append(str(link))

    return list_of_links
