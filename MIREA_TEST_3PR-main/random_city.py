from random import shuffle


def choose_random_city(cities, used_cities):

    if not used_cities:
        shuffle(cities)
        return cities[0]
    
    last_used = used_cities[-1]
    free_cities = list(set(cities) - set(used_cities))
    if not free_cities:
        return None
    else:
        shuffle(free_cities)
        for city in free_cities:
            if last_used[-1] in ['ъ','ь','ы','й']:
                i = 2
            else:
                i = 1

            if last_used[-i].upper() == city[0]:
                return city
        
        return None