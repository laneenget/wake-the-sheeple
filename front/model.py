class Bookmarks():
    def __init__(self, lat, lng, date, time,  country_name, earth_quake=False, air_quality=False, state_name='', city_name=''):
        self.lat = lat
        self.lng = lng
        self.date = date
        self.time = time
        self.earth_quake = earth_quake
        self.air_quality = air_quality
        self.country_name = country_name
        self.state_name = state_name
        self.city_name = city_name