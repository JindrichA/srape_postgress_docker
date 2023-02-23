import json
import re
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)



class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=50&page=:{i}"for i in range(10)]

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.items = []
        with open('../../static/data.json', 'w') as f:
             pass
        self.dict_of_urls_and_img = []

    def parse(self, response):
        self.driver.get(response.url)
        self.html_content = self.driver.page_source
        self.items.append(self.html_content)
        #print("TAD")
        #print(self.items)
        string = self.html_content

        jeden_inzerat_start = r'{"dynamicDown":'
        jeden_inzerat_end = r'"_links": '
        pattern_inzerat = f"{jeden_inzerat_start}(.*?){jeden_inzerat_end}"
        matches_inzerat = re.findall(pattern_inzerat, string)

        for match_inzerat in matches_inzerat:
            start = r'"rus": false, "name": '
            end = r'"region_tip":'
            pattern = f"{start}(.*?){end}"
            matches = re.findall(pattern, match_inzerat)
            for match in matches:
                print(match)
            start_img = 'https://'
            end_img = r'.jpeg'
            pattern_img = f"{start_img}(.*?){end_img}"
            matches_img = re.findall(pattern_img, match_inzerat)
            for match in matches_img:
                print(start_img + match + end_img + '?fl=res,400,300,3|shr,,20|jpg,90"')

            new_record = {
                "title": matches[0],
                "url": 'https://sreality.cz',
                "image": start_img + matches_img[0] + end_img + '?fl=res,400,300,3|shr,,20|jpg,90'
            }
            self.dict_of_urls_and_img.append(new_record)


    def closed(self, reason):

        with open('../../static/data.json', 'a') as f:
                json_data = json.dumps(self.dict_of_urls_and_img)
                f.write(json_data)
        self.driver.quit()