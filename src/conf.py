import configparser

config = configparser.ConfigParser()

def create_starter_config():
    config['DEFAULTS'] = {
        'root_folder_name': '',
        'machine_os': '',
        'machine_username': '',
        'debuger_mode': False
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
        configfile.close()