import os
from sys import platform as p_os

BASE_DIR = os.path.dirname(__file__)

class ProxySettings:

    specific_proxies = "proxies.txt"
    proxies_location = os.path.join(BASE_DIR, specific_proxies)

    if not os.path.exists(proxies_location):
        proxies_location = os.path.join(BASE_DIR, 'proxies.txt')
