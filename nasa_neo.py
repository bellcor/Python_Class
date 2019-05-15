#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# learning about NASA near earth objects API

import requests
import pprint

# Add in a start date - YYYY-MM-DD
# Ask user for input of start date
#START_DATE = input("What is your start date? (FORMAT = YYYY-MM-DD): ")
START_DATE = '2019-05-14'

# Add in an end date - YYYY-MM-DD
# Ask user for input of end date
#END_DATE = input("What is your end date? (NOTE: CAN ONLY BE UP TO 7 DAYS AFTER START DATE) (FORMAT = YYYY-MM-DD): ")
END_DATE = '2019-05-15'

# Lookup NASA API example:
# GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY
def main():
    # Define my API key (from a file)
    with open("/Users/bellcor/keystore/api.nasa.gov.key") as keyfile:
        mykey = keyfile.read()

    asteroids = requests.get(r"https://api.nasa.gov/neo/rest/v1/feed?start_date=" + START_DATE + "&end_date=" + END_DATE + "&api_key=" + mykey)
    rock_data = (asteroids.json())
    #pprint.pprint(rock_data)

''' data before any of the changes below:
txslmacl2254:python_scripts bellcor$ ./nasa_neo.py
{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/3841774?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '3841774', 'neo_reference_id': '3841774', 'name': '(2019 JO3)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3841774', 'absolute_magnitude_h': 24.402, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.0350070066, 'estimated_diameter_max': 0.0782780465}, 'meters': {'estimated_diameter_min': 35.0070066134, 'estimated_diameter_max': 78.2780464762}, 'miles': {'estimated_diameter_min': 0.0217523387, 'estimated_diameter_max': 0.048639708}, 'feet': {'estimated_diameter_min': 114.8523875773, 'estimated_diameter_max': 256.8177460011}}, 'is_potentially_hazardous_asteroid': False, 'close_approach_data': [{'close_approach_date': '2019-05-14', 'epoch_date_close_approach': 1557817200000, 'relative_velocity': {'kilometers_per_second': '10.8281268855', 'kilometers_per_hour': '38981.2567879548', 'miles_per_hour': '24221.4370302711'}, 'miss_distance': {'astronomical': '0.0472990803', 'lunar': '18.3993415833', 'kilometers': '7075841.5', 'miles': '4396724'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}

{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/3753078?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '3753078', 'neo_reference_id': '3753078', 'name': '(2016 JG18)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3753078', 'absolute_magnitude_h': 18.6, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.5064714588, 'estimated_diameter_max': 1.1325046106}, 'meters': {'estimated_diameter_min': 506.4714588346, 'estimated_diameter_max': 1132.5046106177}, 'miles': {'estimated_diameter_min': 0.3147066768, 'estimated_diameter_max': 0.7037055224}, 'feet': {'estimated_diameter_min': 1661.651821003, 'estimated_diameter_max': 3715.566426699}}, 'is_potentially_hazardous_asteroid': False, 'close_approach_data': [{'close_approach_date': '2019-05-14', 'epoch_date_close_approach': 1557817200000, 'relative_velocity': {'kilometers_per_second': '29.8750027007', 'kilometers_per_hour': '107550.0097225837', 'miles_per_hour': '66827.3935412354'}, 'miss_distance': {'astronomical': '0.4843997107', 'lunar': '188.4314880371', 'kilometers': '72465168', 'miles': '45027768'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}

{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/3841617?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '3841617', 'neo_reference_id': '3841617', 'name': '(2019 HG3)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3841617', 'absolute_magnitude_h': 23.045, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.0653965709, 'estimated_diameter_max': 0.1462311781}, 'meters': {'estimated_diameter_min': 65.3965709182, 'estimated_diameter_max': 146.2311780686}, 'miles': {'estimated_diameter_min': 0.0406355327, 'estimated_diameter_max': 0.0908638133}, 'feet': {'estimated_diameter_min': 214.5556857314, 'estimated_diameter_max': 479.7610982545}}, 'is_potentially_hazardous_asteroid': False, 'close_approach_data': [{'close_approach_date': '2019-05-15', 'epoch_date_close_approach': 1557903600000, 'relative_velocity': {'kilometers_per_second': '3.4771823215', 'kilometers_per_hour': '12517.8563574756', 'miles_per_hour': '7778.1091350103'}, 'miss_distance': {'astronomical': '0.273292175', 'lunar': '106.3106613159', 'kilometers': '40883928', 'miles': '25404096'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}

{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/3841626?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '3841626', 'neo_reference_id': '3841626', 'name': '(2019 HT3)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3841626', 'absolute_magnitude_h': 21.848, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.1134893155, 'estimated_diameter_max': 0.2537698242}, 'meters': {'estimated_diameter_min': 113.489315498, 'estimated_diameter_max': 253.7698241734}, 'miles': {'estimated_diameter_min': 0.0705189695, 'estimated_diameter_max': 0.1576852094}, 'feet': {'estimated_diameter_min': 372.3402858584, 'estimated_diameter_max': 832.578189941}}, 'is_potentially_hazardous_asteroid': False, 'close_approach_data': [{'close_approach_date': '2019-05-15', 'epoch_date_close_approach': 1557903600000, 'relative_velocity': {'kilometers_per_second': '16.8735739967', 'kilometers_per_hour': '60744.8663881117', 'miles_per_hour': '37744.4976732131'}, 'miss_distance': {'astronomical': '0.2336411491', 'lunar': '90.8864059448', 'kilometers': '34952220', 'miles': '21718302'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}

{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/3836849?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '3836849', 'neo_reference_id': '3836849', 'name': '(2018 XM2)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3836849', 'absolute_magnitude_h': 25.4, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.022108281, 'estimated_diameter_max': 0.0494356193}, 'meters': {'estimated_diameter_min': 22.1082810359, 'estimated_diameter_max': 49.435619262}, 'miles': {'estimated_diameter_min': 0.0137374447, 'estimated_diameter_max': 0.0307178602}, 'feet': {'estimated_diameter_min': 72.5337327539, 'estimated_diameter_max': 162.1903570994}}, 'is_potentially_hazardous_asteroid': False, 'close_approach_data': [{'close_approach_date': '2019-05-15', 'epoch_date_close_approach': 1557903600000, 'relative_velocity': {'kilometers_per_second': '11.8703375826', 'kilometers_per_hour': '42733.2152974669', 'miles_per_hour': '26552.7581385844'}, 'miss_distance': {'astronomical': '0.3119367629', 'lunar': '121.3433990479', 'kilometers': '46665076', 'miles': '28996334'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}

{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/3802067?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '3802067', 'neo_reference_id': '3802067', 'name': '(2018 FB4)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3802067', 'absolute_magnitude_h': 27.5, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.008405334, 'estimated_diameter_max': 0.0187948982}, 'meters': {'estimated_diameter_min': 8.4053340207, 'estimated_diameter_max': 18.7948982439}, 'miles': {'estimated_diameter_min': 0.0052228308, 'estimated_diameter_max': 0.0116786047}, 'feet': {'estimated_diameter_min': 27.5765560686, 'estimated_diameter_max': 61.6630539546}}, 'is_potentially_hazardous_asteroid': False, 'close_approach_data': [{'close_approach_date': '2019-05-15', 'epoch_date_close_approach': 1557903600000, 'relative_velocity': {'kilometers_per_second': '10.1302279405', 'kilometers_per_hour': '36468.8205856463', 'miles_per_hour': '22660.3068800089'}, 'miss_distance': {'astronomical': '0.3993998608', 'lunar': '155.3665466309', 'kilometers': '59749368', 'miles': '37126536'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}

{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/2350523?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '2350523', 'neo_reference_id': '2350523', 'name': '350523 (2000 EA14)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=2350523', 'absolute_magnitude_h': 21.1, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.160160338, 'estimated_diameter_max': 0.358129403}, 'meters': {'estimated_diameter_min': 160.1603379786, 'estimated_diameter_max': 358.1294030194}, 'miles': {'estimated_diameter_min': 0.0995189894, 'estimated_diameter_max': 0.2225312253}, 'feet': {'estimated_diameter_min': 525.4604432536, 'estimated_diameter_max': 1174.9652706022}}, 'is_potentially_hazardous_asteroid': True, 'close_approach_data': [{'close_approach_date': '2019-05-15', 'epoch_date_close_approach': 1557903600000, 'relative_velocity': {'kilometers_per_second': '6.6549115303', 'kilometers_per_hour': '23957.6815089786', 'miles_per_hour': '14886.3716020651'}, 'miss_distance': {'astronomical': '0.3338875592', 'lunar': '129.8822631836', 'kilometers': '49948868', 'miles': '31036786'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}

{'links': {'self': 'https://api.nasa.gov/neo/rest/v1/neo/3841756?api_key=eUzWaFD1VZsYUz7H2UzjoJ34lwIBg7eE9cfx2Lmf'}, 'id': '3841756', 'neo_reference_id': '3841756', 'name': '(2019 JN2)', 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3841756', 'absolute_magnitude_h': 25.647, 'estimated_diameter': {'kilometers': {'estimated_diameter_min': 0.0197312671, 'estimated_diameter_max': 0.0441204546}, 'meters': {'estimated_diameter_min': 19.731267145, 'estimated_diameter_max': 44.1204546185}, 'miles': {'estimated_diameter_min': 0.0122604372, 'estimated_diameter_max': 0.027415171}, 'feet': {'estimated_diameter_min': 64.7351305001, 'estimated_diameter_max': 144.7521523306}}, 'is_potentially_hazardous_asteroid': False, 'close_approach_data': [{'close_approach_date': '2019-05-15', 'epoch_date_close_approach': 1557903600000, 'relative_velocity': {'kilometers_per_second': '6.7734069663', 'kilometers_per_hour': '24384.2650785492', 'miles_per_hour': '15151.4340428352'}, 'miss_distance': {'astronomical': '0.0180892139', 'lunar': '7.0367045403', 'kilometers': '2706108', 'miles': '1681497.5'}, 'orbiting_body': 'Earth'}], 'is_sentry_object': False}
'''
    for x in rock_data['near_earth_objects']:
        for y in rock_data['near_earth_objects'][x]:
            if y['is_potentially_hazardous_asteroid'] == True:
                print(y['name'], y['is_potentially_hazardous_asteroid'], y['close_approach_data'][0]['close_approach_date'])
                print(y,'\n')

    #for day in rock_data:
        #print(day['absolute_magnitude_h'])
        #input('-- Press Enter to Continue --')


# Dump initial data to screen
#pprint.pprint(asteroids.json())

main()
