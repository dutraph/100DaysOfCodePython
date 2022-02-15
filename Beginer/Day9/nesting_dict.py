nested_dict = {
    'colours': {'black', 'blue', 'red', 'green', 'yellow', 'brown'},
    'weekdays': {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'},
    'numbers': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12,
        'top_rated_place': "Paris",
    },
    "Portugal": {
        'cities_visited': ['Braga', 'Porto', 'Lisbon']
    }
}

# Nesting Dictionary in a List
travel_log_list = [
    {
        'country': "France",
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12,
        'top_rated_place': "Paris",
        'has_valid_visa': True
    },
    {
        'country': "Portugal",
        'cities_visited': ['Braga', 'Porto', 'Lisbon'],
        'total_visits': 20,
        'top_rated_place': "Porto",
        'has_valid_visa': True
    }
]

print(travel_log_list[1]["top_rated_place"])