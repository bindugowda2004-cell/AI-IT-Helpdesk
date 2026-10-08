# AI-IT-Helpdesk

An AI-powered IT Helpdesk system that predicts support ticket categories and priorities, creates tickets, and stores ticket information in PostgreSQL.

## 🚀 Features

- AI-based ticket category prediction
- AI-based ticket priority prediction
- IT support ticket creation
- PostgreSQL database integration
- FastAPI backend
- Interactive web frontend
- MCP server integration
- Machine learning and deep learning components
- ETL and data analysis workflow
- Docker support

## 🛠️ Technologies Used

- Python
- FastAPI
- PostgreSQL
- HTML
- CSS
- JavaScript
- Machine Learning
- PyTorch
- RNN
- LangGraph
- MCP
- Docker
- Git & GitHub

## 📁 Project Structure

```text
AI-IT-Helpdesk/
├── api/
├── database/
├── data/
├── frontend/
├── mcp/
├── notebooks/
├── docker-compose.yml
├── requirements.txt
└── tickets.csv
```

## 🔄 System Workflow

```text
User
  ↓
Web Frontend
  ↓
FastAPI Backend
  ↓
AI Prediction
  ↓
Category + Priority
  ↓
PostgreSQL Database
  ↓
Ticket Created
```

## 🎯 Project Objective

The goal of this project is to demonstrate how AI, backend APIs, databases, and DevOps technologies can be combined to build a practical IT Helpdesk application.

The system helps automate IT support ticket classification and priority prediction while storing ticket information in a PostgreSQL database.

## 🤖 AI Capabilities

The system analyzes the user's ticket description and predicts:

- Ticket category
- Ticket priority

This helps support teams understand incoming issues and process them more efficiently.

## 🗄️ Database

PostgreSQL is used to store employee and IT helpdesk ticket information.

The ticket system includes information such as:

- Employee ID
- Subject
- Description
- Category
- Priority
- Status
- Created time
- Resolved time
- Resolution time

## 🔌 API

The backend is built using FastAPI.

API documentation is available through Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## ▶️ Running the Project

### 1. Start the FastAPI backend

```bash
python -m uvicorn api.main:app --reload
```

### 2. Start the frontend

Open the `frontend` folder and run:

```bash
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500/
```

## 📊 Project Notebooks

The project includes notebooks covering:

- Data analysis
- Machine learning classification
- PyTorch RNN
- PostgreSQL and ETL

## 🔗 MCP Integration

The project includes an MCP server and client for integrating helpdesk functionality with MCP-based tools.

## 🐳 Docker

Docker configuration is included to support containerized deployment of the application.

## 📌 Future Improvements

- User authentication and role-based access
- Helpdesk dashboard and analytics
- Automated ticket assignment
- Email notifications
- Cloud deployment
- CI/CD pipeline using Azure DevOps
- Advanced AI-based ticket resolution suggestions

## 👩‍💻 Project Type

BCA Final Year Project / AI & DevOps Portfolio Project

## 📄 License

This project is created for educational and portfolio purposes.