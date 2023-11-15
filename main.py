import requests
import asyncio
from bs4 import BeautifulSoup
from car import *
from cars_math import *
import re

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
def scrape_cars_on_page(soup):
    car_ads = soup.find_all('article')
    for car_ad in car_ads:
        try:
            # Extract information within each car ad div
            title = car_ad.find('h1').a.text.strip()
            price = car_ad.find('h3').text.strip()
            mileage = car_ad.find('dd', {'data-parameter': 'mileage'}).text.strip()
            fuel_type = car_ad.find('dd', {'data-parameter': 'fuel_type'}).text.strip()
            gearbox = car_ad.find('dd', {'data-parameter': 'gearbox'}).text.strip()
            year = car_ad.find('dd', {'data-parameter': 'year'}).text.strip()

            # Find the p element containing 'cm3'
            capacity_element = None
            for p_element in car_ad.find_all('p'):
                if 'cm3' in p_element.text:
                    capacity_element = p_element
                    break

            if capacity_element:
                # Use regular expression to extract capacity information
                capacity_matches = re.findall(r'\b\d+\s?\d*\s?cm3\b', capacity_element.text)

                if capacity_matches:
                    capacity = capacity_matches[0]
                    car = Car(title, price, mileage, fuel_type, gearbox, year, capacity)
                    print(car)
                    cars_list.add(car)
        except (AttributeError, TypeError) as e:
            #print(f"Error extracting information (Attribute or Type Error): {e}")
            pass
        except Exception as e:
            print(f"Error extracting information: {e}")

        
def get_total_pages(url):
    soup = scrape_page(url)
    if soup:
        # Extract the total number of pages (adjust the selector as needed)
        pagination_items = soup.find_all('li', {'data-testid': 'pagination-list-item'})
        
        if pagination_items:
            last_page_element = pagination_items[-1]
            total_pages = int(last_page_element.find('span').text.strip())
            return total_pages
        else:
            return 1  # If there is no pagination, assume a single page
    else:
        return 0


cars_list = CarList()
async def scrape_and_process(base_url, start_page):
    url = f"{base_url}{start_page}"
    total_pages = get_total_pages(url)

    if total_pages > 0:
        for page_number in range(start_page, total_pages + 1):
            url = f"{base_url}{page_number}"
            soup = scrape_page(url)

            if soup:
                cars_on_page = scrape_cars_on_page(soup)

                if cars_on_page:
                    cars_list.extend(cars_on_page)
            else:
                print(f"Failed to scrape page {page_number}")
    else:
        print("Failed to get the total number of pages.")
    
    return cars_list

async def main():
    base_url = "https://www.otomoto.pl/osobowe/audi/90?page="
    start_page = 1

    cars = await scrape_and_process(base_url, start_page)

    # Additional code to be executed after scraping
    print("All scraping is done. Now processing the cars:")
   # for car in cars:
       # print(car)
    cars.calculate_average_price()
    cars.calculate_average_year()
    cars.calculate_median_capacity()

# Run the asynchronous main function
asyncio.run(main())