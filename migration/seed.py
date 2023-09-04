from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Customer, Restaurant, Review

# Create a SQLite database and tables (if not already created)
engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()


# Create multiple customers
customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Willow", last_name="Smith")
customer3 = Customer(first_name="Angela", last_name="Season")

# Create multiple restaurants
restaurant1 = Restaurant(name="Fanciest Restaurant", price=50.0)
restaurant2 = Restaurant(name="VineYard Restaurant", price=60.0)
restaurant3 = Restaurant(name="BrackenHurst Restaurant", price=49.0)

# Create multiple reviews
review1 = Review(customer=customer1, restaurant=restaurant1, rating=4)
review2 = Review(customer=customer2, restaurant=restaurant2, rating=3)
review3 = Review(customer=customer3, restaurant=restaurant3, rating=6)

# Add the objects to the session
session.add_all([customer1, customer2, customer3, restaurant1, restaurant2, restaurant3, review1, review2, review3])

session.commit()


session.close()