from json import loads
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError, ContentTooShortError

class Net:
    def __init__(self):
        # Initialize API base URL and token as None
        self._api = None
        self._token = None

    def _request(self, method, url, headers={}, data=None, timeout=15):
        # If a token is set, add Authorization header
        if self._token:
            headers.update({
                'Authorization': "Bearer: " + self._token
            })
        # Prepare the HTTP request with method, URL, headers, and data
        req = Request(
            method = method,
            url = url,
            headers = headers,
            data = data
        )
        # Initialize the reply dictionary to store response info
        reply = {
            'status': 0,
            'headers': {},
            'body': {},
            'log': None
        }
        try:
            # Attempt to open the URL and read the response
            response = urlopen(req, timeout=timeout)
            reply.update({
                'status': response.status,
                'headers': dict(response.headers.items())
            })
            try:
                # Try to parse the response body as JSON
                reply['body'] = loads(response.read())
            except Exception as error:
                # If parsing fails, log the error
                reply['log'] = error
        except URLError as error:
            # Handle URL errors (e.g., network issues)
            reply['log'] = error.reason
        except ContentTooShortError as error:
            # Handle incomplete download errors
            reply['log'] = error
        except HTTPError as error:
            # Handle HTTP errors (e.g., 404, 500)
            reply.update({
                'status': response.status,
                'headers': dict(response.headers.items()),
                'log': error.reason
            })
        return reply

    def get(self, url):
        # Make a GET request to the specified URL
        return self._request(
            method = "GET",
            url = url
        )