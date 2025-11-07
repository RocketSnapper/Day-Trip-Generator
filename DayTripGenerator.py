import random 

destinations = ['Nashville', 'Houston', 'Atlanta', 'Boston']
restaurants = ['Chipotle', 'Red Robin', 'Buffalo Wild Wings', 'Mcdonalds']
transportations = ['Bus', 'Train', 'Car', 'Plane']
entertainments = ['Movies', 'Hockey', 'MMA', 'Basketball']

def randomize_destination():
    random_destination = random.choice(destinations)
    return random_destination
random_destination = randomize_destination()

def randomize_restaurant():
    random_restaurant = random.choice(restaurants)
    return random_restaurant
random_restaurant = randomize_restaurant()

def randomize_transportation():
    random_transportation = random.choice(transportations)
    return random_transportation
random_transportation = randomize_transportation()

def randomize_entertainment():
    random_entertainment = random.choice(entertainments)
    return random_entertainment
random_entertainment = randomize_entertainment()

def display_trip_details():
     print(f'Your randomized trip is going to {random_destination}, riding by {random_transportation}, eating at {random_restaurant}, followed by an evening enjoying {random_entertainment}.')
display_trip_details()





