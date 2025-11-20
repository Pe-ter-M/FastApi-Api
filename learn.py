from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_root():
    return {'Hello':"world"}

@app.post('/')
async def receive_data():
    return {'data received'}