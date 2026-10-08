from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# ============================================================
# 1. Define the Agent State
# ============================================================

class HelpdeskState(TypedDict):
    subject: str
    description: str
    category: str
    priority: str
    solution: str
    escalate: bool


# ============================================================
# 2. Analyze Ticket Category
# ============================================================

def analyze_ticket(state: HelpdeskState):

    text = (
        state["subject"] + " " + state["description"]
    ).lower()

    if any(word in text for word in [
        "wifi",
        "internet",
        "network",
        "connection"
    ]):
        category = "Network"

    elif any(word in text for word in [
        "password",
        "login",
        "account"
    ]):
        category = "Account"

    elif any(word in text for word in [
        "laptop",
        "keyboard",
        "mouse",
        "printer"
    ]):
        category = "Hardware"

    elif any(word in text for word in [
        "email",
        "mail",
        "outlook"
    ]):
        category = "Email"

    elif any(word in text for word in [
        "virus",
        "malware",
        "security"
    ]):
        category = "Security"

    else:
        category = "Software"

    return {
        "category": category
    }


# ============================================================
# 3. Analyze Ticket Priority
# ============================================================

def analyze_priority(state: HelpdeskState):

    text = (
        state["subject"] + " " + state["description"]
    ).lower()

    if any(word in text for word in [
        "urgent",
        "critical",
        "server down",
        "cannot work",
        "security breach"
    ]):
        priority = "High"

    elif any(word in text for word in [
        "slow",
        "problem",
        "issue",
        "error",
        "not working"
    ]):
        priority = "Medium"

    else:
        priority = "Low"

    return {
        "priority": priority
    }


# ============================================================
# 4. Search Knowledge Base
# ============================================================

def search_knowledge_base(state: HelpdeskState):

    category = state["category"]

    knowledge_base = {

        "Network":
            "Check WiFi connection, restart the router, "
            "and verify network settings.",

        "Hardware":
            "Check the device connections, restart the device, "
            "and verify whether the hardware is detected.",

        "Software":
            "Restart the application, check for updates, "
            "and reinstall the software if required.",

        "Account":
            "Verify username and password and check whether "
            "the account is locked.",

        "Email":
            "Check internet connection, email credentials, "
            "mailbox storage, and email server settings.",

        "Security":
            "Disconnect the affected device from the network "
            "and contact the IT security team."
    }

    solution = knowledge_base.get(
        category,
        "Please contact the IT support team for assistance."
    )

    return {
        "solution": solution
    }


# ============================================================
# 5. Recommend Solution
# ============================================================

def recommend_solution(state: HelpdeskState):

    solution = state["solution"]

    return {
        "solution": solution
    }


# ============================================================
# 6. Decide Whether Human Escalation Is Required
# ============================================================

def check_escalation(state: HelpdeskState):

    if (
        state["priority"] == "High"
        or state["category"] == "Security"
    ):
        escalate = True

    else:
        escalate = False

    return {
        "escalate": escalate
    }


# ============================================================
# 7. Build LangGraph Workflow
# ============================================================

workflow = StateGraph(HelpdeskState)


# Add nodes

workflow.add_node(
    "analyze_ticket",
    analyze_ticket
)

workflow.add_node(
    "analyze_priority",
    analyze_priority
)

workflow.add_node(
    "search_knowledge_base",
    search_knowledge_base
)

workflow.add_node(
    "recommend_solution",
    recommend_solution
)

workflow.add_node(
    "check_escalation",
    check_escalation
)


# ============================================================
# 8. Connect Nodes
# ============================================================

workflow.add_edge(
    START,
    "analyze_ticket"
)

workflow.add_edge(
    "analyze_ticket",
    "analyze_priority"
)

workflow.add_edge(
    "analyze_priority",
    "search_knowledge_base"
)

workflow.add_edge(
    "search_knowledge_base",
    "recommend_solution"
)

workflow.add_edge(
    "recommend_solution",
    "check_escalation"
)

workflow.add_edge(
    "check_escalation",
    END
)


# ============================================================
# 9. Compile the Graph
# ============================================================

helpdesk_graph = workflow.compile()


# ============================================================
# 10. Test the AI Agent
# ============================================================

if __name__ == "__main__":

    test_ticket = {
        "subject": "WiFi connection problem",
        "description": (
            "My office laptop is unable to connect "
            "to the WiFi network."
        ),
        "category": "",
        "priority": "",
        "solution": "",
        "escalate": False
    }

    result = helpdesk_graph.invoke(test_ticket)

    print("\nAI Helpdesk Result")
    print("----------------------------")

    print("Subject:")
    print(result["subject"])

    print("\nDescription:")
    print(result["description"])

    print("\nPredicted Category:")
    print(result["category"])

    print("\nPredicted Priority:")
    print(result["priority"])

    print("\nRecommended Solution:")
    print(result["solution"])

    print("\nHuman Escalation Required:")
    print(result["escalate"])