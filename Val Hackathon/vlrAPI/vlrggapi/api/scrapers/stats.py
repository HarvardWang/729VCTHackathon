import requests
from selectolax.parser import HTMLParser
import time

from utils.utils import headers


def vlr_stats(region: str, timespan: str):
    base_url = f"https://www.vlr.gg/stats/?event_group_id=all&event_id=all&region={region}&country=all&min_rounds=200&min_rating=1550&agent=all&map_id=all"
    url = (
        f"{base_url}&timespan=all"
        if timespan.lower() == "all"
        else f"{base_url}&timespan={timespan}d"
    )

    resp = requests.get(url, headers=headers)
    html = HTMLParser(resp.text)
    status = resp.status_code

    result = []
    for item in html.css("tbody tr"):
        player_link = item.css_first("td.mod-player.mod-a a").attributes["href"]
        player_url = f"https://www.vlr.gg{player_link}?timespan=all"

        # Fetch player page
        player_resp = requests.get(player_url, headers=headers)
        player_html = HTMLParser(player_resp.text)

        # Retrieve the player's team name and team ID from the player page
        team_element = player_html.css_first("a.wf-module-item.mod-first")
        if team_element:
            team_href = team_element.attributes["href"]  # Get href attribute
            team_id = team_href.split("/")[-2]  # Extract team ID from the href
            team_name = team_element.css_first("div[style='font-weight: 500;']").text()  # Get team name
            team_name = team_name.strip().replace("\n", "").replace("\t", "").strip()
        else:
            team_id = "N/A"
            team_name = "N/A"
        #print(team_href, team_id, team_name)
       
        #print(item.text())
        player = item.text().replace("\t", "").replace("\n", " ").strip().split()
        player_name = player[0]
        org = player[1] if len(player) > 1 else "N/A"
        #print(player)

        agents = [
            agents.attributes["src"].split("/")[-1].split(".")[0]
            for agents in item.css("td.mod-agents img")
        ]
        color_sq = [stats.text() for stats in item.css("td.mod-color-sq")]
        rnd = item.css_first("td.mod-rnd").text()

        top_agents = []
        agentRating = []
        for agent_row in player_html.css("tbody tr")[:3]:
            agent_img = agent_row.css_first("img")
            if agent_img:
                agent_name = agent_img.attributes["alt"]  # Extract agent name from the 'alt' attribute
                agent_stats = [stat.text().replace("\t", "").replace("\n", " ").strip() for stat in agent_row.css("td.mod-right")]
                top_agents.append({"agent_name": agent_name, "stats": agent_stats})
                agentRating.append([stat.text().replace("\t", "").replace("\n", " ").strip() for stat in agent_row.css("td.mod-center ")])
        time.sleep(.5)
        if len(top_agents) > 2:
            result.append(
                {
                    "player": player_name,
                    "org": org,
                    "agents": agents,
                    "rounds_played": rnd,
                    "rating": color_sq[0],
                    "average_combat_score": color_sq[1],
                    "kill_deaths": color_sq[2],
                    "kill_assists_survived_traded": color_sq[3],
                    "average_damage_per_round": color_sq[4],
                    "kills_per_round": color_sq[5],
                    "assists_per_round": color_sq[6],
                    "first_kills_per_round": color_sq[7],
                    "first_deaths_per_round": color_sq[8],
                    "headshot_percentage": color_sq[9],
                    "clutch_success_percentage": color_sq[10],
                    "team_id": team_id,
                    "team_name": team_name,
                    "agent1": top_agents[0]['agent_name'],
                    "agent1_use_pct": top_agents[0]['stats'][0],
                    "agent1_rounds": top_agents[0]['stats'][1],
                    "agent1_rating": agentRating[0][0],
                    "agent1_acs": top_agents[0]['stats'][2],
                    "agent1_kd": top_agents[0]['stats'][3],
                    "agent1_adr": top_agents[0]['stats'][4],
                    "agent1_kast": top_agents[0]['stats'][5],
                    "agent1_kpr": top_agents[0]['stats'][6],
                    "agent1_apr": top_agents[0]['stats'][7],
                    "agent1_fkpr": top_agents[0]['stats'][8],
                    "agent1_fdpr": top_agents[0]['stats'][9],
                    "agent1_kills": top_agents[0]['stats'][10],
                    "agent1_deaths": top_agents[0]['stats'][11],
                    "agent1_assists": top_agents[0]['stats'][12],
                    "agent1_fk": top_agents[0]['stats'][13],
                    "agent1_fd": top_agents[0]['stats'][14],
                    "agent2": top_agents[1]['agent_name'],
                    "agent2_use_pct": top_agents[1]['stats'][0],
                    "agent2_rounds": top_agents[1]['stats'][1],
                    "agent2_rating": agentRating[1][0],
                    "agent2_acs": top_agents[1]['stats'][2],
                    "agent2_kd": top_agents[1]['stats'][3],
                    "agent2_adr": top_agents[1]['stats'][4],
                    "agent2_kast": top_agents[1]['stats'][5],
                    "agent2_kpr": top_agents[1]['stats'][6],
                    "agent2_apr": top_agents[1]['stats'][7],
                    "agent2_fkpr": top_agents[1]['stats'][8],
                    "agent2_fdpr": top_agents[1]['stats'][9],
                    "agent2_kills": top_agents[1]['stats'][10],
                    "agent2_deaths": top_agents[1]['stats'][11],
                    "agent2_assists": top_agents[1]['stats'][12],
                    "agent2_fk": top_agents[1]['stats'][13],
                    "agent2_fd": top_agents[1]['stats'][14],
                    "agent3": top_agents[2]['agent_name'],
                    "agent3_use_pct": top_agents[2]['stats'][0],
                    "agent3_rounds": top_agents[2]['stats'][1],
                    "agent3_rating": agentRating[2][0],
                    "agent3_acs": top_agents[2]['stats'][2],
                    "agent3_kd": top_agents[2]['stats'][3],
                    "agent3_adr": top_agents[2]['stats'][4],
                    "agent3_kast": top_agents[2]['stats'][5],
                    "agent3_kpr": top_agents[2]['stats'][6],
                    "agent3_apr": top_agents[2]['stats'][7],
                    "agent3_fkpr": top_agents[2]['stats'][8],
                    "agent3_fdpr": top_agents[2]['stats'][9],
                    "agent3_kills": top_agents[2]['stats'][10],
                    "agent3_deaths": top_agents[2]['stats'][11],
                    "agent3_assists": top_agents[2]['stats'][12],
                    "agent3_fk": top_agents[2]['stats'][13],
                    "agent3_fd": top_agents[2]['stats'][14]
                }
            )
        elif len(top_agents) > 1:
            result.append(
                {
                    "player": player_name,
                    "org": org,
                    "agents": agents,
                    "rounds_played": rnd,
                    "rating": color_sq[0],
                    "average_combat_score": color_sq[1],
                    "kill_deaths": color_sq[2],
                    "kill_assists_survived_traded": color_sq[3],
                    "average_damage_per_round": color_sq[4],
                    "kills_per_round": color_sq[5],
                    "assists_per_round": color_sq[6],
                    "first_kills_per_round": color_sq[7],
                    "first_deaths_per_round": color_sq[8],
                    "headshot_percentage": color_sq[9],
                    "clutch_success_percentage": color_sq[10],
                    "team_id": team_id,
                    "team_name": team_name,
                    "agent1": top_agents[0]['agent_name'],
                    "agent1_use_pct": top_agents[0]['stats'][0],
                    "agent1_rounds": top_agents[0]['stats'][1],
                    "agent1_rating": agentRating[0][0],
                    "agent1_acs": top_agents[0]['stats'][2],
                    "agent1_kd": top_agents[0]['stats'][3],
                    "agent1_adr": top_agents[0]['stats'][4],
                    "agent1_kast": top_agents[0]['stats'][5],
                    "agent1_kpr": top_agents[0]['stats'][6],
                    "agent1_apr": top_agents[0]['stats'][7],
                    "agent1_fkpr": top_agents[0]['stats'][8],
                    "agent1_fdpr": top_agents[0]['stats'][9],
                    "agent1_kills": top_agents[0]['stats'][10],
                    "agent1_deaths": top_agents[0]['stats'][11],
                    "agent1_assists": top_agents[0]['stats'][12],
                    "agent1_fk": top_agents[0]['stats'][13],
                    "agent1_fd": top_agents[0]['stats'][14],
                    "agent2": top_agents[1]['agent_name'],
                    "agent2_use_pct": top_agents[1]['stats'][0],
                    "agent2_rounds": top_agents[1]['stats'][1],
                    "agent2_rating": agentRating[1][0],
                    "agent2_acs": top_agents[1]['stats'][2],
                    "agent2_kd": top_agents[1]['stats'][3],
                    "agent2_adr": top_agents[1]['stats'][4],
                    "agent2_kast": top_agents[1]['stats'][5],
                    "agent2_kpr": top_agents[1]['stats'][6],
                    "agent2_apr": top_agents[1]['stats'][7],
                    "agent2_fkpr": top_agents[1]['stats'][8],
                    "agent2_fdpr": top_agents[1]['stats'][9],
                    "agent2_kills": top_agents[1]['stats'][10],
                    "agent2_deaths": top_agents[1]['stats'][11],
                    "agent2_assists": top_agents[1]['stats'][12],
                    "agent2_fk": top_agents[1]['stats'][13],
                    "agent2_fd": top_agents[1]['stats'][14]
                }
            )
        else:
            result.append(
                {
                    "player": player_name,
                    "org": org,
                    "agents": agents,
                    "rounds_played": rnd,
                    "rating": color_sq[0],
                    "average_combat_score": color_sq[1],
                    "kill_deaths": color_sq[2],
                    "kill_assists_survived_traded": color_sq[3],
                    "average_damage_per_round": color_sq[4],
                    "kills_per_round": color_sq[5],
                    "assists_per_round": color_sq[6],
                    "first_kills_per_round": color_sq[7],
                    "first_deaths_per_round": color_sq[8],
                    "headshot_percentage": color_sq[9],
                    "clutch_success_percentage": color_sq[10],
                    "team_id": team_id,
                    "team_name": team_name,
                    "agent1": top_agents[0]['agent_name'],
                    "agent1_use_pct": top_agents[0]['stats'][0],
                    "agent1_rounds": top_agents[0]['stats'][1],
                    "agent1_rating": agentRating[0][0],
                    "agent1_acs": top_agents[0]['stats'][2],
                    "agent1_kd": top_agents[0]['stats'][3],
                    "agent1_adr": top_agents[0]['stats'][4],
                    "agent1_kast": top_agents[0]['stats'][5],
                    "agent1_kpr": top_agents[0]['stats'][6],
                    "agent1_apr": top_agents[0]['stats'][7],
                    "agent1_fkpr": top_agents[0]['stats'][8],
                    "agent1_fdpr": top_agents[0]['stats'][9],
                    "agent1_kills": top_agents[0]['stats'][10],
                    "agent1_deaths": top_agents[0]['stats'][11],
                    "agent1_assists": top_agents[0]['stats'][12],
                    "agent1_fk": top_agents[0]['stats'][13],
                    "agent1_fd": top_agents[0]['stats'][14]
                }
            )

    segments = {"status": status, "segments": result}
    data = {"data": segments}

    if status != 200:
        raise Exception("API response: {}".format(status))
    return data
