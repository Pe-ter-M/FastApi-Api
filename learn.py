from fastapi import FastAPI,Body, HTTPException,status


app = FastAPI()

users ={ 
   1: {"name":"peter"},
    2:{"name":"Jane"}
}

@app.get("/")
async def read_root():
    return {'Hello':"world"}

@app.get("/users/{id}")
async def get_user(id:int):
    print(id)
    user = users.get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'This id {id} not found')
    return {'user':user}

@app.post('/')
async def receive_data(payload: dict = Body()):
    print(payload)
    return {'data received'}