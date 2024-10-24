import pandas as pd

players30 = pd.read_csv('./Val Hackathon/playersProcessed/players30.csv')
playersAll   = pd.read_csv('./Val Hackathon/playersProcessed/playersAll.csv')

combined = pd.merge(playersAll, players30, on='player', how='left')

combined.to_csv('./Val Hackathon/playersProcessed/playersCombined.csv', index=False)