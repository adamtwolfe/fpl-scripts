import requests
import json
from graph import point_stem_plot

print('fetching player list...')
response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
r = json.loads(response.text)
players = r['elements']

i = 1
while i < len(players):
  print('fetching player summary...')
  response2 = requests.get('https://fantasy.premierleague.com/api/element-summary/' + str(i) + '/')
  r2 = json.loads(response2.text)
  currentHistory = r2['history']
  pastHistory = r2['history_past']

  point_stem_plot(currentHistory, i, players)

  print('generated player season stem plot')
  i+=1
