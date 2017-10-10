import requests
import simplejson as json

apikey = '[Your_Key]'

url = "https://www.giantbomb.com/api/search/?api_key=%s" % apikey

params = { 'format': "json",
            'query': "mario",
            'resources': "character"
           }

headers = {
    'User-Agent': 'Atomicfox Test Connection'
}

r = requests.get(url, params=params, headers=headers)

#print("Status:", r.status_code)

resp_dict = json.loads(r.text)
#print (resp_dict.get('results')[0])
#resp_dict['id']

run = True
current = 0
char_id = 0

while run:
    if current == 10:
        run = False
    else:
        #print(current)
        for item in resp_dict.get('results'):
            if current < 1:
                print(resp_dict['results'][current]['name'],resp_dict['results'][current]['id'])
                char_url = resp_dict['results'][current]['api_detail_url']
                print (char_url)
            current += 1

detail_url = char_url + "?api_key=%s" % apikey

params_det = { 'format': "json",
               'field_list': "franchises"
           }

char = requests.get(detail_url, params = params_det, headers=headers)

char_dict = json.loads(char.text)

run2 = True
current2 = 0
char_id2 = 0

f = open("./games.csv", "w+")

while run2:
    if current2 > 1000:
        run2 = False
    else:

        for item in char_dict.get('results'):
            if current2 < 1000:
                game_name = (char_dict['results']['franchises'][current2]['name'])
                print(game_name)
                #games = str(game_name + '\n')
                f.write(game_name + "\n" )
            current2 = current2+1

