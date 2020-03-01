class Bookmarks():
    def __init__(self, lat, lng, date, time, earth_quake=False, air_quality=False, magnitude=0.0, qual_val=""):
        self.lat = lat
        self.lng = lng
        self.date = date
        self.time = time
        self.earth_quake = earth_quake
        self.air_quality = air_quality
        self.magnitude = magnitude
        self.qual_val = qual_val
    
    def __str__(self):
        # if(earth_quake and air)
        return f'The ISS flew over {self.lat}, {self.lng} at {self.time} on {self.date}.'

