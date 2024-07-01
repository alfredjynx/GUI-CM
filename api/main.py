# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
import routes

app = FastAPI()
app.include_router(routes.router)

@app.get("/")
def root():
    return {"Hello": "World"}