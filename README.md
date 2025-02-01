# nba_data_api
This is a python api to get nba data

NBA_Data_API/
│── app.py
│── routes/
│   │── __init__.py
│   │── games.py
│   │── players.py
│   │── teams.py
│── requirements.txt
│── venv/ (optional virtual environment)

________________________________________________________________________________________________________
|Routes	            |URL	                            |Description                                   |
--------------------------------------------------------------------------------------------------------
|Player Info	    |/api/player/<player_id>	        |Get player bio & details                      |
|Player Awards	    |/api/player/awards/<player_id>	    |Fetch player MVPs, All-Stars, etc.            |
|Team Roster	    |/api/team/roster/<team_id>	        |Get current team roster                       |
|Team Championships	|/api/team/championships/<team_id>	|Get list of championships won                 |
|Today's Games	    |/api/games/today	                |Get NBA games happening today                 |
|Game Box Score	    |/api/game/boxscore/<game_id>	    |Fetch game stats                              |
|League Leaders	    |/api/league/leaders	            |Get top players in points, rebounds, assists  |
|Standings	        |/api/league/standings	            |Get latest NBA team standings                 |
|Search Players	    |/api/search/player?name=LeBron	    |Search for an NBA player                      |
|Search Teams	    |/api/search/team?name=Lakers	    |Search for an NBA team                        |
________________________________________________________________________________________________________
