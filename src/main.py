from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from app.routes.book_routes import router as book_router
from app.routes.ui_routes import ui

api = FastAPI()

api.include_router(book_router)

api.mount("/", WSGIMiddleware(ui))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="127.0.0.1", port=8000)

# Entry point for the app, Flask for UI and FastAPI for API endpoints.
# WSGIMiddle allows Flask (which uses WSGI) to run along FastAPI (which uses ASGI).