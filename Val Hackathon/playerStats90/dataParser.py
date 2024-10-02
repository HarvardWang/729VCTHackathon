import pandas as pd
import json

# Load JSON file

filenames = ['ap90' , 'na90', 'eu90', 'jp90', 'mn90', 'gc90', 'oce90']
for filename in filenames:
    with open(filename + '.json', encoding='utf-8') as file:
        data = json.load(file)
        segments = data['data']['segments']
        df = pd.DataFrame(segments)
        df['region'] = filename[:2]
        df['gamechanger'] = (filename =="gc90.json")
        df.to_csv(filename +'.csv', index=False)
