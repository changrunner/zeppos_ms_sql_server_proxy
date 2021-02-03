import requests


class Heartbeat:
    @staticmethod
    def ping():
        response = requests.get('http://127.0.0.1:5800/heartbeat/')
        if response.status_code == 200 and \
            response.content.decode().replace('\n', '').replace(' ', '') == '{"alive":"true"}':
            return "pong"
        else:
            return None