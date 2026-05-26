from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}
  
@app.get('/about')
def about():
    return {"message": "campusx is an education platform where you can learn AI/ML"}