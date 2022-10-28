import requests
from pprint import pprint

class Herois:
    host = 'https://www.superheroapi.com/api/2619421814940190/search/'

    def get_headers(self):
        return {'Content-Type': 'application/json'}

    def get_latest_gifs(self, name):
        url = f'{self.host}{name}'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()['results'][0]['powerstats']['intelligence']

if __name__ in '__main__':
    name = input('Введите имена героев через запятую: ').split(', ')
    hero = Herois()
    n = {}
    for i in range(len(name)):
        n.setdefault(name[i],  hero.get_latest_gifs(name[i]))

m = max(n.keys())
print(n)
print(f'Самый умный герой: {m}')

