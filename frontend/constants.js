const API_TEAMS_URL = "http://127.0.0.1:5000/api/teams"; // Ensure Flask is running
const API_PLAYERS_URL = "http://127.0.0.1:5000/api/players"; // Ensure Flask is running

// Define teams in each conference based on their abbreviations
const EASTERN_TEAMS = ["ATL", "BOS", "BKN", "CHA", "CHI", "CLE", "DET", "IND", "MIA", "MIL", "NYK", "ORL", "PHI", "TOR", "WAS"];
const WESTERN_TEAMS = ["DAL", "DEN", "GSW", "HOU", "LAC", "LAL", "MEM", "MIN", "NOP", "OKC", "PHX", "POR", "SAC", "SAS", "UTA"];

const TEAM_CHAMPIONSHIPS = {
    BOS: 17,
    LAL: 17,
    CHI: 6,
    GSW: 7,
    SAS: 5,
    MIA: 3,
    DET: 3,
    PHI: 3,
    MIL: 2,
    HOU: 2,
    NYK: 2,
    CLE: 1,
    DAL: 1,
    TOR: 1,
    ATL: 1,
    WAS: 1,
    OKC: 1, // Includes Seattle SuperSonics
    // Remaining teams have 0
  };
  