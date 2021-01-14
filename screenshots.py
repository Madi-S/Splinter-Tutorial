from splinter import Browser

# Pillow must be installed

browser = Browser()
browser.visit('https://en.wikipedia.org/wiki/Mart%C3%ADn_Vizcarra')

# Take a full screenshot
screenshot_path = browser.screenshot(r'C:\Users\khova\Desktop\Python\Code\Splinter\Splinter-Tutorial\full_page.png',full=True)         

# Take a screenshot of an HTML element:
screenshot_path = browser.find_by_css('.infobox.vcard').screenshot(r'C:\Users\khova\Desktop\Python\Code\Splinter\Splinter-Tutorial\element.png') 

# Take an HTML snapshot:
screenshot_path = browser.html_snapshot(r'C:\Users\khova\Desktop\Python\Code\Splinter\Splinter-Tutorial\snapshot.png')

'''
Snapshot definition:

An HTML snapshot is a capture of a webpage. 
The snapshot contains the content of the page after it has been completely parsed, interpreted and rendered by the browser. 
The role of the HTML snapshot is to be interpretable and thus indexable without the need of executing any JavaScript code.
'''