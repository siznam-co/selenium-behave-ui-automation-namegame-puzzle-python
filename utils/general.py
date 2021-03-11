import random
import string
from time import sleep

import requests
import configparser
import os
from py.path import local
from utils.logger import log

project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(project_path)


def get_dict_attr(obj, attr):
    for obj in [obj] + obj.__class__.mro():
        if attr in obj.__dict__:
            return obj.__dict__[attr]
    raise AttributeError


def verify_links(name, link_list):
    for url in link_list:
        res = requests.get(url)
        print(f'{name}:The status code for this link:  {url} is  {res.status_code}')
        assert res.status_code == 200, f'Something wrong with {url}'


def get_link_list(elements):
    link_list = []
    for link in elements:
        url = link.get_attribute('href')
        link_list.append(url)
    return link_list


def get_random_email():
    """
    Generating an email with fixed prefix and suffix.
    then returning the email
    """
    email_prefix = 'zingtest'
    string_ = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
    email = email_prefix + string_ + '@zing.com'
    log.info(f"Generated Email address: {email}")
    return email


def get_username_password(browser):
    pass
    # TODO


def get_config():
    config_file_Path = os.path.join(project_path, "config.ini")
    config_parser = configparser.RawConfigParser()
    config_parser.read(config_file_Path)
    return config_parser


config = get_config()


def get_setting(parent, key):
    return config.get(parent, key)


def get_browser_name():
    return get_setting("BROWSER", "browser")
