import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    region = rec['region_name']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    
    print(f'[*] Target: {tgt} Geo-located.')
    print(f'[+] Location: {city}, {region}, {country}')
    print(f'[+] Latitude: {lat}, Longitude: {long}')

tgt = '127.0.0.1'
printRecord(tgt)
