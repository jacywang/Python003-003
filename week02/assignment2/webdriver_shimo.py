from selenium import webdriver
from time import sleep

try:
  browser = webdriver.Chrome()

  browser.get('https://shimo.im/login?from=home')
  sleep(1)

  # Change to real email and password when running
  browser.find_element_by_name('mobileOrEmail').send_keys('example@gmail.com')
  browser.find_element_by_name('password').send_keys('example')
  sleep(1)
  browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

  print(browser.get_cookies())
  sleep(2)
except Exception as e:
  print(e)
finally:
  browser.close()