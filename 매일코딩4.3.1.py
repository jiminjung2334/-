def get_rainfall():
    rainfall = {}

    while True:
        city_name = input('Enter city name')
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')

