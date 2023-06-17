from app.validator.charger_models_validator import ChargerInput
from flask import request
from pydantic import ValidationError


class APIHandler:
    @classmethod
    def post_handler(cls, data_form: request):
        try:
            data = data_form.get_json()
            return ChargerInput(
                barcode=int(data['barcode']),
                voltage=float(data['voltage']),
                temperature=float(data['temperature'])
            )

        except ValidationError as ex:
            return ex
