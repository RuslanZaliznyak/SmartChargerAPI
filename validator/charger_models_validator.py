import datetime as datetime
import re
from pydantic import BaseModel, Field, validator


class ChargerInput(BaseModel):
    barcode: int = Field(..., ge=100000, le=999999)
    voltage: float
    temperature: float
    datetime: datetime.datetime | None

    @validator('voltage')
    def validate_voltage(cls, voltage):
        if not isinstance(voltage, float):
            raise ValueError('Voltage must be a float')
        if voltage > 4.5:
            raise ValueError('Voltage must be between 0 and 4.5')
        return voltage

    @validator('temperature')
    def validate_temperature(cls, temperature):
        if not isinstance(temperature, float):
            raise ValueError('Voltage must be a float')
        if temperature > 120:
            raise ValueError('Voltage must be between 0 and 4.5')
        return temperature



