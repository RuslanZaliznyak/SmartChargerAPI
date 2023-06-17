import json

from app.api import bp
from flask import jsonify, request
from app.services.api_services import APIHandler
from pydantic import ValidationError
from app.services.db_services import DataBaseManager as db_manager

"""
- Accept recording requests
- 
"""


@bp.route('/api/get', methods=['GET'])
def get_records():
    results = db_manager.get()
    data = []
    for result in results:
        record = {
            'id': result[0],
            'value1': float(result[1]),
            'value2': float(result[2])
        }
        data.append(record)

    json_data = json.dumps(data)

    return json_data


@bp.route('/api/test', methods=['POST'])
def add_record():
    post_handler = APIHandler.post_handler(request)
    if not isinstance(post_handler, ValidationError):
        db_manager.post(data=post_handler)
        return jsonify(test='ok')
    else:
        return jsonify(errors=post_handler.errors())
