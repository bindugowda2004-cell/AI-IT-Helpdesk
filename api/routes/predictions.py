from fastapi import APIRouter
from pydantic import BaseModel

from agents.helpdesk_graph import helpdesk_graph


router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"]
)


class PredictionRequest(BaseModel):
    subject: str
    description: str


@router.post("/")
def predict_ticket(ticket: PredictionRequest):

    initial_state = {
        "subject": ticket.subject,
        "description": ticket.description,
        "category": "",
        "priority": "",
        "solution": "",
        "escalate": False
    }

    result = helpdesk_graph.invoke(initial_state)

    return {
        "subject": result["subject"],
        "description": result["description"],
        "predicted_category": result["category"],
        "predicted_priority": result["priority"],
        "recommended_solution": result["solution"],
        "human_escalation_required": result["escalate"]
    }