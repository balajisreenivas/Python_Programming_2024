import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://google.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now, you can use BeautifulSoup to extract data from the page
    # For example, let's extract all the links on the page
    links = soup.find_all('a')

    # Print the links
    for link in links:
        print(link.get('href'))
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)