This is a test of pulling data using GiantBomb API.
Currently this is limited to pulling a list of franchises that a given character appears in and writes the results to a csv.

As this is an early test the API key and character name you're searching far are hardcoded. Please make sure you replace the values below.

[Your_Key} = Your Giant Bomb API Key

apikey = '[Your_Key]'

[Character_To_Search} = Name of character you're searching for. e.g. Mario, Sonic, Blanka.

params = {
    'format': "json",
    'query': "[Character_To_Search]",
    'resources': "character"
}
