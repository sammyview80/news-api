import requests

from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.response import Response

from .models import NewsModel

NEWSCHANNEL = 'skysports'
URL = 'https://www.skysports.com/football/news'

BASE_LOCATOR = 'div.site-layout-secondary div.page-filters__offset div.news-list div.news-list__item'
TITLE = 'div.news-list__item div.news-list__body h4 a'
LINK = 'div.news-list__item div.news-list__body h4 a'
TIME = 'div.news-list__item div.news-list__body span'
NEWSTAG = 'div.news-list__item div.news-list__body a'
IMAGE = 'a.news-list__figure img'


def fetch_news():
    print('fetching news....')
    htmlPage = requests.get(URL).content
    htmlPageSoup = BeautifulSoup(htmlPage, 'html.parser')

    selectedPage = htmlPageSoup.select(BASE_LOCATOR)

    news = NewsModel.objects.all()
    news.delete()
    try:
        for page in selectedPage:
            title = page.select_one(TITLE).string
            link = page.select_one(LINK).get('href')
            timeStamp = page.select_one(TIME).string
            newsTag = page.select_one(NEWSTAG).string
            image = page.select_one(IMAGE).get('data-src')

            newsModelInstance = NewsModel()
            newsModelInstance.title = title
            newsModelInstance.link = link
            newsModelInstance.timeStamp = timeStamp
            newsModelInstance.newsTag = newsTag
            newsModelInstance.image = image

            newsModelInstance.save()

    except AttributeError:
        pass
