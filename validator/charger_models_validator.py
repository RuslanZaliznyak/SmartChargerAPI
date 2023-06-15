import datetime as datetime
import re

from pydantic import BaseModel, Field, validator


class ChargerInput(BaseModel):
    barcode: int = Field(..., ge=100000, le=999999)
    datetime: datetime.datetime
    voltage: float
    temperature: float

    @validator('voltage')
    def is_correct_decimal(cls, voltage):
        voltage_regext = r'^\d+(\.\d{1,2})?$'
        return re.match(voltage_regext, voltage) is not None

    @validator('temperature')
    def is_correct_temperature(cls, temperature):
        temperature_regex = r'^\d{1,2}(\.\d{1})?$'
        return re.match(temperature_regex, temperature) is not None
