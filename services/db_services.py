from datetime import datetime

from sqlalchemy import and_

from app.extensions import db
from app.validator.charger_models_validator import ChargerInput
from app.services.api_services import APIHandler
from app.models.charger_models import Record, Parameters, Voltage, Temperature
from sqlalchemy.ext.declarative import DeclarativeMeta


class DataBaseManager:
    @classmethod
    def get_or_create_record(cls, model, field_name, value) -> int:
        record = model.query.filter_by(**{field_name: value}).first()
        if record is None:
            new_record = model(**{field_name: value})
            db.session.add(new_record)
            db.session.flush()
            db.session.refresh(new_record)
            return new_record.id
        return record.id

    @classmethod
    def get(cls):
        query = db.session.query(
            Record.barcode,
            Voltage.voltage,
            Temperature.temperature
        ).join(
            Parameters, Record.params_id == Parameters.id
        ).join(
            Temperature, Parameters.temp_id == Temperature.id
        ).join(
            Voltage, Parameters.voltage_id == Voltage.id)

        return query.all()

    @classmethod
    def post(cls, data: ChargerInput):
        temp_id = cls.get_or_create_record(Temperature, 'temperature', data.temperature)
        voltage_id = cls.get_or_create_record(Voltage, 'voltage', data.voltage)

        params = db.session.query(Parameters).filter(
            and_(Parameters.temp_id == temp_id, Parameters.voltage_id == voltage_id)
        ).first()

        if params:
            params_id = params.id
        else:
            new_params = Parameters(
                voltage_id=voltage_id,
                temp_id=temp_id
            )
            db.session.add(new_params)
            db.session.flush()  # Flush to get the ID before committing
            params_id = new_params.id

        new_record = Record(
            barcode=data.barcode,
            params_id=params_id
        )
        db.session.add(new_record)
        db.session.commit()

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass
