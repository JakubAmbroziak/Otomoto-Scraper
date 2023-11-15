import requests
from bs4 import BeautifulSoup

url = "https://www.otomoto.pl/osobowe/audi"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Verify the class name and adjust if necessary
    car_ads = soup.find_all('article')

    # Check if any titles were found
    
    for car_ad in car_ads:
        try:
            # Extract information within each car ad div
            title = car_ad.find('h1').a.text.strip()
            price = car_ad.find('h3').text.strip()
            mileage = car_ad.find('dd', {'data-parameter': 'mileage'}).text.strip()
            fuel_type = car_ad.find('dd', {'data-parameter': 'fuel_type'}).text.strip()
            gearbox = car_ad.find('dd', {'data-parameter': 'gearbox'}).text.strip()
            year = car_ad.find('dd', {'data-parameter': 'year'}).text.strip()
            capacity = car_ad.find('p').text.split('•')[0].strip()

            print(f"{title} {price} {mileage} {fuel_type} {gearbox} {year} {capacity}")


        except Exception as e:
            # Handle exceptions or ignore them
            #print(f"Error extracting information: {e}")
            pass

    

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
