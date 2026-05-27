from fastapi import FastAPI, HTTPException, Path HTTPException

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
    return data


@app.get("/")
def home():
    return {"message": "Patient management system API"}
  
@app.get('/about')
def about():
    return {"message": "A fully functional API to manage your patient records"}
  
  
@app.get('/view')
def view():
    data = load_data()
    return data


@app.get('patient/{patient_id}')
def view_patient(patient_id: str = Path('patient_id', description='The ID of the patient in the DB', example='p001')):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")