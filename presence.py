from splinter import Browser

browser = Browser('chrome')
browser.visit('https://www.hltv.org/')

# Presence:
assert browser.is_element_present_by_css('a.navnews')
assert browser.is_element_present_by_xpath('//a[@class="big-image-news a-reset"]')
assert browser.is_element_present_by_tag('h1')
assert browser.is_element_present_by_name('viewport')
assert browser.is_element_present_by_text('Stats')
assert browser.is_element_present_by_value('Africa/Lagos')

# The opposite:
assert browser.is_element_not_present_by_id('some_id_that_does_not_exist')
assert browser.is_element_not_present_by_text('Holy Smite')


login = browser.find_by_cls('.navsignin')
login.click()

# Visibility (only css and xpath here):
assert browser.is_element_visible_by_css('#forgot-password-username', wait_time=3) 
assert browser.is_element_visible_by_xpath('//input[@class="loginCheckbox "]', wait_time=3)
