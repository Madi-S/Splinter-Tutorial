from splinter import Browser

browser = Browser(headless=True, incognito=True)
browser.visit('https://www.hltv.org/forums/threads/2402923/boredom')

print(dir(browser.cookies))
print(browser.cookies.all())  # Show all cookies

my_cookie = {'foo': 'bar'}
browser.cookies.add(my_cookie)  # Set cookies via mapping

print(browser.cookies.all())
print(browser.cookies.all().get('foo')) # Get spicific cookie or `None`

browser.cookies.delete('foo')   # Delete special cookie

print(browser.cookies.all())

browser.cookies.delete()    # Delete all cookies

print(browser.cookies.all())