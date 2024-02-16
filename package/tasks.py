from celery import shared_task
from .models import Package, Day
from bs4 import BeautifulSoup as bs
import requests

@shared_task
def create_soup_instance_task(url):
    html_page = requests.get(url).text
    soup = bs(html_page,'lxml')
    return soup

@shared_task
def scrape_trip_url_task(url):
    soup = create_soup_instance_task(url)
    divs = soup.find_all('div', class_='card-product__action')
    hrefs=[]
    i=0
    for div in divs:
        href = 'https://intrepidtravel.com'+ div.find('a')['href']
        if '/en/tailor-made' not in href:
            hrefs.append(href)
    return hrefs

@shared_task
def scrape_day_task(soup, trip):
    divs = soup.find_all(attrs={"data-cy":"trip-itinerary-day"})
    titles = []
    contents = []
    for div in divs:
        #get title
        titles.append(div.find('b').text)
        #get content
        contents.append(div.find('p').text) 
    day_plan = dict(zip(titles, contents))
    for key, value in day_plan.items():
        Day.objects.create(title=key, content=value, package=trip)
    return day_plan

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
            title = soup.find('h1', class_='l-container sm:u-text-align--center u-margin-bottom--1 u-margin-top--3').text
            #get destination
            destination = soup.find('span', class_='trip-summary__destination').text.replace(",", "") 
            #get price
            price = soup.find(attrs={"data-cy": "price-value"}).text
            price_float = float(price.replace(",", "").replace("$", ""))
            #get duration
            duration = soup.find('h2', class_='headline--4 u-padding-bottom--1 u-margin-top--0 u-margin-bottom--0 sm:u-text-align--center').text.replace("\n", "")
            #create object
            trip_obj = Package.objects.create(title=title, destination=destination, price=price_float, duration=duration[9:16])
            #get trip plan as dictionary and save day plan in database
            trip_plan = scrape_day_task(soup,trip_obj)
        except:
            continue
        


