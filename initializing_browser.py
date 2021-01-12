from splinter import Browser

browser = Browser()
browser.visit('https://github.com/Madi-S')

print(browser.url)
print(browser.title)
print(type(browser.html))

# browser.fill('input', 'Redis')
# button = browser.find_by_css('.js-selected-navigation-item.Header-link.mt-md-n3.mb-md-n3.py-2.py-md-3.mr-0.mr-md-3.border-top.border-md-top-0.border-white-fade-15')
# button.click()

if browser.is_text_present('Madi-S'):
    print('Everything is fine')
else:
    print('Cannot locate the text')

browser.quit()