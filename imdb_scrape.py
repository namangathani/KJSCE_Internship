from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
# url2 = f'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'

# webpage = requests.get(url2)
# soup = BeautifulSoup(webpage.content, 'html.parser')
# title = soup.findAll('span', class_= '')

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
		for b in soup.select('td.posterColumn span[name=ir]')]



list = []

for index in range(0, len(movies)):
	movie_string = movies[index].get_text()
	movie = (' '.join(movie_string.split()).replace('.', ''))
	movie_title = movie[len(str(index))+1:-7]
	year = re.search('\((.*?)\)', movie_string).group(1)
	place = movie[:len(str(index))-(len(movie))]
	data = {"place": place,
			"movie_title": movie_title,
			"rating": ratings[index],
			"year": year,
			"star_cast": crew[index],
			}
	list.append(data)

for movie in list:
	print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
		') -', 'Starring:', movie['star_cast'], movie['rating'])


df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv',index=False)
