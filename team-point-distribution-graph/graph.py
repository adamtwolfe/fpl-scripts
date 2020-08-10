import matplotlib.pyplot as plt
import numpy as np

def organize_data(point_distribution, teams):
  labels = []
  forwards = []
  midfielders = []
  defenders = []
  goalkeepers = []

  teamId = 1
  while teamId <= 20:
    labels.append(teams[teamId])
    forwards.append(point_distribution[teamId][4])
    midfielders.append(point_distribution[teamId][3])
    defenders.append(point_distribution[teamId][2])
    goalkeepers.append(point_distribution[teamId][1])
    teamId+=1

  return { 
    'labels': labels,
    'forwards': forwards,
    'midfielders': midfielders,
    'defenders': defenders,
    'goalkeepers': goalkeepers
  }

def point_distribution_plot(point_distribution, teams, fileName, scope):
  width = .5
  fig, ax = plt.subplots()
 
  chartData = organize_data(point_distribution, teams)

  labels = chartData['labels']
  forwards = chartData['forwards']
  midfielders = chartData['midfielders']
  defenders = chartData['defenders']
  goalkeepers = chartData['goalkeepers']

  midfieldStart = np.add(defenders, goalkeepers).tolist()
  forwardStart = np.add(midfielders, np.add(defenders, goalkeepers)).tolist()

  ax.bar(labels, goalkeepers, width, label='Goalkeepers')
  ax.bar(labels, defenders, width, label='Defenders', bottom=goalkeepers)
  ax.bar(labels, midfielders, width, label='Midfielders', bottom=midfieldStart)
  ax.bar(labels, forwards, width, label='Forwards', bottom=forwardStart)
  ax.set_ylabel('Total Points')
  plt.xticks(rotation=45)
  ax.set_title('Points by team and position (' + scope + ')')
  ax.legend()

  plt.savefig(fileName, bbox_inches='tight')

  print('generated point distribuiton chart')
