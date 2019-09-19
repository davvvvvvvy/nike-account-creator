import os
from sys import platform as p_os




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OS_ENV = "windows" if p_os == "win32" else "osx" if p_os == "darwin" else "linux"



class Settings:

    chromedriver_min_version = 2.36

    specific_chromedriver = "chromedriver_{}".format(OS_ENV)
    chromedriver_location = os.path.join(BASE_DIR, "assets", specific_chromedriver)

    if not os.path.exists(chromedriver_location):
        chromedriver_location = os.path.join(BASE_DIR, 'assets', 'chromedriver')
