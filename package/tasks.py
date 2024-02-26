from celery import shared_task
from .models import Package, Day, Hotel
from bs4 import BeautifulSoup as bs
import requests
import re

@shared_task
def create_soup_instance_task(url):
    html_page = requests.get(url).text
    soup = bs(html_page,'lxml')
    return soup

@shared_task
def scrape_trip_url_task(url):
    soup = create_soup_instance_task(url)
    divs = soup.find_all('div', class_='title')
    hrefs=[]
    for div in divs:
        href ='https://www.friendlyplanet.com'+ div.find('a')['href'] 
        print(href)
        hrefs.append(href)
    return hrefs

@shared_task
def scrape_day_task(soup, trip):
    divs = soup.find_all('div', class_='day')
    titles = []
    contents = []
    for div in divs:
        #get title
        titles.append(div.find('span',class_='itinDay').text)
        #get content
        contents.append(div.find('ul').text)
    day_plan = dict(zip(titles, contents))
    for key, value in day_plan.items():
        Day.objects.create(title=key, content=value, package=trip)
    return day_plan

@shared_task
def scrape_hotel_task(soup, trip):
    hotels=[]
    divs = soup.find_all('div', class_='expandoBlock hotel')
    for div in divs:
        hotels.append(div.find('div', class_='title').text)
        for hotel in hotels:
            Hotel.objects.create(title=hotel, package=trip)
    return hotels

@shared_task    
def scrape_trip_task(url):
    # Delete existing data
    Package.objects.all().delete()
    Day.objects.all().delete()

    #scrape new data
    links = scrape_trip_url_task(url)
    for link in links:
        try:
            soup = create_soup_instance_task(link)
            #get title
            title = soup.find('h1', class_='tourHead').text
            #get destination
            #destination = soup.find('span', class_='trip-summary__destination').text.replace(",", "") 
            #get price
            p= soup.find('span', class_='price').text
            price = int(''.join(re.findall(r'\d+', p)))
            #get duration
            duration = soup.find('span', class_='duration').text.replace('days','')
            #create object
            trip_obj = Package.objects.create(title=title, destination=title, price=price, duration=duration)
            #get trip plan as dictionary and save day plan in database
            trip_plan = scrape_day_task(soup,trip_obj)
            hotels = scrape_hotel_task(soup,trip_obj)
        except:
            continue
        


