def handle_air_n_quake_exceptions(qual_er_mag):
    if qual_er_mag==0:
        print( 'There is an issue with the credentials. Please contact your developer.')
        return None
    elif qual_er_mag==-1:
        print('There was an issue with the location. Please contact your developer.')
        return None
    elif qual_er_mag:
        return qual_er_mag
    else:
        return None
