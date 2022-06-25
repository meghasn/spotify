#BQBh3FASeYmdnlJIadc77UfTgHUjX2ZefrHoUTp1Cb2qlX2SwfCUqDXOqcD1wG2tUC2YClcCLPeSjuurGZYhAgzoxc3IFuIxdHB55jot9ds0p4Agt6TerhCZr2_8z7XqAvl9TBtsiCcs9cogIZBMkqfW9QRkOTHXSfVYhieja2fg3WZJoAf2iepy6TwZkQuZxeNbtd4

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import requests
import ast
from typing import List
from os import listdir
token='BQDd0PXOkRvqGrgZ6H6YgSxsfLwWfyICJzeap9zaYqSpjoMigQK0D2iaI86eMcgVlz6D2dkD5d4CZ8ILbByewwWnXf0rS5NPgwHKDKgOZYRcQF8jCOLADCNKr3_P8iUuOyFPb3IJDZ6mI5LEou26CsHDo1FUKPjpFTWKRFafMoTMUvjhNaVuqkzFocX0c3PHifjySnM'
"""
same as spotify_create_dataset
"""
def get_streamings(path: str = 'MyData') -> List[dict]:
    
    files = ['MyData/' + x for x in listdir(path)
             if x.split('.')[0][:-1] == 'StreamingHistory']
    
    all_streamings = []
    
    for file in files: 
        with open(file, 'r', encoding='UTF-8') as f:
            new_streamings = ast.literal_eval(f.read())
            all_streamings += [streaming for streaming 
                               in new_streamings]
    return all_streamings
"""
input:track name and token
output: popularity
"""

def get_id(track_name: str, token: str) -> str:

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer ' + token,
    }
    params = [('q', track_name),('type', 'track')]
    try:
        response = requests.get('https://api.spotify.com/v1/search', 
                    headers = headers, params = params, timeout = 5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        """
        first result contains
        {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1WgXqy2Dd70QQOU7Ay074N'}, 'href': 'https://api.spotify.com/v1/artists/1WgXqy2Dd70QQOU7Ay074N', 'id': '1WgXqy2Dd70QQOU7Ay074N', 'name': 'AURORA', 'type': 'artist', 'uri': 'spotify:artist:1WgXqy2Dd70QQOU7Ay074N'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GW', 'GY', 'HK', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NL', 'NP', 'NR', 'OM', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZM', 'ZW'], 'external_urls': {'spotify': 'https://open.spotify.com/album/6YMSXPIHkA2jPIlFHuejXW'}, 'href': 'https://api.spotify.com/v1/albums/6YMSXPIHkA2jPIlFHuejXW', 'id': '6YMSXPIHkA2jPIlFHuejXW', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273c379325088c2845fe85cd70a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02c379325088c2845fe85cd70a', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851c379325088c2845fe85cd70a', 'width': 64}], 'name': 'All My Demons Greeting Me As A Friend (Deluxe)', 'release_date': '2016-03-11', 'release_date_precision': 'day', 'total_tracks': 17, 'type': 'album', 'uri': 'spotify:album:6YMSXPIHkA2jPIlFHuejXW'}
        from that take whatever features you can
        """
        pop=first_result['popularity']
        art = first_result['album']['artists'][0]['name']
        return pop
    except:
        return None

streamings = get_streamings()
print(streamings)
# print(streamings)
unique_tracks = list(set([streaming['trackName'] 
                for streaming in streamings]))
print(unique_tracks)

all_features = {}
for track in unique_tracks:
    popularity = get_id(track, token)
    all_features[track]=popularity
    print("x")
diction={}
diction['names']=[]
diction['popularity']=[]
for i in all_features.keys():
    diction['names'].append(i)
    diction['popularity'].append(all_features[i])

 """
 after modifying the dictionary into the neccessary format download it
 """   

df = pd.DataFrame.from_dict(diction)
df.to_csv('popularity.csv')


   
