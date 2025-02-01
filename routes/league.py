from flask import jsonify
from nba_api.stats.endpoints import leaguelineleaders, leaguestandingsv3
from routes import api_bp

@api_bp.route('/league/leaders', methods=['GET'])
def get_league_leaders():
    try:
        leaders = leaguelineleaders.LeagueLineLeaders()
        data = leaders.get_data_frames()[0].to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/league/standings', methods=['GET'])
def get_league_standings():
    try:
        standings = leaguestandingsv3.LeagueStandingsV3()
        data = standings.get_data_frames()[0].to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
