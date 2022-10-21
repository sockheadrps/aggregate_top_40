import requests
import bs4

url = r"https://www.musixmatch.com/explore/genre/Country"
urls = [r"https://www.musixmatch.com/explore/genre/Country",
		r"https://www.musixmatch.com/explore/genre/Alternative",
		r"https://www.musixmatch.com/explore/genre/Dance",
		r"https://www.musixmatch.com/explore/genre/Pop",
		r"https://www.musixmatch.com/explore/genre/Rock"



]

for u in urls:
	r = requests.get(u, headers={'User-Agent': 'Custom'})

	soup = bs4.BeautifulSoup(r.content, 'html.parser')
	a_tags = (soup.findAll("a", {'class': "title"}, href=True))

	print(a_tags)
	links = []
	for a in a_tags:
		links.append(f"https://www.musixmatch.com{a['href']}")
		print(a)

	with open('lyrics.txt', 'a') as f:
		for link in links:
			r = requests.get(link, headers={'User-Agent': 'Custom'})
			soup = bs4.BeautifulSoup(r.content, 'html.parser')
			lyrics = (soup.findAll("span", {'class': "lyrics__content__ok"}))
			for item in lyrics:
				print(item)
				f.write(item.text.encode("ascii", 'ignore').decode('utf-8'))



