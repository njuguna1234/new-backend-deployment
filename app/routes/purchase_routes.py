from flask import Blueprint, jsonify, request
from app.models import Purchase, db

purchase_bp = Blueprint('purchases', __name__)

@purchase_bp.route('/purchases', methods=['GET'])
def get_purchases():
    purchases = Purchase.query.all()
    return jsonify([purchase.to_dict() for purchase in purchases])

@purchase_bp.route('/purchases', methods=['POST'])
def create_purchase():
    data = request.get_json()
    new_purchase = Purchase(
        user_id=data.get('user_id'),
        artwork_id=data.get('artwork_id')
    )
    db.session.add(new_purchase)
    db.session.commit()
    return jsonify(new_purchase.to_dict()), 201
