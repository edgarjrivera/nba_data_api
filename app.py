from flask import Flask, jsonify
from nba_api.stats.endpoints import leaguegamefinder, playergamelog, commonplayerinfo, teamgamelogs
from nba_api.stats.static import players, teams
import pandas as pd

app = Flask(__name__)

@app.route('/games', methods=['GET'])
def get_all_games():
    try:
        # Fetch all games
        game_finder = leaguegamefinder.LeagueGameFinder()
        games = game_finder.get_data_frames()[0]  # Get the first DataFrame
        
        # Limit data for performance (adjustable)
        return jsonify(games.head(100).to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/player/stats/<int:player_id>', methods=['GET'])
def get_player_stats(player_id):
    try:
        # Fetch player stats
        player_log = playergamelog.PlayerGameLog(player_id=player_id)
        stats = player_log.get_data_frames()[0]  # Get the first DataFrame
        return jsonify(stats.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/team/stats/<int:team_id>', methods=['GET'])
def get_team_stats(team_id):
    try:
        # Fetch team stats (convert team_id to string if required)
        team_log = teamgamelogs.TeamGameLogs(team_id_nullable=str(team_id))  # Fix: Expecting a string format
        stats = team_log.get_data_frames()[0]  # Get the first DataFrame
        return jsonify(stats.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/players', methods=['GET'])
def get_players():
    try:
        # Fetch all players
        player_list = players.get_players()
        return jsonify(player_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/teams', methods=['GET'])
def get_teams():
    try:
        # Fetch all teams
        team_list = teams.get_teams()
        return jsonify(team_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the NBA API! Use endpoints like /games, /players, /teams"})


if __name__ == '__main__':
    app.run(debug=True)
