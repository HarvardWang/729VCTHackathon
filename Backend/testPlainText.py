import requests
response = requests.get(
    'https://liquipedia.net/valorant/api.php',
    params={
        'action': 'query',
        'format': 'json',
        'titles': 'TenZ',
        'prop': 'extracts'
    }
).json()
page = next(iter(response['query']['pages'].values()))
print(page['extract'])