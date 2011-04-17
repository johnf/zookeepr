from lettuce import after, before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

def is_executable(program):
    import os
    for path in os.environ["PATH"].split(os.pathsep):
        exe_file = os.path.join(path, program)
        if os.path.exists(exe_file) and os.access(exe_file, os.X_OK):
            return True

    return False

@before.all
def setup_browser():
    if is_executable('chromedriver'):
      world.browser = webdriver.Chrome()
    else:
      world.browser = webdriver.Firefox()


@after.all
def clowse_browser(total):
    world.browser.quit()
