from selenium import webdriver
from parsed_data.modules.cafe_crawling import parse_cafe
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_parser.settings")
django.setup()
from parsed_data.models import CafeData

if __name__ == '__main__':
    # Download chromedriver location setting
    driver = webdriver.Chrome('/Users/byeun/Downloads/chromedriver')
    driver.implicitly_wait(3) # Delay for web loading
    try:
        # url access
        driver.get('https://cafe.naver.com/joonggonara')
        data = parse_cafe(driver, '컴퓨터', '07:00')

        for t in data:
            CafeData(title=t.title, link=t.link, time=t.time).save()

    # the end of work
    finally:
        driver.quit()