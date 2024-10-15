import pandas as pd
import json

df = pd.read_csv('./Val Hackathon/playersProcessed/playersCombined.csv')

for _, row in df.iterrows():
    filename_base = str(row['player']).replace(' ', '_')

    row_dict = {k: v for k, v in row.items() if pd.notna(v)}
    json_content = {"metadataAttributes": row_dict}

    json_filename = f'./Val Hackathon/playerDataFinal/playerMetadata/{filename_base}.metadata.json'
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, indent=4)

    text_filename = f'./Val Hackathon/playerDataFinal/playerText/{filename_base}.txt'
    with open(text_filename, 'w', encoding='utf-8') as text_file:
        for col, val in row_dict.items():
            text_file.write(f"The {col} is {val}.\n")

