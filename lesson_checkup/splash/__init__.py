import configparser

config = configparser.ConfigParser()
config.read('config.ini')

container_name = config['Docker']['container_name']
port = config['Docker']['port']

from .Container import Container as Splash
