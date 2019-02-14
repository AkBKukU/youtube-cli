# Youtube CLI
Primarily for uploading. Maybe other stuff eventually


## What can this do?
Upload videos


## Installation
You will need [python 3](https://www.python.org/downloads/) and the [google api](https://developers.google.com/api-client-library/python/start/installation)
installed. You will also need to get a [Google API key](https://support.google.com/googleapi/answer/6158862)
to access the Youtube API servers. Once you have a `client_id` and
`client_secret` to put in the `apikey-empty.py` file and add your channel id
(it's the non-custom version of your channel url link) you should be ready. Then
rename it to `apikey.py`.

The code is written in python and is compatible with Windows, Mac, and Linux.


## Usage
The code is based around using VideoData objects. They represent all the metadata
for the video file. `upload.py` is an example of how metadata can be loaded in.
The video data object also gets the filepath of the video to upload and the
thumbnail.

Passing a VideoData object to the a created Youtube Data API upload function
like `ytd.video_upload_test(video)` is all that is needed to upload.



