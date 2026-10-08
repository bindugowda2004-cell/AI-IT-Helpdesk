async function predictTicket() {
    const subject = document.getElementById("subject").value.trim();
    const description = document.getElementById("description").value.trim();

    if (!subject || !description) {
        alert("Please enter subject and description.");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/predictions/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                subject: subject,
                description: description
            })
        });

        const data = await response.json();

        console.log("Prediction API response:", data);

        // Display the results directly on the page
        document.getElementById("category").textContent =
            data.predicted_category;

        document.getElementById("priority").textContent =
            data.predicted_priority;

        document.getElementById("solution").textContent =
            data.recommended_solution;

        document.getElementById("escalation").textContent =
            data.human_escalation_required ? "Yes" : "No";

    } catch (error) {
        console.error("Prediction error:", error);
        alert("Error connecting to the AI Helpdesk API.");
    }
}

async function createTicket() {
    const employeeId = document.getElementById("employeeId").value;
    const subject = document.getElementById("subject").value;
    const description = document.getElementById("description").value;
    const category = document.getElementById("category").value;
    const priority = document.getElementById("priority").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/tickets/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                employee_id: Number(employeeId),
                subject: subject,
                description: description,
                category: category,
                priority: priority
            })
        });

        const data = await response.json();

        if (!response.ok) {
            console.error("Create ticket API error:", data);
            document.getElementById("createResult").innerText =
                "Unable to create the ticket.";
            return;
        }

        document.getElementById("createResult").innerText =
            "Ticket created successfully. Ticket ID: " + data.ticket_id;

    } catch (error) {
        console.error("Create ticket error:", error);
        document.getElementById("createResult").innerText =
            "Unable to create the ticket.";
    }
}