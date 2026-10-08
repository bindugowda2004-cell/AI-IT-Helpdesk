from fastapi import APIRouter
from api.database import get_db_connection
from api.schemas import TicketCreate

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/")
def create_ticket(ticket: TicketCreate):

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO tickets
        ( employee_id, subject, description, category, priority, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING ticket_id;
    """

    cursor.execute(
        query,
        (
            ticket.employee_id,
            ticket.subject,
            ticket.description,
            ticket.category,
            ticket.priority,
            "Open"
        )
    )

    ticket_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Ticket created successfully!",
        "ticket_id": ticket_id
    }
@router.get("/")
def get_tickets():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        ticket_id,
        employee_id,
        subject,
        description,
        category,
        priority,
        status
    FROM tickets
    ORDER BY ticket_id DESC
    """

    cursor.execute(query)

    tickets = cursor.fetchall()

    cursor.close()
    connection.close()

    return {"tickets": tickets}

@router.get("/{ticket_id}")
def get_ticket(ticket_id: int):

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            ticket_id,
            employee_id,
            subject,
            description,
            category,
            priority,
            status
        FROM tickets
        WHERE ticket_id = %s
    """

    cursor.execute(query, (ticket_id,))
    ticket = cursor.fetchone()

    cursor.close()
    connection.close()

    if ticket is None:
        return {
            "message": "Ticket not found"
        }

    return {
        "ticket_id": ticket[0],
        "employee_id": ticket[1],
        "subject": ticket[2],
        "description": ticket[3],
        "category": ticket[4],
        "priority": ticket[5],
        "status": ticket[6]
    }