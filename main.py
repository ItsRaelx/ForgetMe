from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
import os
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict

# Import our application modules
from app.email_service import EmailService
from app.gdpr_service import GDPRService

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="ForgetMe - GDPR Data Removal Tool")

# Setup templates and static files directories
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create instances of our services
email_service = EmailService()
gdpr_service = GDPRService()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render the home page."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/connect", response_class=HTMLResponse)
async def connect_form(request: Request):
    """Render the email connection form."""
    return templates.TemplateResponse("connect.html", {"request": request})

@app.post("/connect")
async def connect_smtp(
    request: Request,
    email: EmailStr = Form(...),
    password: str = Form(...),
    smtp_server: str = Form(...),
    smtp_port: int = Form(...)
):
    """Connect to the user's SMTP server and scan for emails."""
    try:
        # Connect to SMTP and get domains
        domains = await email_service.connect_and_scan(
            email=email,
            password=password,
            smtp_server=smtp_server,
            smtp_port=smtp_port
        )
        
        # Store connection in session (this would need session middleware in real app)
        # For now we'll just redirect to the domains page
        return RedirectResponse(url="/domains?email=" + email, status_code=302)
    
    except Exception as e:
        return templates.TemplateResponse(
            "connect.html", 
            {"request": request, "error": str(e)}
        )

@app.get("/domains", response_class=HTMLResponse)
async def list_domains(request: Request, email: Optional[str] = None):
    """Show list of domains from which the user has received emails."""
    # In a real app, we'd get this from a session or database
    # For demo, we'll generate some fake domains if email was provided
    domains = []
    if email:
        # This would be replaced with actual domain extraction logic
        domains = email_service.get_domains_for_demo(email)
    
    return templates.TemplateResponse(
        "domains.html", 
        {"request": request, "domains": domains, "email": email}
    )

@app.post("/send-requests")
async def send_gdpr_requests(
    request: Request,
    selected_domains: List[str] = Form(...)
):
    """Send GDPR data removal requests to selected domains."""
    results = {}
    
    for domain in selected_domains:
        try:
            privacy_email = await gdpr_service.find_privacy_email(domain)
            if privacy_email:
                success = await gdpr_service.send_gdpr_request(domain, privacy_email)
                results[domain] = "Request sent successfully" if success else "Failed to send request"
            else:
                results[domain] = "No privacy email found"
        except Exception as e:
            results[domain] = f"Error: {str(e)}"
    
    return templates.TemplateResponse(
        "results.html", 
        {"request": request, "results": results}
    )

if __name__ == "__main__":
    # Default port to 8000 if not specified in environment
    port = int(os.getenv("PORT", 8000))
    
    # Run the application
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True) 