from pydantic import BaseModel


class SoilData(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    sodium: float
    iron: float
    zinc: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float
