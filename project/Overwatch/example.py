from selenium.webdrive import chrome
from bs4 import BeautifulSoup
import pandas as pd
import time


#%%
import requests

## 자신의 Client ID와 Client Secret 입력
CLIENT_ID = '87cf4b880c7343238bb5472a1c0080d5'
CLIENT_SECRET = '9hkYXBAPHhVFI8aNAbpug5b5V4Q36DpP'

def get_spotify_access_token(client_id, client_secret):
    
    url = 'https://develop.battle.net/access/clients'

    auth_data = {'grant_type': 'client_credentials',
                  'client_id': client_id,
                  'client_secret': client_secret}
        
    r = requests.post(url, data=auth_data) # POST 방법으로 응답을 요청
    r_token = r.json() # 응답 객체의 text 부분을 JSON 형식으로 변환
    
    return r_token['access_token']

#%%

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls=['https://blog.scrapinghub.com']
    
    def parse(self, response):
        for title in response.css('.post_header>h2'):
            yield{'title':title.css('a::text').get()}
            
        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)
            