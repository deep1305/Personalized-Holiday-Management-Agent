from  fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from autogen_agentchat.messages import TextMessage
from Personalized_Holiday_Management.teams.holiday_team import holiday_team

class HolidayRequest(BaseModel):
    content: str
    source: str = "user"

app = FastAPI(title = "Holiday Management API")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/plan-trip")
async def plan_trip(request: HolidayRequest):
    try:
        task = TextMessage(content=request.content, source=request.source)
        response = await holiday_team.run(task=task)
        messages = [{"role": message.source, "content": message.content} for message in response.messages]
        return {"messages": messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

