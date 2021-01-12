from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


# using context manager
with Browser('chrome', retry_count=5, user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/6.1.6 Safari/537.78.2') as b:
    b.visit('https://www.udacity.com/course/linux-command-line-basics--ud595')
    
    # Locating elements:
    title = b.find_by_text('Linux Command Line Basics')
    print(title.query, 'text')

    title = b.find_by_xpath('//h1')
    print(title.text, 'xpath')

    title = b.find_by_tag('h1')
    print(title.text, 'tag name')

    title = b.find_by_css('.hero__course--title')
    print(title.text, 'css')

    try:
        title = b.find_by_name('title')
        print(title.text, 'name')
    except ElementDoesNotExist:
        pass

    # b.find_by_name('name').first
    # b.find_by_id('id').last
    # b.find_by_value('value').[3]

    button = b.find_by_text('Start Free Course')
    button.click()    

    # Locating links on the page:
    containing_https = b.links.find_by_partial_href('https')
    containing_a = b.links.find_by_partial_text('a')
    print(containing_https.query, containing_a.last.text)

    # Locating inside the tags:
    head = b.find_by_tag('head')
    title = head.find_by_tag('title').text
    print(title)