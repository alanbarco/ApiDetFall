from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI( )

class AlertaItem(BaseModel):
    mensaje: str
    location: str

@app.post("/alerta")
def alerta(alerta: AlertaItem):
    return {"message": "Alerta recibida!!"}