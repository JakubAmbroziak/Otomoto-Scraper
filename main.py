import requests
from bs4 import BeautifulSoup

url = "https://www.otomoto.pl/osobowe/audi"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Verify the class name and adjust if necessary
    car_titles = soup.find_all('a')

    # Check if any titles were found
    if car_titles:
        for title in car_titles:
            print(title.text.strip())
    else:
        print("No car titles found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
