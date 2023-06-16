from fastapi import FastAPI

from middleware.error_handler import ErrorHandler

from routers.user import user_router

# APP_INFO
app = FastAPI()
app.title = "Match"
app.version = "0.0.1"

# MIDDLEWARE
app.add_middleware(ErrorHandler)

# ROUTERS
app.include_router(user_router)