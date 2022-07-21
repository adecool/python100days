from selenium import webdriver
from selenium.webdriver.common.by import By




chrome_driver_path = r"C:\Users\Tobiloba\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get('https://www.amazon.com/dp/B0963P9QTM/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0')
#price = driver.find_element(By.CLASS_NAME, "a-price")
#print(price.text)

driver.get('https://www.python.org/')
#
# search = driver.find_element(By.NAME, 'q')
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text, bug_link.get_attribute('a'))
# print(search.tag_name)
#
# driver.find_elements(By.XPATH, '')

event_times  = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
events  = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')

event_dict = {}
# for i in range(len(event_times)):
#     for time in event_times:
#         for event in events:
#             event_dict[i] = f'{time.text}, {event.text}'

for n in range(len(event_times)):
    event_dict[n] = {
        'name': events[n].text,
        'time': event_times[n].text
    }
print(event_dict)




#driver.close()
driver.quit()
