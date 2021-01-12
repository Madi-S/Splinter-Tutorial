from splinter import Browser

browser = Browser()

browser.visit('http://norvig.com/python-iaq.html')

browser.click_link_by_href('https://docs.google.com/document/pub?id=1dTAzkH8Cv9Kx0i8f2czAJ9ToKU54btObQGW86Xm5JO4')
browser.back()

browser.click_link_by_text('Java IAQ')
browser.back()

browser.click_link_by_partial_text('Legends')
browser.back()

# browser.click_link_by_id('id attribute value')

# browser.visit('https://www.google.com/recaptcha/api2/demo')
# browser.fill('input1', 'Jeff')
# 
# browser.check('radios')
# browser.uncheck('radios')
# browser.select('selector', 'value')
# browser.attach_file('name', '/path/to/some/file/test_splinter.py')
# browser.type('name', 'text to type', slowly=True)
# assert browser.find_by_css('h1.main').first.visible
# assert browser.find_by_name('name').first.has_class('my_class')