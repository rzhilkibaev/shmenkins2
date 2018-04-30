import requests
import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini")
_push_notification_url = str(cfg["default"]["push_notification_url"])


def test_push_notification_accepted():
    response = requests.post(_push_notification_url, json={"foo": "bar"})
    assert response.status_code == 201
