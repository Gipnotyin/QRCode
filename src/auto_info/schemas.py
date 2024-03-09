from datetime import datetime

from pydantic import BaseModel


class Auto(BaseModel):
    vin: str
    mark: str
    model: str
    modelYear: str
    year: int
    date: datetime
    equipment: str
    bodywork: str
    package: str
    color: str
    department: str
