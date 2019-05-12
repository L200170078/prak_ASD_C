from bs4 import BeautifulSoup
import requests

page = requests.get('https://en.wikipedia.org/wiki/Knowledge_Economic_Index')
soup = BeautifulSoup(page.text, 'html.parser')
td_start=2
td_max=7
if page.status_code==200:
	final=[]
	table = soup.findAll("tr")
	# print(table[141])
	final=[
			[
				table[1].findAll("th")[0].get_text(),
				table[1].findAll("th")[1].get_text(),
				table[1].findAll("th")[2].get_text(),
				table[1].findAll("th")[3].get_text(),
				table[1].findAll("th")[4].get_text(),
				table[1].findAll("th")[5].get_text(),
				table[1].findAll("th")[6].get_text()
			]
		]
	count=2
	while count<=141:
		# print(count)
		# negara=table[count].find("a").attrs['title']
		# x=table[count].findAll("td")[1].get_text()
		# print(table[count].findAll("td")[1].get_text())
		final+=[
				[
					table[count].find("a").attrs['title'],
					table[count].findAll("td")[1].get_text(),
					table[count].findAll("td")[2].get_text(),
					table[count].findAll("td")[3].get_text(),
					table[count].findAll("td")[4].get_text(),
					table[count].findAll("td")[5].get_text(),
					table[count].findAll("td")[6].get_text()
				]
			]
		count+=1
print(final)