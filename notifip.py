#!/usr/bin/env python3
#
# Ethan Seyl
#
# Check for Public IP Address Changes
# If changes are found, trigger IFTTT recipe

import logging.config
import requests
import logging
import glob
import os


def get_public_ip():
    ip = requests.get("http://ipinfo.io/ip")
    ip = ip.text
    ip = ip.rstrip()
    logging.info("[get_public_ip] Public IP: {}".format(ip))
    return ip


def ifttt_trigger():
    requests.post('https://maker.ifttt.com/trigger/{}/with/key/{}'.format(
        config['ifttt_recipe_name'], config['ifttt_api_key']))
    logging.debug("[ifttt_trigger] Recipe '{}' triggered".format(config[
        'ifttt_recipe_name']))


def read_file_name(my_ip):
    if os.path.isfile('{}.ipchk'.format(my_ip)):
        return True


def create_file(my_ip):
    open('{}.ipchk'.format(my_ip), 'w+b')


def delete_file():
    try:
        for ipchk in glob.glob('*.ipchk'):
            os.remove(ipchk)
    except Exception as e:
        logging.debug("[delete_file] {}".format(str(e)))


def main():
    my_ip = get_public_ip()
    if read_file_name(my_ip):
        logging.debug("[main] No change.")
    elif glob.glob('*.ipchk'):
        logging.info("IP Changed")
        delete_file()
        create_file(my_ip)
        ifttt_trigger()
    else:
        logging.debug("[main] File doesn't exist.")
        create_file(my_ip)
        logging.debug("[main] File created.")


if __name__ == "__main__":
    config = {}
    exec(open("config/notifip.conf").read(), config)
    logging.config.fileConfig("config/logging.conf")
    main()
