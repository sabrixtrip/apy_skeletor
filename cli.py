"""
 Apy - Cli

 This module provides a simple command-line interface (CLI) helper class
 for interacting with APIs, handling user input, displaying messages,
 and parsing command-line arguments.
"""
from json import dumps, loads
from time import sleep
from argparse import ArgumentParser
from getpass import getuser, getpass

class Cli:
    def __init__(self):
        # Initialize counters for errors and successful operations
        self.error = 0
        self.ok = 0
        # Set up argument parser for CLI options
        parser = ArgumentParser(
            description = 'A simple way to start talking API.'
        )
        parser.add_argument(
            '-u', '--user',
            type = str,
            default = getuser(),
            help = 'User to login. (default: %(default)s)'
        )
        parser.add_argument(
            '-p', '--password',
            type = str,
            default = None,
            help = 'Password or secret to login.'
        )
        parser.add_argument(
            '-t', '--token',
            type = str,
            default = None,
            help = 'Token to bear.'
        )
        # Parse command-line arguments and store them
        self.args = parser.parse_args()

    def ask(self, msg):
        # Prompt the user for input with a message
        print('🤖💬❔ \033[37m{0}\033[0m'.format(msg))
        return input()

    def secret(self, msg):
        # Prompt the user for sensitive input (hidden)
        print('🤖💬❓ \033[37m{0}\033[0m (not shown)'.format(msg))
        return getpass("")

    def info(self, msg):
        # Display an informational message
        print('🤖💭💡 \033[36m{0}\033[0m'.format(msg))

    def warning(self, msg):
        # Display a warning message
        print('🤖🗯❕ \033[1;33m{0}\033[0m'.format(msg))

    def critical(self, msg):
        # Display a critical error message and exit
        print('🤖🗯❗ \033[1;31m{0}\033[0m'.format(msg))
        exit(1)

    def section(self, msg):
        # Display a section header
        print('📂 \033[1;4;37m{0}\033[0m'.format(msg))

    def item(self, msg):
        # Display an item in a list or menu
        print('📄 \033[37m{0}\033[0m'.format(msg))

    def content(self, json):
        # Pretty-print JSON content
        print('\033[37m{0}\033[0m'.format(dumps(json, indent=2)))

    def verify(self, msg, value, expect):
        # Verify if a value matches the expected value and display result
        if value == expect:
            print('💚 \033[32m{0}\033[0m'.format(msg))
            self.ok += 1
            return True
        else:
            print('💔 \033[31m{0}\033[0m'.format(msg))
            self.error += 1
            return False

    def wait(self, seconds):
        # Display a waiting message and pause execution
        print('⏳ \033[33mWaiting {0} seconds...\033[0m'.format(seconds))
        sleep(seconds)

    def load(self, path):
        # Load and parse a JSON file from the given path
        try:
            fhand = open(path, 'r')
        except Exception as error:
            self.warning(error)
            return None
        content = fhand.read()
        fhand.close()
        data = {}
        try:
            data = loads(content)
        except Exception as error:
            self.warning(error)
            return None
        return data

class UserAPI:
    def __init__(self, api_base_url, token=None):
        # Initialize Net helper and set API base URL and optional token
        self.net = Net()
        self.net._api = api_base_url
        self.net._token = token

    def get_user(self, user_id):
        # Retrieve a single user by ID using GET
        url = f"{self.net._api}/users/{user_id}"
        return self.net.get(url)

    def list_users(self):
        # Retrieve all users using GET
        url = f"{self.net._api}/users"
        return self.net.get(url)

    def create_user(self, user_data):
        # Create a new user using POST
        url = f"{self.net._api}/users"
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(user_data).encode('utf-8')
        return self.net._request("POST", url, headers, data)

    def update_user(self, user_id, user_data):
        # Update an existing user by ID using PUT
        url = f"{self.net._api}/users/{user_id}"
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(user_data).encode('utf-8')
        return self.net._request("PUT", url, headers, data)

    def delete_user(self, user_id):
        # Delete a user by ID using DELETE
        url = f"{self.net._api}/users/{user_id}"
        return self.net._request("DELETE", url)