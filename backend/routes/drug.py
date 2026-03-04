import requests
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

drug_bp = Blueprint("drug", __name__)

@drug_bp.route("/drug-info", methods=["POST"])
@jwt_required()
def drug_info():
    drug = request.json.get("drug")

    url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug}&limit=1"

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Drug not found"}), 404

    data = response.json()["results"][0]

    return jsonify({
        "name": drug,
        "description": data.get("description", ["Not available"])[0],
        "uses": data.get("indications_and_usage", ["Not available"])[0],
        "side_effects": data.get("adverse_reactions", ["Not available"])[0]
    })