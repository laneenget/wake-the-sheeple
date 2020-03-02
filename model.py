class Bookmarks():
    def __init__(self, dateTime, lat, lng, magnitude=0.0, qual_val=""):
        self.dateTime = dateTime
        self.lat = lat
        self.lng = lng
        self.magnitude = magnitude
        self.qual_val = qual_val
    
    def __str__(self):
        # if(earth_quake and air)
        return f'The ISS flew over {self.lat}, {self.lng} on {dateTime}.'

