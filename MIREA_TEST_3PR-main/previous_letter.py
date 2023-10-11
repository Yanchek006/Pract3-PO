def check_letters(previous_city, new_city):
    if previous_city[-1] in ['ъ','ь','ы','й']:
        i = 2
    else:
        i = 1

    if previous_city[-i].upper() == new_city[0]:
        return True
    else:
        return False