from __future__ import print_function
import time

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
import winsound

change_in_output = datetime.now().strftime("%M")
duration = 1000  # milliseconds
freq = 440  # Hz
loading_dots="..."

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
driver_path = r"<chrome driver file path>"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--headless")
honeygain = webdriver.Chrome(service=chrome_service, options=chrome_options)

# navigate to a webbsite
honeygain.get('https://dashboard.honeygain.com/login')
honeygain.execute_script("window.localStorage.setItem('JWT','eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NjkyNjk3MzIsImV4cCI6MTcwMDgwNTczMiwicm9sZXMiOlsiUk9MRV9VU0VSIiwiUk9MRV9UT1NfQUNDRVBURUQiLCJST0xFX0NPTkZJUk1FRF9FTUFJTCJdLCJlbWFpbCI6ImtpcnVzbm92YXJAZ21haWwuY29tIn0.U46o2gen09zKjSTqfp-Mxzl4TZ8F8uxR3_vGV1jrdbnNlZTvMYANpg4srNA-igd-7c5kNIgKxDiUYLcnuzaje_FSIQqu7AezEmg6SSbYpy-nsYZDEgmBjBXlFasfb_wgA-VNF9h8wLoFirQ9pbOUTWT685a5xTHeDtUef30fGf0MVWa8iC1nrku_IZ7g17zAZjmur7sziD64dNgWXid2iv6_j5bo3HSIwMZX5ELtGNK9Zuq8LSS6Jh7ZDdIGoaC0Zjl4Jg7xgIAuygcIbZr17XZgNWko9E7MXWjCNyx371ZZgQ5aoHNlcPu2Rh1xIeh1uj_KTBpVSw4MHIWA9Sr5N-ScJ4qDZKvH-VTt9WPjckzeuOKNWAjze9Np8wG0C4b-lsd29LFvldyigWUuVvraSxx3xgHcwZLppqNQ4MgK6A5hM89VqkjcpjFMsV7pRAk-6yagMJkHqoqqvedzGW6MLAf2K5w_7SVd4WqfODuGcKUuITTvM6m2lEYa3sorksrctsYKey06s6Kqlaru_MPeizAv4lQ24fDHgmpDHYtoEBjyvlPFoUTnIYeLu5CIQdmrjzknkasKuZXL9-vg-awH0pmWj6MZ22Hi56PNftHHRWMkmmjxp67__rMqB32gO5vs0hUk-uirzYQ9P3Ir0gOnBIGr-5upZcUemo_k-cvKIPk');")
honeygain.refresh()
time.sleep(5)
print(honeygain.find_element(By.XPATH, "//div[@class='sc-dkrFOg jgIGAb']").text)

print("  total       Daily     ACTIVE_DEVICES")
diff = "0"
while(True):

    total = honeygain.find_element(By.XPATH, "//div[@class='sc-dkrFOg jgIGAb']").text
    daily = honeygain.find_element(By.XPATH, "//div[@class='sc-dkrFOg gyXphO']").text
    ACTIVE_DEVICES = honeygain.find_element(By.XPATH, "/html/body").text

    Count = ACTIVE_DEVICES.count("Seen")
    active = 3 - int(Count)

    # print(ACTIVE_DEVICES[509:len(ACTIVE_DEVICES) - 1159])

    prev_time = datetime.now().strftime("%M")
    # print("", end=f"\r{total,daily+'+'+str(diff),active}")
    # print("Daily", end=f"\r{daily}")

    honeygain.refresh()
    time.sleep(5)
    daily1 = honeygain.find_element(By.XPATH, "//div[@class='sc-dkrFOg gyXphO']").text
    if daily1 == daily:
        print("", end=f"\rtime: {datetime.now().strftime('%H:%M:%S')} ")
    else:
        print("", end=f"\rchanged")
        winsound.Beep(freq, duration)

        diff = float(daily1)-float(daily)
        next_time = datetime.now().strftime("%M")
        total_time = float(change_in_output) - float(next_time)
        change_in_output = next_time
        cpm = diff/total_time
        print("", end=f"\r{total, daily + '+' + str(diff), active}")
        print("changed+","%.2f" % diff,"time:","%.2f" % total_time)
