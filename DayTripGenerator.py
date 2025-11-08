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

def ask_approval():
    trip_approval = input('Are you satisfied with your trip details?')
    return trip_approval
trip_approval = ask_approval()

def adjust_trip():
    global random_destination, random_entertainment, random_transportation, random_restaurant, trip_approval
    while trip_approval == 'No' or trip_approval == 'no':
        change_required = input('Would you like to change destination, transportation, entertainment, restaurant?')
        if change_required == 'Destination' or change_required == 'destination':
            destinations.remove(random_destination)
            random_destination = randomize_destination()
            print(f'Your new randomized trip is going to {random_destination}, riding by {random_transportation}, eating at {random_restaurant}, followed by an evening enjoying {random_entertainment}.')
            trip_approval = ask_approval()
        elif change_required == 'Transportation' or change_required == 'transportation':
            transportations.remove(random_transportation)
            random_transportation = randomize_transportation()
            print(f'Your new randomized trip is going to {random_destination}, riding by {random_transportation}, eating at {random_restaurant}, followed by an evening enjoying {random_entertainment}.')
            trip_approval = ask_approval()
        elif change_required == 'Restaurant' or change_required == 'restaurant':
            restaurants.remove(random_restaurant)
            random_restaurant = randomize_restaurant()
            print(f'Your new randomized trip is going to {random_destination}, riding by {random_transportation}, eating at {random_restaurant}, followed by an evening enjoying {random_entertainment}.')
            trip_approval = ask_approval()
        elif change_required == 'Entertainment' or change_required == 'entertainment':
            entertainments.remove(random_entertainment)
            random_entertainment = randomize_entertainment()
            print(f'Your new randomized trip is going to {random_destination}, riding by {random_transportation}, eating at {random_restaurant}, followed by an evening enjoying {random_entertainment}.')
            trip_approval = ask_approval()
        else:
            print('Incorrect selection, try again')

adjust_trip()


def final_trip():  
    print(f'Congratulations, your trip is going to {random_destination}, riding by {random_transportation}, eating at {random_restaurant}, followed by an evening enjoying {random_entertainment}.')
final_trip()