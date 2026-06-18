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

@app.get("/data")
def get_partial_data(skip: int = 0, limit: int = 5):
    data_ids = list(range(skip, skip + limit))
    return {"message": "Get partial data ids", "skip": skip, "limit": limit, "data_ids": data_ids}  