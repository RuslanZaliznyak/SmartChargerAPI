from app.api import bp
from flask import jsonify


@bp.route('/')
def main():
    return jsonify(test='test value')
