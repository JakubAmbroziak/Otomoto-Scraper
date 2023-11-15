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
            mileage = soup.find('dd', {'data-parameter': 'mileage'}).text.strip()



            # Print or save the extracted information
            print(f"{title} Cena {price} Przebieg: {mileage}")
        except Exception as e:
            #print(e)
            pass
    

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
