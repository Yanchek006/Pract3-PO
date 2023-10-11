def add_city_to_used(city_list, city):
    if isinstance(city, str) and isinstance(city_list, list):
        try:
            city_list.append(city)
            return city_list
        except:
            print("Unknown Error")
            return None
    else:
        print("Incorrect Type Error")
        return None