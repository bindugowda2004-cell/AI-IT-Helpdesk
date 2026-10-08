import csv
import random
from datetime import datetime, timedelta

categories = {
    "Network": [
        "WiFi is not connecting",
        "Internet connection is very slow",
        "VPN is not working",
        "Unable to access office network",
        "Network connection keeps disconnecting"
    ],
    "Hardware": [
        "Laptop is not turning on",
        "Keyboard is not working",
        "Mouse is not responding",
        "Monitor is not displaying properly",
        "Printer is not working"
    ],
    "Software": [
        "Application is crashing",
        "Software installation failed",
        "Application is running slowly",
        "Unable to open application",
        "Software is showing an error"
    ],
    "Account": [
        "Password reset required",
        "Account is locked",
        "Unable to login",
        "User account is not working",
        "Need access to account"
    ],
    "Security": [
        "Suspicious email received",
        "Security alert received",
        "Possible phishing email",
        "Antivirus warning appeared",
        "Unauthorized login detected"
    ],
    "Email": [
        "Unable to send email",
        "Unable to receive email",
        "Email is not syncing",
        "Outlook is not opening",
        "Email attachment is not working"
    ]
}

departments = [
    "HR",
    "Finance",
    "IT",
    "Sales",
    "Marketing",
    "Operations"
]

employee_types = [
    "Permanent",
    "Contract",
    "Intern"
]

priorities = [
    "Low",
    "Medium",
    "High"
]

statuses = [
    "Open",
    "In Progress",
    "Resolved"
]

rows = []

start_date = datetime.now() - timedelta(days=180)

for ticket_id in range(1, 501):

    category = random.choice(list(categories.keys()))
    description = random.choice(categories[category])

    priority = random.choice(priorities)
    status = random.choice(statuses)
    department = random.choice(departments)
    employee_type = random.choice(employee_types)

    created_at = start_date + timedelta(
        minutes=random.randint(0, 180 * 24 * 60)
    )

    resolution_time = round(
        random.uniform(0.5, 48.0), 2
    )

    if status == "Resolved":
        resolved_at = created_at + timedelta(
            hours=resolution_time
        )
    else:
        resolved_at = ""

    rows.append({
        "ticket_id": ticket_id,
        "employee_name": f"Employee_{random.randint(1, 100)}",
        "department": department,
        "employee_type": employee_type,
        "subject": description,
        "description": description,
        "category": category,
        "priority": priority,
        "status": status,
        "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "resolved_at": (
            resolved_at.strftime("%Y-%m-%d %H:%M:%S")
            if resolved_at else ""
        ),
        "resolution_time_hours": resolution_time
    })


output_file = "data/raw/tickets.csv"

fieldnames = [
    "ticket_id",
    "employee_name",
    "department",
    "employee_type",
    "subject",
    "description",
    "category",
    "priority",
    "status",
    "created_at",
    "resolved_at",
    "resolution_time_hours"
]

with open(output_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(rows)

print("500 helpdesk tickets generated successfully!")
print(f"File: {output_file}")