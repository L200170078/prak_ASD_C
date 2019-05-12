from bs4 import BeautifulSoup
import requests
import re

page = requests.get('https://id.wikipedia.org/wiki/Indonesia')
soup = BeautifulSoup(page.text, 'html.parser')
if page.status_code==200:
	coba = soup.get_text()
	cari = re.findall(r'di[\w\.-]+', coba)
	print(cari)