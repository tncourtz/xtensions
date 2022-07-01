# Google Events

This is a set of scripts to use against google drive. The primary purpose was/is to test googl drive events.
There are now also a few other scripts that just interact with the google drive.

## Authentication

Getting auth going the first time can be hard. You need to:

1. go to `https://console.cloud.google.com`
2. Create a project
3. Enable API access on the project
4. Add Credentials under APIs & Services (add Oauth 2.0 Client IDs)
5. Modify/update the redirect URI to make sure it's pointing to `receivetoken.py`
6. Download the OAuth 2.0 Client IDs (the JSON file) and store it as `ClientDetailsApp.json`
7. Then, use `getauthcode.sh` to generate a URL to open in the browser. The oauth flow will end in `receivetoken.py` which /writes/ to `accesstoken.json`. The other scripts make use of `accesstoken.json`

You might encounter some small issues. Best is to use `getfiles.sh` to see if the API calls are really working.

## Scripts

Quick description of what is what

- `getauthcode.sh` generates a oauth-url. See Authentication above.
- `getfiles.sh` simple script to query for the file objects.
- `DoDriveThing.py` python code that helps with creating/listing/deleting google shared drives. This is useful for testing > 100 drives.
- `setwatch.sh` sets a 'watch' on a google drive resource. This makes sure google tells us something is changes, after which you can use `getchanges.sh`
- `getchanges.sh` gets changes on your google drive

`setwatch.sh` and `getchanges.sh` will require some modifications.
