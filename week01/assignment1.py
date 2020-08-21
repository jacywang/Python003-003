import requests
from bs4 import BeautifulSoup

# Movies info to export to csv
movies_dict = {'Name': [], 'Type': [], 'Release Date': []}

# Request info
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
headers = {'user-agent': user_agent}
url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
movies_list = soup.find_all('div', attrs={'class': 'movie-hover-info'})
for movie in movies_list[:10]:
  info = movie.find_all('div', attrs={'class': 'movie-hover-title'})
  movie_name = info[0].find('span', attrs={'class': 'name'}).text
  movie_type = info[1].text.split(':')[1].strip()
  movie_release_date = info[3].text.split(':')[1].strip()

  movies_dict['Name'].append(movie_name)
  movies_dict['Type'].append(movie_type)
  movies_dict['Release Date'].append(movie_release_date)
  

import pandas
movies = pandas.DataFrame(data=movies_dict)
movies.to_csv('./movies.csv', encoding='utf8', index=False)

