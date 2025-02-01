from flask import jsonify
from nba_api.stats.endpoints import teamgamelogs
from nba_api.stats.static import teams
from routes import api_bp # Import Blueprint

@api_bp.route('/teams', methods=['GET'])
def get_teams():
    try:
        team_list = teams.get_teams()
        return jsonify(team_list)
    except Exception as e:
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
