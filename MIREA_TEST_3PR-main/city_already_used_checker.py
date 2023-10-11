def is_city_used(city_list, city):
    if isinstance(city, str) and isinstance(city_list, list):
        try:
            if city in city_list:
                return True
            else:
                return False
        except:
            print("Unknown Error")
            return None
    else:
        print("Incorrect Type Error")
        return None