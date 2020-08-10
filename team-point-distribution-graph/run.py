import requests
import json
from pointDistributionDict import point_distributions_total
from pointDistributionDict import point_distributions_event
from graph import point_distribution_plot

def mapTeams(teams):
  teamMap = {}
  for team in teams:
    teamMap[team['id']] = team['short_name']
  return teamMap

print('fetching FPL data...')
response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')

r = json.loads(response.text)

events_raw = r['events']
teams_raw = r['teams']
players_raw = r['elements']

print('calculating team points by position...')
for player in players_raw:
  point_distributions_total[player['team']][player['element_type']] += player['total_points']
  point_distributions_event[player['team']][player['element_type']] += player['event_points']

teams = mapTeams(teams_raw)
point_distribution_plot(point_distributions_total, teams, 'data/total_point_distribution.png', 'total')
point_distribution_plot(point_distributions_event, teams, 'data/event_point_distribution.png', 'gameweek')
