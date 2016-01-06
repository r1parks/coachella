#!/usr/bin/env python

from selenium import webdriver

def get_div_info(browser):
    divs = browser.find_elements_by_tag_name('div')
    return {(div.get_attribute('id'), div.get_attribute('class')) for div in divs}

def run():
    browser = webdriver.Firefox()
    browser.get('https://www.coachella.com')
    divs = get_div_info(browser)
    for _ in range(10):
        browser.get('https://www.coachella.com')
        new_divs = get_div_info(browser)
        if new_divs != divs:
            sys.exit(0)

if __name__ == '__main__':
    run()

