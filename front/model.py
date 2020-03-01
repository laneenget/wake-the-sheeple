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
    
    def __str__(self):
        return f'The ISS flew over {self.lat}, {self.lng} at {self.time} on {self.date}.'

    def conspiracy(self):
        if (self.earth_quake and self.air_quality):
            print(f'SOMEHOW, the air quality is bad and there was an earthquake. Right under the satelite, so weird, must be the world government.')
        elif(self.earth_quake):
            print(f'SOMEHOW, there was an earthquake right under the International Space Station. So wierd, must be the illuminatity')
        elif(self.air_quality):
            print(f'SOMEHOW, the air quality below the Internation Space Station just HAPPENS to be bad. Weird, must be the illuminaty world government.')
        else:
            print(f'All is well, the world government is sparing us today.')
