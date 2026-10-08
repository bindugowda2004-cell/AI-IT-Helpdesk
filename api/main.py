from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.tickets import router as ticket_router
from api.routes.predictions import router as prediction_router

app = FastAPI(
    title="AI IT Helpdesk API",
    description="Backend API for the AI-Powered IT Helpdesk System",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {
        "message": "AI IT Helpdesk API is running!"
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "AI IT Helpdesk API is working correctly!"
    }

app.include_router(ticket_router)
app.include_router(prediction_router)