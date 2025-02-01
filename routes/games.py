from flask import jsonify
from nba_api.stats.endpoints import leaguegamefinder
from routes import api_bp  # Absolute import

@api_bp.route('/games', methods=['GET'])
def get_all_games():
    try:
        game_finder = leaguegamefinder.LeagueGameFinder()
        games = game_finder.get_data_frames()[0]
        return jsonify(games.head(100).to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/games/today', methods=['GET'])
def get_today_games():
    try:
        today = datetime.today().strftime('%Y-%m-%d')
        games = scoreboard.Scoreboard(game_date=today)
        data = games.get_data_frames()[0].to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/game/boxscore/<string:game_id>', methods=['GET'])
def get_boxscore(game_id):
    try:
        box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
        data = box_score.get_data_frames()[0].to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
