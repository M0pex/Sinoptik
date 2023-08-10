# config.py


import configparser

read_config = configparser.ConfigParser()
read_config.read('settings.ini')


bot_token = read_config['settings']['token'].strip()
PATH_DATABASE = 'data/database.db'

for section in read_config.sections():
    print(f"Section: {section}")
    for key, value in read_config.items(section):
        print(f"  {key} = {value}")







