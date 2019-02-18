# Youtube CLI
Upoad videos from a CLI. Multiplatform, easy to use, robust programming.o

## Example:

    $ upload.py -t "My Awesome Video" \
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
violate the Goole Developer TOS to include it here. Even if I created a
pre-compiled blob to use with the code, the usage would be known due to the
open source nature. I would have to provide a fully compiled binary version
with obfuscated keys. Not something I'm wanting to do.


## Setting up the API keys.
Once you have a `client_id` and `client_secret` you can  download the JSON from
google saving it as `client_secret.json` in the same directory as the code and
it will be loaded automatically during initialization if you use the example
script. If you want to modify the code you can add the `client_id` and
`client_secret` directly in the code by setting the `GoogleAPIKey` object's
`client_id` and `client_secret` atributtes.


## Script Usage for Uploading
`upload.py` can upload videos to Youtube. It is a fairly simple file because all
of the real functionality is in all the supporting files. You can set video
information either over parameters or JSON. You can run `./upload.py -h` to see the
parameters you can pass. Everything accepts qouted strings except category.
That is set with integer numbers(look in `videodata.py` for what numbers are
used). Tags are also able to be set with multiple arguments.

To supply all the video data that is accepted by loading a JSON file
as well, load it by using the `-l` parameter. A VideoData object will be filled
in from that.

You can use both a JSON and parameters. The JSON is loaded first and any passed
parameters will overwrite the loaded JSON data.

## Code Usage
The code is based around using VideoData objects. They represent all the metadata
for the video file. `upload.py` is an example of how metadata can be loaded in.
The video data object also gets the filepath of the video to upload and the
thumbnail.

Passing a VideoData object to the a created Youtube Data API upload function
like `YTData.video_upload(video)` is all that is needed to upload.



