from flask import jsonify
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from routes import api_bp  # Import Blueprint

@api_bp.route('/players', methods=['GET'])
def get_players():
    try:
        player_list = players.get_players()
        return jsonify(player_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/player/stats/<int:player_id>', methods=['GET'])
def get_player_stats(player_id):
    try:
        player_log = playergamelog.PlayerGameLog(player_id=player_id)
        stats = player_log.get_data_frames()[0]
        return jsonify(stats.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/player/<int:player_id>', methods=['GET'])
def get_player_info(player_id):
    try:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        data = player_info.get_data_frames()[0].to_dict(orient='records')[0]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/player/awards/<int:player_id>', methods=['GET'])
def get_player_awards(player_id):
    try:
        awards = playerawards.PlayerAwards(player_id=player_id)
        data = awards.get_data_frames()[0].to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
