class Bookmarks():
    def __init__(self, lat, lng, date, time, earth_quake=False, air_quality=False):
        self.lat = lat
        self.lng = lng
        self.date = date
        self.time = time
        self.earth_quake = earth_quake
        self.air_quality = air_quality
    
    def __str__(self):
        return f'The ISS flew over {self.lat}, {self.lng} at {self.time} on {self.date}.'

