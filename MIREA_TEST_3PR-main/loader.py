def load_cities(path):
    with open(path, 'r', encoding='utf8') as f:
        cities = f.readlines()
        # trim /n
        cities = [city.strip() for city in cities]
    return cities