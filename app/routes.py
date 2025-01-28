from flask import Blueprint, jsonify
from app.models.Adventure import Adventure

adventures_bp = Blueprint("adventures", __name__, url_prefix="/adventures")

# adventures
@adventures_bp.route("", methods=["GET"])
def get_adventures():
    adventures = Adventure.query.all()
    response = []
    for adv in adventures:
        response.append(adv.to_dict())
    return jsonify(response)
