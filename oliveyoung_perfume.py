import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



sorting = [['01','<인기 순>'],['03','<판매 수량 순>'],['06','<높은 가격 순>']]
    

# 기존 : G마켓의 마스크 상품 정보
print("< 올리브영의 여성 향수 TOP 5 >")
    
for sort in sorting:
    URL = "https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100050003&fltDispCatNo=&prdSort=" + sort[0]
    raw = requests.get(URL)
    
    html = bs4.BeautifulSoup(raw.text, 'html.parser')
    
    box = html.find('div', {'id' : 'Contents'})
    items = box.find_all('div', {'class' : 'prd_info'})
    

    print(sort[1])

    num = 1
    for item in items[:5]:
        title = item.find('p', {'class' : 'tx_name'})
        price = item.find('span', {'class' : 'tx_num'})
        print(num, "위 : ", title.text)
        print('=>', price.text, '원')
        num += 1
    print()