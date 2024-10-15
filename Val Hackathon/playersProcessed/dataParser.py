import pandas as pd
import numpy as np
import json

# Load JSON file

finaldf = pd.DataFrame()

dirs = ['./Val Hackathon/playerStats30/', './Val Hackathon/playerStatsAll/']
filenames30 = ['ap30' , 'na30', 'eu30', 'jp30']
filenamesAll = ['apAll' , 'naAll', 'euAll', 'jpAll', 'mnAll', 'saAll', 'oceAll']

gc = []
with open('./Val Hackathon/game-changers/esports-data/players.json', encoding='utf-8') as file:
    data = json.load(file)
    for player in data:
        gc.append(player['handle'])
f = open('./Val Hackathon/playerLabels/challenger.txt', 'r', encoding='utf-8')
text = f.read()
chal = text.split(', ')
f = open('./Val Hackathon/playerLabels/igls.txt', 'r', encoding='utf-8')
text = f.read()
igl = text.split(',')


for filename in filenamesAll:
    with open(dirs[1] + filename + '.json', encoding='utf-8') as file:
        data = json.load(file)
        segments = data['data']['segments']
        df = pd.DataFrame(segments)
        df['igl'] = df['player'].isin(igl)
        df['region'] = filename[:-3]

        levels = [
            df['player'].isin(chal),
            df['player'].isin(gc)
        ]
        choices = ['challenger', 'game-changer']

        df['level'] = np.select(levels, choices, default='international')
        finaldf = pd.concat([finaldf, df])

finaldf.to_csv('./Val Hackathon/playersProcessed/playersAll.csv', index=False)