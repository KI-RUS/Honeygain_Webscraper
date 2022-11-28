import time

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

def get_stat():
    text = browser.find_element(By.XPATH, "/html/body").text


    # reduced_string = re.sub(r'.', '', text, count=92)
    # print(reduced_string)


    size = len(text)
    # Slice string to remove last 3 characters from string
    mod_string = text[94:size - 680]
    print(mod_string)



# intialzie chrome service
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
driver_path = r"<chrome driver file path>"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

# navigate to a webbsite
browser.get('https://app.jumptask.io/home')
browser.execute_script("window.localStorage.setItem('JWT','eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzIwMDkzNDAsImlhdCI6MTY2OTQxNzM0MCwianRpIjoiZWNkOTRjYmMtYWZjMC00OGIyLTg0ZTgtNmRkN2RjZTdjZGYyIiwid2FsIjoiMHgwRDUzNjBCMUIzMUUwNTU5MDhkRmI3OGVjNkI5MUJlZThlZjBCOUE4In0.EEMztaLVt4twpmcXiOZFKKJSWLgqjaV8cBxcAhhNOHV7414DlAYTbKBhD5Yd_a85TUWYowxnnhNrlA4ni75YBg');")
browser.refresh()
time.sleep(3)


# print("DAILY: ",daily)
while(True):

    get_stat()
    time.sleep(180)
# while(True):
#     get_stat()
#     browser.refresh()
#     time.sleep(5)

# link to search field (input)
# search_field = browser.find_element(By.ID, 'id-search-field')
# search_field.clear()
# search_field.send_keys('Class datatype')

# click on Go button
# browser.find_element(By.NAME, 'submit').click()