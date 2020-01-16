from os.path import join, dirname, abspath, isfile
from os import remove
import json
from time import sleep

SETTINGS_FILE = join(abspath(dirname(__file__)), 'data/settings.json')

SETTINGS = None
if isfile(SETTINGS_FILE):
    with open(SETTINGS_FILE, 'r') as f:
        SETTINGS = json.load(f)


def get_data_path():
    global SETTINGS
    if SETTINGS is None or 'data_path' not in SETTINGS:
        return join(abspath(dirname(__file__)), 'data')
    else:
        return SETTINGS['data_path']


def set_h36m_path(path):
    global SETTINGS, SETTINGS_FILE
    if SETTINGS is None:
        SETTINGS = {}
    SETTINGS['h36m_path'] = path
    if isfile(SETTINGS_FILE):
        remove(SETTINGS_FILE)
        sleep(0.5)
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(SETTINGS, f)
    print()
    print('\033[92mHuman3.6M path is set\033[0m')
    print()


def get_h36m_path():
    global SETTINGS
    if SETTINGS is None or 'h36m_path' not in SETTINGS:
        raise ValueError("Settings do not contain {h36m_path}!")
    else:
        return SETTINGS['h36m_path']


def set_data_path(path):
    global SETTINGS, SETTINGS_FILE
    if SETTINGS is None:
        SETTINGS = {}
    SETTINGS['data_path'] = path
    if isfile(SETTINGS_FILE):
        remove(SETTINGS_FILE)
        sleep(0.5)
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(SETTINGS, f)
    print()
    print('\033[92mData path is set\033[0m')
    print()


def set_password(password):
    password_file = join(abspath(dirname(__file__)), 'data/password.txt')
    if isfile(password_file):
        remove(password_file)
    sleep(0.1)
    with open(password_file, 'w') as f:
        f.write(password)
    sleep(0.1)
    print()
    print('\033[92mWrite password to ' + password_file + '\033[0m')
    print()


def reset_settings(user_warning_prompt=True):
    """
    Resets the settings to the default values
    """
    global SETTINGS, SETTINGS_FILE
    if user_warning_prompt:
        print('\n\033[1m\033[93m[mocap][Settings] WARNING! deleting settings!\033[0m')
        choice = input('This cannot be undone! Continue? [y/N]\n').lower()
        print()

        if choice != 'y':
            print('aborting... \033[92mSettings are NOT reset!\033[0m')
            print()
            return

    print('\033[93m[mocap][Settings] resetting Settings...\033[0m')
    print()

    SETTINGS = None
    if isfile(SETTINGS_FILE):
        remove(SETTINGS_FILE)
        sleep(0.5)
