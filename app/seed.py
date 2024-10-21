from app import db
from app.models import User, Artwork, Review, Purchase

def seed_data():
    user1 = User(username='artist1', email='artist1@example.com')
    user2 = User(username='buyer1', email='buyer1@example.com')
    
    artwork1 = Artwork(title='Sunset', price=200, artist=user1)
    artwork2 = Artwork(title='Abstract', price=150, artist=user1)

    review1 = Review(content='Amazing artwork!', rating=5, user=user2, artwork=artwork1)
    
    purchase1 = Purchase(user=user2, artwork=artwork1, quantity=1)

    db.session.add_all([user1, user2, artwork1, artwork2, review1, purchase1])
    db.session.commit()
