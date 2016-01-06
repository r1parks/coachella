#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_div_info(browser):
    divs = browser.find_elements_by_tag_name('div')
    return {(div.get_attribute('id'), div.get_attribute('class')) for div in divs}

def run():
    browser = webdriver.Firefox()
    browser.get('https://www.coachella.com')
    browser.set_window_size(1, 1)
    divs = get_div_info(browser)
    while True:
        print 'refreshing...'
        browser.refresh()
        new_divs = get_div_info(browser)
        if new_divs != divs:
            print "FOUND SOMETHING!!! OMG!!!"
            browser.maximize_window()
            break


if __name__ == '__main__':
    run()
