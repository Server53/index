from fastapi import FastAPI

from .cors import setup_cors
from .logging_ import *

app = FastAPI()

setup_cors(app)


from .modules.auth import router as auth_router
from .modules.files import router as files_router
from .modules.minecraft import router as minecraft_router

app.include_router(auth_router, prefix='/auth')
app.include_router(files_router, prefix='/files')
app.include_router(minecraft_router, prefix="/minecraft")
