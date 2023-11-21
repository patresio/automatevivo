import csv
import json
import os
import shutil
from random import uniform
from time import sleep

import undetected_chromedriver as uc
from colorama import Fore
from decouple import config
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.transform_data import *


def config_initial_local_folder():
    return os.getcwd()


def config_download_folder():
    return os.path.join(config_initial_local_folder(), 'Downloads')


def config_initial_data():
    SITE_LINK = "https://mve.vivo.com.br/"
    USER_DATA = {
        "email": config('EMAIL'),
        "password": config('PASSWORD')
    }
    with open("utils/sitemap.json", "r") as sm:
        SITE_MAP = json.load(sm)
    return SITE_MAP, SITE_LINK, USER_DATA


def initial_drivers(browser):
    if browser == 'Firefox':
        options = FirefoxOptions()
        browser_arguments(options)
        options.set_preference(
            "plugin.disable_full_page_plugin_for_types", "application/pdf")
        options.set_preference("pdfjs.disabled", True)
        options.set_preference("pdfjs.enabledCache.state", False)
        options.set_preference("browser.download.dir",
                               config_download_folder())
        options.set_preference("browser.download.folderList", 2)
        options.set_preference(
            "browser.download.manager.showWhenStarting", False)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        driver = webdriver.Firefox(options=options, service=FirefoxService(
            GeckoDriverManager().install()))
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
            ]
        )
        return driver, wait
    elif browser == 'Chrome':
        options = uc.ChromeOptions()
        browser_arguments(options)
        prefs = {"download.default_directory": config_download_folder(),
                 "safebrowsing.enabled": "false"}
        options.add_experimental_option("prefs", prefs)
        driver = uc.Chrome(options=options, service=ChromeService(
            ChromeDriverManager().install()), use_subprocess=True)
        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
            ]
        )
        return driver, wait


def browser_arguments(options):
    arguments = ["disable-infobars", "--disable-notifications", "--no-sandbox",
                 "--disable-application-cache", "--disable-gpu", "--disable-dev-shm-usage", "--disable-extensions"]
    for argument in arguments:
        options.add_argument(argument)
    options.headless = False


def create_folder_faturas():
    name_folder_fatura = f'Faturas-{mes_txt}'
    if os.path.isdir(name_folder_fatura):
        print(Fore.RED, '\U0001F916', 'O ROBO DIZ:',
              f'Pasta do mês: {mes_data} já existe!', '\U0001F4C5', '\U0001F4C1')
        return (
            '\U0001F916',
            'O ROBO DIZ:',
            f'Pasta do mês: {mes_data} já existe!',
            '\U0001F4C5',
            '\U0001F4C1',
        )
    else:
        os.mkdir(name_folder_fatura)
        print(Fore.GREEN, '\U0001F916', 'O ROBO DIZ:',
              f'Pasta para as faturas do mês: {mes_data} foi criada com sucesso!', '\U0001F4C5', '\U0001F91D', '\U0001F4BE')
        return (
            '\U0001F916',
            'O ROBO DIZ:',
            f'Pasta para as faturas do mês: {
                mes_data} foi criada com sucesso!',
            '\U0001F4C5',
            '\U0001F91D',
            '\U0001F4BE',
        )


def create_folder_download():
    if os.path.isdir(config_download_folder()):
        print(Fore.RED, '\U0001F916', 'O ROBO DIZ:',
              'A pasta downloads já existe!', '\U0001F4C1')
        resposta = (
            '\U0001F916',
            'O ROBO DIZ:',
            'A pasta downloads já existe!',
            '\U0001F4C1',
        )
    else:
        os.mkdir(config_download_folder())
        print(Fore.GREEN, '\U0001F916', 'O ROBO DIZ:',
              'A pasta downloads foi criada com sucesso!', '\U0001F4BE')
        return (
            '\U0001F916',
            'O ROBO DIZ:',
            'A pasta downloads foi criada com sucesso!',
            '\U0001F4BE',
        )


def random_wait(inicio=5, fim=7):
    sleep(uniform(inicio, fim))


def create_csv(header, data, filename):
    with open(filename, "w", newline="") as csvfile:
        faturas = csv.writer(csvfile)
        faturas.writerow(header)
        for x in data:
            faturas.writerow(x)


def rename_arquivo(local, download, rename, phone):
    if os.path.isfile(download):
        extract_and_rename(download, rename, local, phone)
    else:
        print('\U0001F916', 'O ROBO está aguardando o arquivo, vamos esperar')
        random_wait(20, 30)
        if os.path.isfile(download):
            extract_and_rename(download, rename, local, phone)


def extract_and_rename(download, rename, local, phone):
    print(Fore.WHITE, '\U0001F916',
          f'O ROBO Verificou e achou o arquivo {download}')
    os.rename(download, rename)
    shutil.move(rename, local)
    print(Fore.GREEN,
          '\U0001F916', f'O ROBO renomeou e moveu a fatura da linha {phone} com sucesso')
