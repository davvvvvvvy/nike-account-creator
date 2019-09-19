import os
from sys import platform as p_os

BASE_DIR = os.path.dirname(__file__)

class AccountsSettings:

    specific_accounts = "accounts.txt"
    accounts_location = os.path.join(BASE_DIR, specific_accounts)

    if not os.path.exists(accounts_location):
        proxies_location = os.path.join(BASE_DIR, 'accounts.txt')
