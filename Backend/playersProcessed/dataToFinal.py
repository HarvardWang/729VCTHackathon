import pandas as pd
import numpy as np
import json

def write_text(text_dict):
    text = ""
    text += (f"""{text_dict['player']} is a member of {text_dict['team_name']} ({text_dict['org']}). They play in the {regions[text_dict['region']]} region and the VCT 
{text_dict['level']} circuit. Over their entire career, they have played {text_dict['rounds_played']} rounds 
with an average rating of {text_dict['rating']}, an average average combat score (ACS) of {text_dict['average_combat_score']}, an average kills death ratio 
of {text_dict['kill_deaths']}, an average average damage per round (ADR) of {text_dict['average_damage_per_round']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['kill_assists_survived_traded']}, an average kills per round (KPR) of {text_dict['kills_per_round']}, an average assists per round (APR) 
of {text_dict['assists_per_round']}, an average first kills per round (FKPR) of {text_dict['first_kills_per_round']}, an average first deaths per round (FDPR) 
of {text_dict['first_deaths_per_round']}, an average headshot percentage of {text_dict['headshot_percentage']}, and an average clutch success percentage 
of {text_dict['clutch_success_percentage']}. """)
    if text_dict['igl']:
        text += 'This player plays the role of an in game leader (IGL). '
    else:
        text += 'This player is not an in game leader. '
    text += (f"""Over their entire career, {text_dict['agent1']} is their most played agent. Over the {text_dict['agent1_rounds']} rounds they have played {text_dict['agent1']}, 
they have an average rating of {text_dict['agent1_rating']}, an average average combat score (ACS) of {text_dict['agent1_acs']}, an average kills death ratio 
of {text_dict['agent1_kd']}, an average average damage per round (ADR) of {text_dict['agent1_adr']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['agent1_kast']}, an average kills per round (KPR) of {text_dict['agent1_kpr']}, an average assists per round (APR) 
of {text_dict['agent1_apr']}, an average first kills per round (FKPR) of {text_dict['agent1_fkpr']}, and an average first deaths per round (FDPR) 
of {text_dict['agent1_fdpr']}. Using {text_dict['agent1']} this player has a total of {text_dict['agent1_kills']} kills, {text_dict['agent1_deaths']} deaths, 
{text_dict['agent1_assists']} assists, {text_dict['agent1_fk']} first bloods, and {text_dict['agent1_fd']} first deaths. """)
    if text_dict['agent2'] != 'Unknown':
        text += (f"""Over their entire career, {text_dict['agent2']} is their second most played agent. Over the {text_dict['agent2_rounds']} rounds they have played {text_dict['agent2']}, 
they have an average rating of {text_dict['agent2_rating']}, an average average combat score (ACS) of {text_dict['agent2_acs']}, an average kills death ratio 
of {text_dict['agent2_kd']}, an average average damage per round (ADR) of {text_dict['agent2_adr']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['agent2_kast']}, an average kills per round (KPR) of {text_dict['agent2_kpr']}, an average assists per round (APR) 
of {text_dict['agent2_apr']}, an average first kills per round (FKPR) of {text_dict['agent2_fkpr']}, and an average first deaths per round (FDPR) 
of {text_dict['agent2_fdpr']}. Using {text_dict['agent2']} this player has a total of {text_dict['agent2_kills']} kills, {text_dict['agent2_deaths']} deaths, 
{text_dict['agent2_assists']} assists, {text_dict['agent2_fk']} first bloods, and {text_dict['agent2_fd']} first deaths. """)
    if text_dict['agent3'] != 'Unknown':
        text += (f"""Over their entire career, {text_dict['agent3']} is their third most played agent. Over the {text_dict['agent3_rounds']} rounds they have played {text_dict['agent3']}, 
they have an average rating of {text_dict['agent3_rating']}, an average average combat score (ACS) of {text_dict['agent3_acs']}, an average kills death ratio 
of {text_dict['agent3_kd']}, an average average damage per round (ADR) of {text_dict['agent3_adr']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['agent3_kast']}, an average kills per round (KPR) of {text_dict['agent3_kpr']}, an average assists per round (APR) 
of {text_dict['agent3_apr']}, an average first kills per round (FKPR) of {text_dict['agent3_fkpr']}, and an average first deaths per round (FDPR) 
of {text_dict['agent3_fdpr']}. Using {text_dict['agent3']} this player has a total of {text_dict['agent3_kills']} kills, {text_dict['agent3_deaths']} deaths, 
{text_dict['agent3_assists']} assists, {text_dict['agent3_fk']} first bloods, and {text_dict['agent3_fd']} first deaths. """)
        
    if text_dict['org30'] != 'Unknown':
        text += (f"""Over the past thirty days, {text_dict['player']} has played {text_dict['rounds_played30']} rounds 
with an average rating of {text_dict['rating30']}, an average average combat score (ACS) of {text_dict['average_combat_score30']}, an average kills death ratio 
of {text_dict['kill_deaths30']}, an average average damage per round (ADR) of {text_dict['average_damage_per_round30']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['kill_assists_survived_traded30']}, an average kills per round (KPR) of {text_dict['kills_per_round30']}, an average assists per round (APR) 
of {text_dict['assists_per_round30']}, an average first kills per round (FKPR) of {text_dict['first_kills_per_round30']}, an average first deaths per round (FDPR) 
of {text_dict['first_deaths_per_round30']}, an average headshot percentage of {text_dict['headshot_percentage30']}, and an average clutch success percentage 
of {text_dict['clutch_success_percentage30']}. """)
        text += (f"""Over the past thirty days, {text_dict['agent130']} is their most played agent. Over the {text_dict['agent1_rounds30']} rounds they have played {text_dict['agent130']}, 
they have an average rating of {text_dict['agent1_rating30']}, an average average combat score (ACS) of {text_dict['agent1_acs30']}, an average kills death ratio 
of {text_dict['agent1_kd30']}, an average average damage per round (ADR) of {text_dict['agent1_adr30']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['agent1_kast30']}, an average kills per round (KPR) of {text_dict['agent1_kpr30']}, an average assists per round (APR) 
of {text_dict['agent1_apr30']}, an average first kills per round (FKPR) of {text_dict['agent1_fkpr30']}, and an average first deaths per round (FDPR) 
of {text_dict['agent1_fdpr30']}. Using {text_dict['agent130']} this player has a total of {text_dict['agent1_kills30']} kills, {text_dict['agent1_deaths30']} deaths, 
{text_dict['agent1_assists30']} assists, {text_dict['agent1_fk30']} first bloods, and {text_dict['agent1_fd30']} first deaths. """)
        if text_dict['agent230'] != 'Unknown':
            text += (f"""Over the past thirty days, {text_dict['agent230']} is their second most played agent. Over the {text_dict['agent2_rounds30']} rounds they have played {text_dict['agent230']}, 
they have an average rating of {text_dict['agent2_rating30']}, an average average combat score (ACS) of {text_dict['agent2_acs30']}, an average kills death ratio 
of {text_dict['agent2_kd30']}, an average average damage per round (ADR) of {text_dict['agent2_adr30']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['agent2_kast30']}, an average kills per round (KPR) of {text_dict['agent2_kpr30']}, an average assists per round (APR) 
of {text_dict['agent2_apr30']}, an average first kills per round (FKPR) of {text_dict['agent2_fkpr30']}, and an average first deaths per round (FDPR) 
of {text_dict['agent2_fdpr30']}. Using {text_dict['agent230']} this player has a total of {text_dict['agent2_kills30']} kills, {text_dict['agent2_deaths30']} deaths, 
{text_dict['agent2_assists30']} assists, {text_dict['agent2_fk30']} first bloods, and {text_dict['agent2_fd30']} first deaths. """)
        if text_dict['agent330'] != 'Unknown':
            text += (f"""Over the past thirty days, {text_dict['agent330']} is their third most played agent. Over the {text_dict['agent3_rounds30']} rounds they have played {text_dict['agent330']}, 
they have an average rating of {text_dict['agent3_rating30']}, an average average combat score (ACS) of {text_dict['agent3_acs30']}, an average kills death ratio 
of {text_dict['agent3_kd30']}, an average average damage per round (ADR) of {text_dict['agent3_adr30']}, an average kill, assist, survive, trade percent (KAST) 
of {text_dict['agent3_kast30']}, an average kills per round (KPR) of {text_dict['agent3_kpr30']}, an average assists per round (APR) 
of {text_dict['agent3_apr30']}, an average first kills per round (FKPR) of {text_dict['agent3_fkpr30']}, and an average first deaths per round (FDPR) 
of {text_dict['agent3_fdpr30']}. Using {text_dict['agent330']} this player has a total of {text_dict['agent3_kills30']} kills, {text_dict['agent3_deaths30']} deaths, 
{text_dict['agent3_assists30']} assists, {text_dict['agent3_fk30']} first bloods, and {text_dict['agent3_fd30']} first deaths. """)
    return text

df = pd.read_csv('./Val Hackathon/playersProcessed/playersCombined.csv')

df = df.replace({np.nan: 'Unknown'})
regions = {'na': 'North America', 'eu': 'Europe', 'sa': 'Latin America', 'mn': 'Middle East and North Africa', 'oce': 'Oceania', 'ap': 'Asia Pacific', 'jp': 'Japan'}

for _, row in df.iterrows():
    filename_base = str(row['player']).replace(' ', '_')

    json_dict = {k: v for k, v in row.items() if v != 'Unknown'}
    json_content = {"metadataAttributes": json_dict}

    text_dict = row.to_dict()

    json_filename = f'./Val Hackathon/playerDataFinal/playerMetadata/{filename_base}.txt.metadata.json'
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, indent=4)

   # text_filename = f'./Val Hackathon/playerDataFinal/playerText/{filename_base}.txt'
   # with open(text_filename, 'w', encoding='utf-8') as text_file:
    #    text_file.write(write_text(text_dict))
        

