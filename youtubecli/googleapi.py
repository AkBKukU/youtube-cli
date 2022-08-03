#!/usr/bin/python3

# python
import http.client
import httplib2
import os
import random
import sys
import time
import webbrowser
import threading
import pprint

# google
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


class GoogleAPIBase():
    """Google OAuth2 login authentication

    Manages login information for authenticating access to the Google API.
    Uses a json token and requires an API key (GoogleAPIKey object usable)
    """

    storage_file = "./token.json"

    client_id = None
    client_secret = None
    api_name = None
    api_version = None

    service = None

    credentials = None
    scopes = []

    def __init__(self,apikey=None):
        """Set client_id and client_secret from a GoogleAPIKey object"""
        if apikey is not None:
            self.set_client(apikey)
            
            
    def add_args(parser):
        """Add options for Oauth token storage using parameters with argparse"""
        parser.add_argument('--token', '-k', action="store", help='Oauth login token location')
        
        return parser
        
    def parse_args(args):
        """Read options form parsearg to fill in API object attributtes"""
        
        if args.token is not None:
            GoogleAPIBase.storage_file = args.token

    def set_client(self, apikey):
        """Set client_id and client_secret from a GoogleAPIKey object"""
        GoogleAPIBase.client_id = apikey.client_id
        GoogleAPIBase.client_secret = apikey.client_secret

    def set_api(self, name, version):
        """The name of the api you will be using and the version targeted"""
        self.api_name = name
        self.api_version = version

    def set_storage(self, storage):
        """Change token file path for storing authentication"""
        GoogleAPIBase.storage_file = storage

    def add_scope(self, scope):
        """Add a scope to to the API connection

        Scopes are "technically" supposed to be added as needed to make the
        application seem less needy up front. Due to the nature of CLI and
        the authentication beaing web browser based this is extremely
        inconvienent. For CLI usage, I would just added all the scope you'll use
        and get all of them out of the way from the start.
        """
        GoogleAPIBase.scopes.append(scope)
        GoogleAPIBase.credentials = None

    def build_scope(self):
        """Create string of scopes for the API call"""
        scope = ""
        for s in GoogleAPIBase.scopes:
            scope += s + " "
        return scope

    def login(self):
        """Authenticate login credentials and store them"""

        # Build flow for API authentication (delcares using web authentication)
        flow = OAuth2WebServerFlow(
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.build_scope(),
            redirect_uri="http://localhost"
        )

        # Get user authentication storage
        storage = Storage(GoogleAPIBase.storage_file)
        GoogleAPIBase.credentials = storage.get()

        # Authenticate user credentials (launches web authentication)
        if GoogleAPIBase.credentials is None or \
                GoogleAPIBase.credentials.invalid:
            flags = argparser.parse_args(args=[])
            GoogleAPIBase.credentials = run_flow(flow, storage, flags)

    def get_service(self):
        """Create an authenticated service. Logins in if needed"""
        if GoogleAPIBase.credentials is None:
            self.login()
        return build(
            self.api_name, self.api_version,
            http=GoogleAPIBase.credentials.authorize(httplib2.Http()))

    def connect(self):
        """Connect to API and get a service object"""
        self.service = self.get_service()

