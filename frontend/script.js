document.addEventListener("DOMContentLoaded", () => {
    console.log("✅ DOM fully loaded. Running fetchTeams()");
    fetchTeams();
});

/**
 * Fetch teams from the API and categorize them into Eastern or Western Conference.
 * Displays all teams inside their respective conference cards.
 */
async function fetchTeams() {
    try {
        console.log("Fetching data from:", API_TEAMS_URL);

        // Make API request to fetch teams
        const response = await fetch(API_TEAMS_URL);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        // Convert response to JSON
        const teams = await response.json();
        console.log("Teams Data:", teams);

        // Get references to the Eastern and Western Conference containers
        const easternContainer = document.getElementById("eastern-teams");
        const westernContainer = document.getElementById("western-teams");

        // Clear previous content
        easternContainer.innerHTML = "";
        westernContainer.innerHTML = "";

        // Loop through each team and categorize them into the appropriate conference
        teams.forEach(team => {
            if (!team.abbreviation) return; // Skip if abbreviation is missing

            // Construct the path to the team's logo stored in the assets folder
            const logoPath = `assets/${team.abbreviation}-logo.svg`;

            // Create a div element to represent a single team (logo + name)
            const teamItem = document.createElement("div");
            teamItem.className = "team-item";
            teamItem.innerHTML = `
                <img src="${logoPath}" alt="${team.full_name} Logo" 
                     onerror="this.onerror=null; this.src='assets/default-logo.svg';">
                <p>${team.abbreviation}</p>
            `;

            // Add an event listener to open the modal when the team is clicked
            teamItem.addEventListener("click", () => showTeamDetails(team));

            // Append the team to the correct conference section
            if (EASTERN_TEAMS.includes(team.abbreviation)) {
                easternContainer.appendChild(teamItem);
            } else if (WESTERN_TEAMS.includes(team.abbreviation)) {
                westernContainer.appendChild(teamItem);
            }
        });

    } catch (error) {
        console.error("Error fetching teams:", error);
    }
}


/**
 * Show the modal with detailed information about the selected team.
 * @param {Object} team - The selected team object containing details like name, city, and state.
 */
function showTeamDetails(team) {
    // Get reference to the modal content section
    const teamDetails = document.getElementById("team-details");

    // Populate the modal with team information
    teamDetails.innerHTML = `
        <h2>${team.full_name} (${team.abbreviation})</h2>
        <img src="assets/${team.abbreviation}-logo.svg" alt="${team.full_name} Logo"
             onerror="this.onerror=null; this.src='assets/default-logo.svg';" width="100">
        <p><strong>City:</strong> ${team.city}, ${team.state}</p>
        <p><strong>Founded:</strong> ${team.year_founded}</p>
    `;

    // Display the modal
    document.getElementById("team-modal").style.display = "flex";
}

// Add event listener to close the modal when the close button is clicked
document.querySelector(".close-btn").addEventListener("click", () => {
    document.getElementById("team-modal").style.display = "none";
});


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
