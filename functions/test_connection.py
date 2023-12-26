# --- test_connection.py --- #
# Test whether we can connect to the given URL. We use this to check if we can connect to the ESP32's web server

# We use urllib to test the connection.
from urllib import request, error


# testConnection: test the connection to the given URL.
def testConnection(URL):
    try:
        request.urlopen(URL, timeout=2)
        # Try making timeout longer if you think connection should be working.
        return True
    except error.URLError:
        return False
