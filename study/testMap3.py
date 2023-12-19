import googlemaps
from datetime import datetime

# API 키를 입력하세요.
gmaps = googlemaps.Client(key='AIzaSyCUzWM4L4iAj-krLKiEx3MkD-j0HrqlNrs')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result = gmaps.geocode('1600 Amphitheatre Pk', 
                                          region='US',
                                          components={'locality': 'Mountain View'},
                                          result_type='postal_code')

print("Geocode Result:", geocode_result)
print("Reverse Geocode Result:", reverse_geocode_result)
print("Directions Result:", directions_result)
print("Address Validation Result:", addressvalidation_result)