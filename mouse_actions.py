from splinter import Browser

with Browser() as b:
    b.visit('https://developer.mozilla.org/en-US/')
    
    button = b.find_by_css('.signin-link')
    button.mouse_over()     # Put the mouse above the element
    button.mouse_out()      # Put the mouse out of the element
    button.right_click()    # Right click the element
    button.click()          # Click the element
    # button.double_click   # Double click the element
    # button.drag_and_drop(`target`)    # Drag the element to the target element