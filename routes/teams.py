import time
from flask import jsonify, current_app
from nba_api.stats.static import teams
from routes import api_bp
from utils import get_response_metrics 

@api_bp.route('/teams', methods=['GET'])
def get_teams():
    try:
         # ✅ Record start time
        start_time = time.time()

         # Fetch team data
        team_list = teams.get_teams()
        response_json = jsonify(team_list)

        # ✅ Log response size
        get_response_metrics(response_json, start_time)

        return response_json
    except Exception as e:
        current_app.logger.error(f"Error fetching teams: {e}")
        return jsonify({"error": str(e)}), 500

@api_bp.route('/team/stats/<int:team_id>', methods=['GET'])
def get_team_stats(team_id):
    try:
        team_log = teamgamelogs.TeamGameLogs(team_id_nullable=str(team_id))
        stats = team_log.get_data_frames()[0]
        return jsonify(stats.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/team/roster/<int:team_id>', methods=['GET'])
def get_team_roster(team_id):
    try:
        roster = commonteamroster.CommonTeamRoster(team_id=team_id)
        data = roster.get_data_frames()[0].to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/team/championships/<int:team_id>', methods=['GET'])
def get_team_championships(team_id):
    try:
        team_history = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id)
        championships = [season for season in team_history.get_data_frames()[0].to_dict(orient='records') if season["NBA_FINALS_APPEARANCE"] == "Y"]
        return jsonify(championships)
    except Exception as e:
        return jsonify({"error": str(e)}), 500