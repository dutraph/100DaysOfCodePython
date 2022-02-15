travel_log = [
    {
        'country': "France",
        'total_visits': 12,
        'cities_visited': ['Paris', 'Lille', 'Dijon']
    },
    {
        'country': "Portugal",
        'total_visits': 20,
        'cities_visited': ['Braga', 'Porto', 'Lisbon']
    },
]


def add_country(country_name, numb_of_visits, cities_list):
    travel_log.append({'country': country_name,
                       'total_visits': numb_of_visits,
                       'cities_visited': cities_list
                       })


country = input("Enter the Country name: ")
visits = int(input("How many time did you visit this country: "))
cities = input("Enter the cities have you been to: ").split(" ")

add_country(country, visits, cities)

print(travel_log)