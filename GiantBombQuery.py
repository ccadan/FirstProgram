import requests
import simplejson as json

# Define Giant Bomb API Key
apikey = '[Your_Key]'

# Giant Bomb Search URL
url = "https://www.giantbomb.com/api/search/?api_key=%s" % apikey

# Defining parameters of search, limiting to character pages
params = {
    'format': "json",
    'query': "[Character_To_Search]",
    'resources': "character"
}

# Giant Bomb API requires User-Agent defined in requests
# this text can be anything but I supplied my Giant Bomb
# user name.
headers = {
    'User-Agent': 'Atomicfox Test Connection'
}

# Define the request URL based on parameters and headers
r = requests.get(url, params=params, headers=headers)

# Define dictionary based on json load of request
resp_dict = json.loads(r.text)

# Define parameters to loop through character entries
run = True
current = 0
char_id = 0

# Running loop but limiting to the first result.
# retrieve the detail url for the given character
while run:
    if current == 10:
        run = False
    else:
        for item in resp_dict.get('results'):
            if current < 1:
                char_url = resp_dict['results'][current]['api_detail_url']
            current += 1

# Accessing the character URL with defined API key
detail_url = char_url + "?api_key=%s" % apikey

# Defining parameters of search, limiting to francises pages
params_det = {'format': "json",
              'field_list': "franchises"
              }

# Define the character request URL based on parameters and headers
char = requests.get(detail_url, params=params_det, headers=headers)

# Define character dictionary based on json load of request
char_dict = json.loads(char.text)

# Define parameters to loop through character entries
run2 = True
current2 = 0
char_id2 = 0

# Create games.csv file and write header line
f = open("./games.csv", "w+")
f.write("Franchise_Name, Mario_In_Title" + "\n")

# Loop through the franchises for the given character and write the
# title back to games.csv. Indicate whether 'Mario' appears within
# the title of the game.
while run2:
    if current2 > 1000:
        run2 = False
    else:
        for items in char_dict.get('results'):
            if current2 < 1000:
                game_name = (char_dict['results']['franchises'][current2]['name'])
                print(game_name)
                if 'maro' in game_name:
                    f.write(game_name + ", Yes" + "\n")
                else:
                    f.write(game_name + ", No" + "\n")
            current2 = current2 + 1
