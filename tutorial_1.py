from splinter import Browser

browser = Browser()
browser.visit('https://github.com/Madi-S')

print(browser.url)
print(browser.status_code)
print(browser.title)
print(type(browser.html))