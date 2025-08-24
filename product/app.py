from fastapi import FastAPI
from product.api.router import router

app = FastAPI()
app.include_router(router)
