import datetime

from app.validator.charger_models_validator import ChargerInput
from flask import request


def post_handler(raw_data: request):
    try:
        data = raw_data.get_data()
        print(data)
        if ChargerInput(
            barcode=data['barcode'],
            voltage=data['voltage'],
            temperature=data['temperature'],
            datetime=datetime.datetime.now()
        ):
            return 'dobre'
    except Exception:
        return 'not ok'
