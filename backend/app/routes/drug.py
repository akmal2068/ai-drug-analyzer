import requests
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..utils.report_generator import save_report

drug_bp = Blueprint("drug", __name__)

@drug_bp.route("/drug-info", methods=["POST"])
@jwt_required()
def drug_info():
    drug = request.json.get("drug")

    url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug}&limit=1"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Drug not found"}), 404

    result = response.json()["results"][0]

    data = {
        "description": result.get("description", ["Not available"])[0],
        "uses": result.get("indications_and_usage", ["Not available"])[0],
        "side_effects": result.get("adverse_reactions", ["Not available"])[0]
    }

    save_report(drug, data)

    return jsonify({"name": drug, **data})