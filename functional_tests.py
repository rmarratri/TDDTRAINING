from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()
MAX_WAIT = 10

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

print(browser.title)
assert 'The install worked successfully! Congratulations!' in browser.title
