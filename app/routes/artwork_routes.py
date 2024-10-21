from flask import Blueprint, jsonify, request
from app.models import Artwork, db

artwork_bp = Blueprint('artworks', __name__)

@artwork_bp.route('/artworks', methods=['GET'])
def get_artworks():
    artworks = Artwork.query.all()
    return jsonify([artwork.to_dict() for artwork in artworks])

@artwork_bp.route('/artworks', methods=['POST'])
def create_artwork():
    data = request.get_json()
    new_artwork = Artwork(
        title=data.get('title'),
        artist=data.get('artist'),
        price=data.get('price')
    )
    db.session.add(new_artwork)
    db.session.commit()
    return jsonify(new_artwork.to_dict()), 201
