from fastapi import FastAPI
from starlette.responses import HTMLResponse

from routes import router
from fastapi import APIRouter, HTTPException


app = FastAPI()

# Include routers
app.include_router(router)

main_router = APIRouter()

# Route to display all available routes
@main_router.get("/", response_class=HTMLResponse)
async def main_page():
    route_info = "<h1>Available Routes:</h1>"
    for route in app.routes:
        route_info += f"<p><strong>{route.path}</strong>: {route.methods}</p>"
    return route_info

# Include the main router in the app
app.include_router(main_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)