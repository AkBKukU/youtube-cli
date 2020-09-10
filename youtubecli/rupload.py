
# python
import http.client
import httplib2
import os
import random
import sys
import time
import webbrowser
import threading
import json

from apiclient.errors import HttpError
from youtubecli.util import Util

class ReumableUpload():
    """Safe uploading of files

    Upload files with tolerance of poor network connections. Also prints upload
    progress and time.

    Derived from: https://developers.google.com/youtube/v3/guides/uploading_a_video
    """

    # Explicitly tell the underlying HTTP transport library not to retry, since
    # we are handling retry logic ourselves.
    httplib2.RETRIES = 1

    # Maximum number of times to retry before giving up.
    MAX_RETRIES = 10

    # Always retry when these exceptions are raised.
    RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError,
        http.client.NotConnected, http.client.IncompleteRead,
        http.client.ImproperConnectionState, http.client.CannotSendRequest,
        http.client.CannotSendHeader, http.client.ResponseNotReady,
        http.client.BadStatusLine
    )

    # Always retry when an apiclient.errors.HttpError with one of these status
    # codes is raised.
    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

    def upload_video(self,video,insert_request):
        """Begin upload of video and update returned ID if succesful"""
        self.name = video.title
        response = self.resumable_upload(insert_request, "video")

        # Check for successful upload
        if 'id' in response:
            video.id=response['id']
            return response
        else:
            print()
            print("The upload failed with an unexpected response: %s" % response)
            print()

            return

    def upload_video_test(self,video):
        """Fake an upload for testing purposes. Returns example data from JSON"""
        with open('test/response.json', 'r') as f:
            response = json.load(f)

            # Check for successful upload
            if 'id' in response:
                video.id=response['id']
                return video
            else:
                print()
                print("The upload failed with an unexpected response: %s" % response)
                print()

                return



    # This method implements an exponential backoff strategy to resume a
    # failed upload
    def resumable_upload(self,insert_request, name):
        """Chunk based upload with connection problem tolerance

        Derived from: https://developers.google.com/youtube/v3/guides/uploading_a_video
        """

        response = None
        error = None
        retry = 0
        self.start_time = time.time()
        util = Util()

        # Upload file until response is received
        while response is None:
            try:
                # Upload file chunk
                status, response = insert_request.next_chunk()
                # Use status for progress
                if status:
                    # MediaFileUpload chunksize determines the frequency of this
                    util.progress_bar("Uploading: " + name ,self.start_time, status.progress())
            except HttpError as e:
                if e.resp.status in self.RETRIABLE_STATUS_CODES:
                    error = "A retriable HTTP error %d occurred:\n%s" \
                        % (e.resp.status,e.content)
                else:
                    raise
            except self.RETRIABLE_EXCEPTIONS as e:
                error = "A retriable error occurred: %s" % e

            # Handle errors
            if error is not None:
                print()
                print(error)
                print()
                error = None
                retry += 1
                if retry > MAX_RETRIES:
                    print()
                    print("Out of retries")
                    print()
                    return response

                # Wait semi-random time before retrying upload
                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                time.sleep(sleep_seconds)

            # Record test response
            #with open('./response.json', 'w') as f:
            #    json.dump(response, f, sort_keys=True)

        util.progress_bar("Uploading: " + name ,self.start_time, 1)
        return response


