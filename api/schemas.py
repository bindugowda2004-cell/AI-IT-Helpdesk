from pydantic import BaseModel


class TicketCreate(BaseModel):
    employee_id: int
    subject: str
    description: str
    category: str
    priority: str