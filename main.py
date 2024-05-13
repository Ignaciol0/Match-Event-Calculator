import requests
import json
import pandas as pd

url = 'https://www.sofascore.com/salernitana-atalanta/Ldbskeb#id:11406754'



# Requests
'''
response = requests.get(
            f'https://api.sofascore.com/api/v1/event/{match_id}/lineups', 
            headers=self.requests_headers
        )

response = requests.get(f'https://api.sofascore.com/api/v1/event/{match_id}', headers=self.requests_headers)

request_url = f'https://api.sofascore.com/api/v1' +\
                f'/unique-tournament/{league_id}/season/{season_id}/statistics'+\
                f'?limit=100&order=-rating&offset={offset}'+\
                f'&accumulation={accumulation}' +\
                f'&fields={self.concatenated_fields}'+\
                f'&filters=position.in.{positions}'
            response = requests.get(request_url, headers=self.requests_headers)

response = requests.get(
            f'https://api.sofascore.com/api/v1/event/{match_id}/graph', 
            headers=self.requests_headers
        )

response = requests.get(
            f'https://api.sofascore.com/api/v1/event/{match_id}/statistics', 
            headers=self.requests_headers
        )

response = requests.get(
            f'https://api.sofascore.com/api/v1/event/{match_id}/lineups', 
            headers=self.requests_headers
        )

response = requests.get(
            f'https://api.sofascore.com/api/v1/event/{match_id}/average-positions', 
            headers=self.requests_headers
        )

response = requests.get(
            f'https://api.sofascore.com/api/v1/event/{match_id}/player/{player_id}/heatmap', 
            headers=self.requests_headers
        )

'''