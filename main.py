from fastapi import FastAPI, status
from pydantic_types import NumRequest

# Commands to start the server
# dev: fastapi dev
# prod: fastapi run

app = FastAPI()

# TO DO: endpoint testing/error handling
# Optional: React UI

@app.get("/health", status_code=status.HTTP_200_OK)
async def do_health_check():
    return {"status": "healthy", "message": "Service is running"}

# _______________________________________________________________________________
# CRUD endpoints: Will need mock data/database/ORM for meaningful functionality

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
# _______________________________________________________________________________

@app.get("/data/{id}")
def get_data_by_id(id: int):
    return {"message": f"Data for ID {id}", "id": id}

@app.get("/data")
def get_partial_data(skip: int = 0, limit: int = 5):
    data_ids = list(range(skip, skip + limit))
    return {"message": "Get partial data ids", "skip": skip, "limit": limit, "data_ids": data_ids}  

@app.get("/num")
def get_num(num: int):
    return {"message": f"Get data for num: {num}", "num": num}

@app.get("/num2")
def get_num_with_request_model(num_info: NumRequest = {"num": 0}):
    return {"message": "Get num request data", "num_request": num_info}

@app.get("/num3")
def get_num_with_model_dump(num_request: NumRequest):
    return {"message": "Get num request data", "num_request_dict": num_request.model_dump()}

@app.get("/nums")
def get_filtered_nums(min_num: int = 0):
    nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_nums = [num for num in nums if num >= min_num]
    return {"message": f"Get data with filter min num: {min_num}", "min_num": min_num, "filtered_nums": filtered_nums}