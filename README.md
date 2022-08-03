# Youtube CLI
Upoad videos from a CLI. Multiplatform, easy to use, robust programming.

## Example:

    $ yt.py -t "My Awesome Video" \
    -d "My new video has a description! \
    You can see more lines of the description here!" \
    -p unlisted \
    -f videofile.mov


## What can this do?
Upload videos and thumbnails with metadata


## Installation and Getting API keys
You will need [python 3](https://www.python.org/downloads/), the [google api](https://developers.google.com/api-client-library/python/start/installation),
and the [oauth2client](https://oauth2client.readthedocs.io/en/latest/)
installed. (A pointer, you'll probably want to use `pip3` instead of `pip` to
install). You will also need to get a [Google API key](https://support.google.com/googleapi/answer/6158862)
to access the Youtube API servers.

The code is written in python and is compatible with Windows, Mac, and Linux.


## Why do I have to get an API key, you are the software developer?
You are not allowed to distribute API keys in a reusable method. I would have to
violate the Google Developer TOS to include it here. Even if I created a
pre-compiled blob to use with the code, the usage would be known due to the
open source nature. I would have to provide a fully compiled binary version
with obfuscated keys. Not something I'm wanting to do.


## Setting up the API keys.
Once you have a `client_id` and `client_secret` you can  download the JSON from
google saving it as `client_secret.json` in the same directory as the code and
it will be loaded automatically during initialization if you use the example
script. You can also specify the location of your API key with the `--client`/`-s` 
parameter and place it anywhere.

## Login Management
After logging in an Oauth token file is generated in the same directory if a path
is not specified using using `--token`/`-k`. This is the stored login file that
is used to reauthenticate without going through the web login again. You can
store and swap different tokens to upload to different Youtube channels, evem
brand managed accounts. The token can be transferred to another system to make
authenticating headless systems easier.

## Script Usage for Uploading
`yt.py` can upload videos to Youtube. It is a fairly simple file because all
of the real functionality is in all the supporting files. You can set video
information either over parameters or JSON. You can run `./yt.py -h` to see the
parameters you can pass. Everything accepts quoted strings except category.
That is set with integer numbers(look in `videodata.py` for what numbers are
used). Tags are also able to be set with multiple arguments.

To supply all the video data that is accepted by loading a JSON file
as well, load it by using the `-l` parameter.

You can use both a JSON and parameters. The JSON is loaded first and any passed
parameters will overwrite the loaded JSON data.

