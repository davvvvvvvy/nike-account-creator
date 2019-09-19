from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
import string
import random
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tqdm import tqdm
import threading

from bin.settings import Settings
from bin.proxies_settings import ProxySettings
from bin.verifysms import VerifySMS
from bin.versms import VerSMS
from bin.accounts_settings import AccountsSettings

def random_mail_ld():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8)) + '@gmail.com'

def random_mail_letters():
    return ''.join(random.choice(string.ascii_letters) for i in range(4))

def random_password():
    return ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_uppercase + string.digits) for i in range(12))

def write_file(usrname, psword):
    f = open("accounts.txt", "a")
    f.write("{}:{}:".format(usrname, psword))
    f.close()

proxiess = [proxy.rstrip('\n') for proxy in open(ProxySettings.proxies_location)]

chromedriver_location = Settings.chromedriver_location
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"')
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument('--dns-prefetch-disable')
chrome_options.add_argument('--lang=en-US')
#chrome_options.add_argument('-headless')

def create_nike(n, location, PROXY=False):
    n = n-1
    r_mail = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8)) + '@gmail.com'
    r_fn = ''.join(random.choice(string.ascii_letters) for i in range(4))
    r_pas = ''.join(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase+ string.digits) for i in range(12))
    r_ln = ''.join(random.choice(string.ascii_letters) for i in range(4))

    if PROXY==True:
        chrome_options.add_argument('--proxy-server=http://%s' % proxiess[n])
        print("Connected to proxy -> {}".format(proxiess[n]))

    else:
        print("Using without proxy.")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver_location)

    if PROXY==True:
        print("Connected to proxy -> {}".format(proxiess[n]))

    print("Starting new session...")

    if location=='CN2':

        os.system("cls")
        username = input("Input username for smscin... ")
        os.system("cls")
        token = input("Input token for smscin... ")
        os.system("cls")
        pid = input("Input pid for smscin... ")

        driver.get('https://www.nike.com/cn/zh_cn/s/register')

        try:
            time.sleep(4)
            try:
                flag = driver.find_element_by_xpath("//div[@class='modal-close-glyph nsg-glyph--x']")
                flag.click()
            except:
                print("Something went wrong:/")
            input_num = driver.find_element_by_xpath("//input[@type='tel']")
            input_num.click()
            input_num.clear()
            input.send_keys(VerSMS.getmobile_cn(token, username, pid))
            print("Number -> {}".format(VeySMS.getmobile_cn(token, username, pid)))

            time.sleep(2)

            send_code = driver.find_element_by_xpath("//input[@value='Send Code']")
            send_code.click()

            time.sleep(15)

            code = driver.find_element_by_xpath("//input[@value='number']")
            code.click()
            code.clear()
            code.send_keys(VerSMS.getsms_cn(token, username, pid))
            print("Code -> {}".format(VerSMS.getsms_cn(token, username, pid)))

            time.sleep(1)

        except Exception as e:
            print(e)

    else:

        try:
            if location=='US':
                driver.get('https://www.nike.com/us/en_us/s/register')
            if location=='UK':
                driver.get('https://www.nike.com/gb/en_gb/s/register')


        except Exception as e:

            print(e)

        time.sleep(5)

        '''if driver.find_element_by_class_name('exp-geodetect-notifier__title nsg-font-family--platform').is_displayed():
            flag = driver.find_element_by_class_name('exp-geodetect-notifier__flag')
            flag.click()'''

        try:
            flag = driver.find_element_by_xpath("//div[@class='modal-close-glyph nsg-glyph--x']")
            flag.click()
        except:
            print("Something went wrong:/")

        time.sleep(4)

        try:

            try:
                em = driver.find_element_by_name('emailAddress')
                em.click()
            except:
                print("Couldn't click!")
            time.sleep(1)
            em.clear()

            em.send_keys(r_mail)

            time.sleep(2)

            try:
                pas = driver.find_element_by_name('password')
                pas.click()
            except:
                print("Couldn't click!")
            time.sleep(1)
            pas.clear()
            try:
                pas.send_keys(r_pas)
            except:
                print("Couldn't send keys!")

            time.sleep(2)

            try:
                fn = driver.find_element_by_name('firstName')
                fn.click()
            except:
                print("Couldn't click!")
            time.sleep(1)
            fn.clear()
            try:

                fn.send_keys(r_fn)
            except:
                print("Couldn't send keys!")

            time.sleep(2)

            try:
                ln = driver.find_element_by_name('lastName')
                ln.click()
            except:
                print("Couldn't click!")
            time.sleep(1)
            ln.clear()
            try:

                ln.send_keys(r_ln)
            except:
                print("Couldn't send keys!")

            time.sleep(2)

            try:
                date_mm = Select(driver.find_element_by_id('nike-unite-date-id-mm'))
                for index in range(len(date_mm.options)):
                    date_mm = Select(driver.find_element_by_id('nike-unite-date-id-mm'))
                    date_mm.select_by_index(index)
                time.sleep(2)

                date_dd = Select(driver.find_element_by_id('nike-unite-date-id-dd'))
                for index in range(len(date_dd.options)):
                    date_dd = Select(driver.find_element_by_id('nike-unite-date-id-dd'))
                    date_dd.select_by_index(index)
                time.sleep(2)

                date_yyyy = Select(driver.find_element_by_id('nike-unite-date-id-yyyy'))
                for index in range(len(date_yyyy.options)):
                    date_yyyy = Select(driver.find_element_by_id('nike-unite-date-id-yyyy'))
                    date_yyyy.select_by_index(index)
                time.sleep(2)

            except:
                date_mm = driver.find_element_by_name('dateOfBirth')
                date_mm.clear()
                date_mm.send_keys('01.01.2000')

            try:
                genre = driver.find_element_by_xpath("//span[contains(text(), 'Male')]")
                genre.click()
            except:
                print("Couldn't click!")

            time.sleep(2)

            try:
                login_btn = driver.find_element_by_xpath("//input[@value='CREATE ACCOUNT']")
                login_btn.click()
                time.sleep(2)
                print(" >>> Account created!")
                write_file(r_mail, r_pas)
            except:
                print("Couldn't click!")

            time.sleep(1)

            driver.quit()

        except Exception as e:

            print(e)

def verify_smscin(username, token, pid):
    f = open('accounts.txt', 'r+')
    accs = []
    for line in f.readlines():
        for value in line.split(':'):
            accs.append( value )
    f.close()
    n=1
    i=0
    final = [accs[i * n:(i + 1) * n] for i in range((len(accs) + n - 1) // n )]
    for j in range(0, len(final)):
        accs_mail = final[0:len(final):2]
        accs_pass = final[1:len(final):2]
    for i in range(0, len(final)//2):
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver_location)
        print('Trying to verify...')
        time.sleep(10)
        driver.get("https://www.nike.com/cn")
        time.sleep(6)
        try:
            flag = driver.find_element_by_xpath("//div[@class='modal-close-glyph nsg-glyph--x']")
            flag.click()
        except:
            print("Something went wrong:/")
        time.sleep(7)

        try:
            log = driver.find_element_by_xpath("//button[@data-type='click_navJoinLogin']")
            log.click()
        except:
            print("Nono")

        try:
            em = driver.find_element_by_name('emailAddress')
            em.click()
        except:
            print("Couldn't click!")
        time.sleep(1)
        em.clear()

        em.send_keys(accs_mail[i])

        time.sleep(2)

        try:
            pas = driver.find_element_by_name('password')
            pas.click()
        except:
            print("Couldn't click!")
        time.sleep(1)
        pas.clear()
        try:
            pas.send_keys(accs_pass[i])
        except:
            print("Couldn't send keys!")

        time.sleep(4)
        driver.get('https://www.nike.com/member/settings')

        time.sleep(5)
        try:
            flag = driver.find_element_by_xpath("//div[@class='modal-close-glyph nsg-glyph--x']")
            flag.click()
        except:
            print("Something went wrong:/")

        try:
            time.sleep(5)
            try:
                try:
                    ver = driver.find_element_by_xpath("//button[@class='ncss-btn-secondary-dark bg-white']")
                except:
                    print("Can't find add button!")
                try:
                    ver.click()
                except:
                    print("Can't click!")

            except:
                print("Can't find button!")

            input_num = driver.find_element_by_xpath("//input[@type='tel']")
            input_num.click()
            input_num.clear()
            input.send_keys(VerSMS.getmobile_cn(token, username, pid))
            print("Number -> {}".format(VeySMS.getmobile_cn(token, username, pid)))

            time.sleep(2)

            send_code = driver.find_element_by_xpath("//input[@value='Send Code']")
            send_code.click()

            time.sleep(15)

            code = driver.find_element_by_xpath("//input[@value='number']")
            code.click()
            code.clear()
            code.send_keys(VerSMS.getsms_cn(token, username, pid))
            print("Code -> {}".format(VerSMS.getsms_cn(token, username, pid)))

            time.sleep(1)

        except Exceptions as e:
            print(e)


def verify_simsms(token, location):
    f = open('accounts.txt', 'r+')
    accs = []
    for line in f.readlines():
        for value in line.split(':'):
            accs.append( value )
    f.close()
    n=1
    i=0
    final = [accs[i * n:(i + 1) * n] for i in range((len(accs) + n - 1) // n )]
    for j in range(0, len(final)):
        accs_mail = final[0:len(final):2]
        accs_pass = final[1:len(final):2]
    for i in range(0, len(final)//2):
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver_location)
        print('Trying to verify...')
        time.sleep(10)
        if location=='US':
            driver.get('https://www.nike.com/us/en_us/s/register')
        if location=='UK':
            driver.get('https://www.nike.com/gb/en_gb/s/register')

        time.sleep(6)
        try:
            flag = driver.find_element_by_xpath("//div[@class='modal-close-glyph nsg-glyph--x']")
            flag.click()
        except:
            print("Something went wrong:/")
        time.sleep(7)

        try:
            log = driver.find_element_by_xpath("//button[@data-type='click_navJoinLogin']")
            log.click()
        except:
            print("Nono")

        try:
            em = driver.find_element_by_name('emailAddress')
            em.click()
        except:
            print("Couldn't click!")
        time.sleep(1)
        em.clear()

        em.send_keys(accs_mail[i])

        time.sleep(2)

        try:
            pas = driver.find_element_by_name('password')
            pas.click()
        except:
            print("Couldn't click!")
        time.sleep(1)
        pas.clear()
        try:
            pas.send_keys(accs_pass[i])
        except:
            print("Couldn't send keys!")

        time.sleep(4)

        driver.get('https://www.nike.com/member/settings')

        time.sleep(5)
        try:
            flag = driver.find_element_by_xpath("//div[@class='modal-close-glyph nsg-glyph--x']")
            flag.click()
        except:
            print("Something went wrong:/")
        try:
            time.sleep(5)
            try:
                try:
                    ver = driver.find_element_by_xpath("//button[@class='ncss-btn-secondary-dark bg-white']")
                except:
                    print("Can't find add button!")
                try:
                    ver.click()
                except:
                    print("Can't click!")

            except:
                print("Can't find button!")

            time.sleep(2)

            input_num = driver.find_element_by_xpath("//input[@type='tel']")
            input_num.click()
            input_num.clear()
            input.send_keys(VerifySMS.getmobile(token, location))
            print("Number -> {}".format(VerifySMS.getmobile(token, location)))

            time.sleep(2)

            send_code = driver.find_element_by_xpath("//input[@value='Send Code']")
            send_code.click()

            time.sleep(15)

            code = driver.find_element_by_xpath("//input[@value='number']")
            code.click()
            code.clear()
            code.send_keys(VerifySMS.getsms(token, location))
            print("Code -> {}".format(VerifySMS.getsms(token, location)))

            time.sleep(1)

            agree = driver.find_element_by_class_name('checkbox')
            agree.click()

            time.sleep(2)

            g = driver.find_element_by_xpath("//input[@value='number']")
            g.click()

            print("Account verified!")

        except:
            print("Can't verify!")


location = input("Choose location [UK, CN2, US]... ")
print("1.) Create accounts\n2.) Verify accounts")
c = int(input("\nChoose -> "))
if c==1:
    os.system("cls")
    col = int(input("How much accouts you want... "))
    os.system("cls")
    thread_list = []
    for i in range(col):
        t = threading.Thread(name='Starting {}'.format(i+2), target=create_nike(i, location, False))
        t.start()
        time.sleep(1)
        print(t.name)
        thread_list.append(t)

    for thread in thread_list:
        thread.join()

else:
    os.system("cls")
    print("1.) SimSMS\n2.) SMSCin")
    sms = int(input("\nChoose -> "))
    if sms==1:
        os.system("cls")
        token = input("Input SimSMS API Token... ")
        thread_list = []
        for i in range(0, 100):
            t = threading.Thread(name='Starting {}'.format(i+2), target=verify_simsms(token, location))
            t.start()
            time.sleep(1)
            print(t.name)
            thread_list.append(t)

        for thread in thread_list:
            thread.join()

    else:
        os.system("cls")
        username = input("Input username for smscin... ")
        os.system("cls")
        token = input("Input token for smscin... ")
        os.system("cls")
        pid = input("Input pid for smscin... ")
        thread_list = []
        for i in range(col):
            t = threading.Thread(name='Starting {}'.format(i+2), target=verify_smscin(username, token, pid))
            t.start()
            time.sleep(1)
            print(t.name)
            thread_list.append(t)

        for thread in thread_list:
            thread.join()

'''while col > 0:
    create_nike(col)
    print(" >>> Created {} accounts :)".format(col-(col-1)))
    col -= 1'''

time.sleep(1)
