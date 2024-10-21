from flask import Blueprint, jsonify, request
from app.models import Review, db

review_bp = Blueprint('reviews', __name__)

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])

@review_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    new_review = Review(
        content=data.get('content'),
        user_id=data.get('user_id'),
        artwork_id=data.get('artwork_id')
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201
