from mcp.server.mcpserver import MCPServer
from api.database import get_db_connection

# Create MCP server
mcp = MCPServer("AI IT Helpdesk")


# Simple test tool
@mcp.tool()
def get_helpdesk_status() -> str:
    """Check whether the AI IT Helpdesk MCP server is running."""
    
    return "AI IT Helpdesk MCP server is running successfully."


@mcp.tool()
def search_tickets(keyword: str) -> str:
    """Search helpdesk tickets using a keyword."""
    return f"Ticket search requested for: {keyword}"

@mcp.tool()
def get_knowledge_base(category: str) -> str:
    """Get a troubleshooting solution for a helpdesk category."""

    knowledge_base = {
        "Network": "Check WiFi connection, restart the router, and verify network settings.",
        "Hardware": "Check device connections, restart the device, and verify whether the hardware is detected.",
        "Software": "Restart the application, check for updates, and reinstall the software if required.",
        "Account": "Verify username and password and check whether the account is locked.",
        "Email": "Check internet connection, email credentials, mailbox storage, and email server settings.",
        "Security": "Disconnect the affected device from the network and contact the IT security team."
    }

    return knowledge_base.get(
        category,
        "No knowledge-base solution found for this category."
    )

@mcp.tool()
def create_ticket(
    employee_id: int,
    subject: str,
    description: str,
    category: str,
    priority: str
) -> str:
    """Create a new IT helpdesk ticket in PostgreSQL."""

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO tickets
        (employee_id, subject, description, category, priority, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING ticket_id;
    """

    cursor.execute(
        query,
        (
            employee_id,
            subject,
            description,
            category,
            priority,
            "Open"
        )
    )

    ticket_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return f"Ticket created successfully with ticket ID: {ticket_id}"

if __name__ == "__main__":
    mcp.run()