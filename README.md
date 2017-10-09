﻿This is a test of pulling data using GiantBomb API.
Currently this is limited to pulling a list of franchises that a given character appears in and writes the results to a csv.

As this is an early test the API key and character name you're searching for are hardcoded.

Please make sure you edit GiantBombQuery.py and replace the values below.

    apikey = '[Your_Key]'
        # [Your_Key} = Your Giant Bomb API Key

    params = {
        'format': "json",
        'query': "[Character_To_Search]",
        'resources': "character"
    }
        #[Character_To_Search} = Name of character you're searching for. e.g. Mario, Sonic, Blanka.

Once API key has been entered and a character name supplied you can run the script directly from Python.
