from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# Pydantic Model


class Application(BaseModel):
    id: int
    fullName: str
    email: str
    phone: str
    whatsappNumber: str
    university: str
    course: str
    level: str
    track: str
    motivation: str
    portfolioLink: str
    resumeLink: str
    joinInnovationClub: bool
    status: str
    submittedAt: str



# Mock Data

applications = [
    {
        "id": 2,
        "fullName": "Ama Serwaa Owusu",
        "email": "amaserwaa@gmail.com",
        "phone": "0245567812",
        "whatsappNumber": "0245567812",
        "university": "University of Ghana",
        "course": "Computer Engineering",
        "level": "2nd Year",
        "track": "Embedded Systems",
        "motivation": "I want to gain hands-on experience in embedded systems and IoT development.",
        "portfolioLink": "https://github.com/amase",
        "resumeLink": "https://linkedin.com/in/amase",
        "joinInnovationClub": True,
        "status": "accepted",
        "submittedAt": "2026-05-04T10:12:45Z"
    },

    {
        "id": 3,
        "fullName": "Yaw Mensah",
        "email": "yawmensah@gmail.com",
        "phone": "0558876123",
        "whatsappNumber": "0558876123",
        "university": "KNUST",
        "course": "Electrical Engineering",
        "level": "4th Year",
        "track": "Radar & RF Systems",
        "motivation": "To improve my knowledge in RF systems, radar engineering, and wireless communications.",
        "portfolioLink": "https://github.com/yawmensah",
        "resumeLink": "https://linkedin.com/in/yawmensah",
        "joinInnovationClub": True,
        "status": "pending",
        "submittedAt": "2026-05-05T08:45:30Z"
    },

    {
        "id": 4,
        "fullName": "Pricilla Adjei",
        "email": "pricillaadjei@gmail.com",
        "phone": "0203344556",
        "whatsappNumber": "0203344556",
        "university": "Ashesi University",
        "course" : "Software Engineering",
        "level" : "3rd Year",
        "track": "Backend Engineering",
        "motivation": "I want to stregthen my backend engineering skills using FastAPU and modern software architecture.",
        "portfolioLink": "https://github.com/pricillaadjei",
        "resumeLink": "https://linkedin.com/in/pricillaadjei",
        "joinInnovationClub": True,
        "status": "accepted",
        "submittedAt": "2026-05-06T14:18:22Z"
    },

    {
        "id": 5,
        "fullName": "Daniel Kofi Asante",
        "email": "danielasante@gmail.com",
        "phone": "0277788990",
        "whatsappNumber": "0277788990",
        "university": "UENR",
        "course" : "Biomedical Engineering",
        "level" : "2nd Year",
        "track": "Biomedical Systems",
        "motivation": "I want to stregthen my backend engineering skills using FastAPU and modern software architecture.",
        "portfolioLink": "https://github.com/danieasante",
        "resumeLink": "https://linkedin.com/in/danieasante",
        "joinInnovationClub": False,
        "status": "rejected",
        "submittedAt": "2026-05-07T11:05:10Z"
    }
]


# Home Route


@app.get("/")
def home():
    return {"message": "Backend API is running"}


# GET All Applications


@app.get("/applications")
def get_applications():
    return applications

# GET Single Application

@app.get("/applications/{application_id}")
def get_application(application_id: int):

    for app_data in applications:
        if app_data["id"] == application_id:
            return app_data

    raise HTTPException(status_code=404, detail="Application not found")

# CREATE Application

@app.post("/applications")
def create_application(application: Application):

    applications.append(application.dict())

    return {
        "message": "Application created successfully",
        "data": application
    }

# UPDATE Application

@app.put("/applications/{application_id}")
def update_application(application_id: int, updated_application: Application):

    for index, app_data in enumerate(applications):

        if app_data["id"] == application_id:

            applications[index] = updated_application.dict()

            return {
                "message": "Application updated successfully",
                "data": updated_application
            }

    raise HTTPException(status_code=404, detail="Application not found")

# DELETE Application

@app.delete("/applications/{application_id}")
def delete_application(application_id: int):

    for index, app_data in enumerate(applications):

        if app_data["id"] == application_id:

            deleted_app = applications.pop(index)

            return {
                "message": "Application deleted successfully",
                "data": deleted_app
            }

    raise HTTPException(status_code=404, detail="Application not found")