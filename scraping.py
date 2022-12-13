import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlopen

# https://pixabay.com/ko/illustrations/search/%EC%98%A4%ED%94%88/
# https://pixabay.com/ko/images/search/blue%20orange/?manual_search=1

# import requests 
# from bs4 import BeautifulSoup 
# url = "https://www.pexels.com/ko-kr/search/blue%20orange/" 
# res = requests.get(url) 
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "img")

# headers = {"User-Agent": "[WhatIsMyBrowser에 나타난 나의 유저 정보]"}
# res = requests.get(url, headers=headers)

html1 = urlopen("https://www.pexels.com/ko-kr/search/blue%20orange/")
html2 = urlopen("https://unsplash.com/s/photos/blue-orange")
html3_1 = urlopen("https://pixabay.com/ko/images/search/blue%20orange/?manual_search=1")
html3_2 = urlopen("https://pixabay.com/ko/images/search/blue%20orange/?manual_search=2")
html3_3 = urlopen("https://pixabay.com/ko/images/search/blue%20orange/?manual_search=3")
html4_1 = urlopen("https://pixabay.com/ko/images/search/blue%20orange%20art/?manual_search=1")
html4_2 = urlopen("https://pixabay.com/ko/images/search/blue%20orange%20art/?manual_search=2")
html4_3 = urlopen("https://pixabay.com/ko/images/search/blue%20orange%20art/?manual_search=3")

bs4_objects1 = BeautifulSoup(html1, "html.parser")
bs4_objects2 = BeautifulSoup(html2, "html.parser")
bs4_objects3_1 = BeautifulSoup(html3_1, "html.parser")
bs4_objects3_2 = BeautifulSoup(html3_2, "html.parser")
bs4_objects3_3 = BeautifulSoup(html3_3, "html.parser")
bs4_objects4_1 = BeautifulSoup(html4_1, "html.parser")
bs4_objects4_2 = BeautifulSoup(html4_2, "html.parser")
bs4_objects4_3 = BeautifulSoup(html4_3, "html.parser")

async def scraping1(html):
    for link in bs4_objects1.find_all("img"):
        print(link.text.strip(), link.get("src"))

# async def fetch(url):
#     request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#     response = await loop.run_in_executor(None, urlopen, request)
#     page = await loop.run_in_executor(None, response.read)
#     return len(page)

# async def main():
#     futures = [asyncio.ensure_future(fetch(url)) for url in urls]
#     result = await asyncio.gather(*futures)                
#     print(result)


# begin = time()
# loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
# loop.run_until_complete(main())          # main이 끝날 때까지 기다림
# loop.close()                             # 이벤트 루프를 닫음
# end = time()