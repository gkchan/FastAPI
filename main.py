from fastapi import FastAPI

# Commands to start the server
# dev: fastapi dev
# prod: fastapi run

app = FastAPI()

@app.get("/")
def get_data():
    return {"message": "Sample data"}

@app.post("/")
def create_data():
    return {"message": "Data created", "data": "Data"}

@app.put("/")
def update_data():
    return {"message": "Data updated", "data": "Updated data"}

@app.delete("/")
def delete_data():
    return {"message": "Data deleted"}

@app.get("/data/{id}")
def get_data_by_id(id: int):
    return {"message": f"Data for ID {id}", "id": id}