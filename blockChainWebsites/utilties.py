from urllib.parse import urlencode


user_agents='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'

def payload_url(payload):
    return str(urlencode(payload))
