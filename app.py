from fastapi import FastAPI

from .cors import setup_cors

app = FastAPI()

setup_cors(app)
