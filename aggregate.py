import requests
import bs4

url = r"https://www.musixmatch.com/explore/genre/Hip-Hop-Rap"

r = requests.get(url, headers={'User-Agent': 'Custom'})

soup = bs4.BeautifulSoup(r.content, 'html.parser')
a_tags = (soup.findAll("a", {'class': "title"}, href=True))

links = []
for a in a_tags:
	links.append(f"https://www.musixmatch.com{a['href']}")

with open('lyrics.txt', 'w') as f:
	for link in links:
		r = requests.get(link, headers={'User-Agent': 'Custom'})
		soup = bs4.BeautifulSoup(r.content, 'html.parser')
		lyrics = (soup.findAll("span", {'class': "lyrics__content__ok"}))
		for item in lyrics:
			f.write(item.text.encode("ascii", 'ignore').decode('utf-8'))
