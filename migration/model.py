from model import Customer, Restaurant, Review, session

fanciest_restaurant = Restaurant.fanciest()
if fanciest_restaurant:
    print(f"Fanciest Restaurant: {fanciest_restaurant.name}, Price: {fanciest_restaurant.price}")
else:
    print("No restaurants found in the database.")