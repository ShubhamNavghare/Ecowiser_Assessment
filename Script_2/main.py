# First importing the necessary modules to complete the Task

from bs4 import BeautifulSoup
from requests import get

# URL from where the data to be extracted
url = ""  

# Passing the url for web scarping
data = get(url)

# Creating a soup which contains data of the URL
soup = BeautifulSoup(data.content)