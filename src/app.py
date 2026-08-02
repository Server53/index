from fastapi import FastAPI

from .cors import setup_cors

app = FastAPI()

setup_cors(app)


from .modules.auth import router as auth_router
from .modules.files import router as files_router

app.include_router(auth_router, prefix='/auth')
app.include_router(files_router, prefix='/files')
