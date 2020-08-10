import requests
import json
import csv
from datetime import datetime
from csvWriters import writePlayerInfo, writePlayerMatchStats, writePlayerFplStats

print('fetching FPL data...')
response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')

r = json.loads(response.text)

players_raw = r['elements']

time = str(datetime.now()).split('.', 1)[0].replace(' ', '-').replace(':', '-')

playerInfoWriter = csv.writer(open('data/' + time + '_player-info.csv', 'w'))
playerMatchStatWriter = csv.writer(open('data/' + time + '_game-stats.csv', 'w'))
playerFplStatWriter = csv.writer(open('data/' + time + '_fpl-stats.csv', 'w'))

print('writing player data to files...')
for player in players_raw:
  writePlayerInfo(player, playerInfoWriter)
  writePlayerMatchStats(player, playerMatchStatWriter)
  writePlayerFplStats(player, playerFplStatWriter)

print('done!')