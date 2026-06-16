from fastapi import FastAPI

# Commands to start the server
# dev: fastapi dev
# prod: fastapi run

app = FastAPI()

@app.get("/")
def get_data():
    return {"message": "Sample data"}