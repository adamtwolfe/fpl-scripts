import requests
import matplotlib.pyplot as plt

def getPlayerName(playerId, players):
  for player in players:
    if(int(player['id'] == int(playerId))):
      return player['first_name'] + player['second_name']

def point_stem_plot(currentHistory, playerId, players):
  gameweek = []
  points = []
  wasHome = []
  totalPoints = 0

  for event in currentHistory:
    gameweek.append(event['round'])
    points.append(event['total_points'])
    wasHome.append(event['was_home'])
    totalPoints += event['total_points']

  averagePoints = totalPoints / len(gameweek)

  fig, ax = plt.subplots()
  ax.set_title('Points per gameweek')
  ax.set_ylabel('Gameweek points')
  ax.set_xlabel('Gameweek')
  ax.stem(gameweek, points, bottom=averagePoints)

  player = getPlayerName(playerId, players)
  plt.savefig('data/' + player + '.png', bbox_inches='tight')