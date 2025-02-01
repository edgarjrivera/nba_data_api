from flask import request, jsonify
from nba_api.stats.static import players, teams
from routes import api_bp

@api_bp.route('/search/player', methods=['GET'])
def search_player():
    query = request.args.get('name', '').lower()
    matching_players = [p for p in players.get_players() if query in p['full_name'].lower()]
    return jsonify(matching_players)

@api_bp.route('/search/team', methods=['GET'])
def search_team():
    query = request.args.get('name', '').lower()
    matching_teams = [t for t in teams.get_teams() if query in t['full_name'].lower()]
    return jsonify(matching_teams)