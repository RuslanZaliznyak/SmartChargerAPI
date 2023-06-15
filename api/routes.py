from app.api import bp
from flask import jsonify, request
from app.services.charger_post_handler import post_handler

"""
- Accept recording requests
- 
"""


@bp.route('/api/test', methods=['POST'])
def add_record():
    print(post_handler(request))
    return jsonify(test='ok')
