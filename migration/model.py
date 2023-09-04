from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

import string

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define a one-to-many relationship between Customer and Review
    reviews = relationship('Review', back_populates='customer')
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Find the restaurant with the highest star rating from this customer
        highest_rating = 0
        favorite = None
        for review in self.reviews:
            if review.rating > highest_rating:
                highest_rating = review.rating
                favorite = review.restaurant
        return favorite

    def add_review(self, restaurant, rating):
        # Create a new review for the restaurant with the given rating
        review = Review(customer=self, restaurant=restaurant, rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
        # Remove all reviews for this customer and restaurant
        for review in self.reviews:
            if review.restaurant == restaurant:
                session.delete(review)
        session.commit()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    # Define a one-to-many relationship between Restaurant and Review
    reviews = relationship('Review', back_populates='restaurant')

    @classmethod
    def fanciest(cls):
        # Use SQLAlchemy query methods to find the fanciest restaurant
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        # Get all reviews for this restaurant
        reviews_list = []
        for review in self.reviews:
            reviews_list.append(review.full_review())
        return reviews_list

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)  # Change the data type to Integer
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    # Define many-to-one relationships between Review and Customer/Restaurant
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars"


# Create a SQLite database and tables
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()