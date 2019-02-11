
# python
import http.client
import httplib2
import os
import random
import sys
import time
import webbrowser
import threading

from apiclient.errors import HttpError

class ReumableUpload():

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
        self.name = video.title
        self.resumable_upload(insert_request)


    # This method implements an exponential backoff strategy to resume a
    # failed upload
    def resumable_upload(self,insert_request):
        response = None
        error = None
        retry = 0
        self.start_time = time.time()

        # Upload file until response is received
        while response is None:
            try:
                # Upload file chunk
                status, response = insert_request.next_chunk()
                # Use status for progress
                if status:
                    # MediaFileUpload chunksize determines the frequency of this
                    self.print_progress("video" , status.progress())
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
                    return

                # Wait semi-random time before retrying upload
                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                time.sleep(sleep_seconds)

        # Check for successful upload
        if 'id' in response:
            self.print_progress("video" , 1)
            video.video_id=response['id']
            return response['id']
        else:
            print()
            print("The upload failed with an unexpected response: %s" % response)
            print()

            return


    def print_progress(self,name, done):
        width = os.get_terminal_size().columns
        start = "Uploading: " + self.name + " ["
        end = "] 100% 00:00:00 "
        fluff = len(start) + len(end)

        bar = round(done*(width-fluff))
        space = width-fluff-bar
        print("\r" + start, end='', flush=True)
        for j in range(bar):
            print("=", end='', flush=True)
        for j in range(space):
            print(" ", end='', flush=True)
        print("] ", end='', flush=True)
        print(round(done*100), end='', flush=True)
        dur=time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start_time))
        print("% "+ dur, end='', flush=True)
        if done == 1:
            print("\n")

