const API_TEAMS_URL = "http://127.0.0.1:5000/api/teams"; // Ensure Flask is running
const API_PLAYERS_URL = "http://127.0.0.1:5000/api/players"; // Ensure Flask is running


async function fetchTeams() {
    try {
        const response = await fetch(API_TEAMS_URL);
        const teams = await response.json();

        const tableBody = document.getElementById("teams-table");
        tableBody.innerHTML = ""; // Clear previous data

        teams.forEach(team => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${team.full_name}</td>
                <td>${team.city}</td>
                <td>${team.state}</td>
                <td>${team.abbreviation}</td>
                <td>${team.year_founded}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error("Error fetching teams:", error);
    }
}

async function fetchPlayers() {
    try {
        const response = await fetch(API_PLAYERS_URL)
        const teams = await response.json();

        const tableBody = document.getElementById("teams-table");
        tableBody.innerHTML = ""; // Clear previous data

        
    } catch (error) {
        console.error("Error fetching players stats:", error);
    }
}

// Load teams on page load
document.addEventListener("DOMContentLoaded", fetchTeams);
