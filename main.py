import os
import re
import sys
import logging
from logging import StreamHandler


def delete_edge() -> None:
    try:

        PATH = 'C:\Program Files (x86)\Microsoft\Edge\Application\ '
        os.chdir(PATH)
        pattern = re.compile(r'\d\d\.\d\.\d\d\d\.\d\d')
        list_dir = os.listdir('.')
        for item in list_dir:
            if pattern.match(item):
                os.chdir(item)
        os.chdir('Installer')
        os.system('@echo off')
        os.system('@chcp 65001')
        os.system(
            'setup.exe --uninstall --system-level --verbose-logging --forse-uninstall')
        os.system('cls')
        logging.info('Edge is uninstalled')

    except Exception as e:
        print('Error can\'t delete Edge')
        logging.exception('Error can\'t delete Edge')
        # logging.warning(e)


def install_edge() -> None:
    try:
        # os.system('winget install Microsoft.Edge')
        os.startfile(f'{os.getcwd()}\\MicrosoftEdgeSetup.exe')
        os.system('cls')
    except Exception:
        # print('Install winget from https://github.com/microsoft/winget-cli/releases')
        logging.exception('Can not installed')


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.basicConfig(filename='logs.log', filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')
    handler = StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)
    # logger.info('Удаление Edge')
    # delete_edge()
    while True:
        print('1.Удалить Microsoft Edge Chromium\n2.Установить Microsoft Edge Chromium\n0.Выйти')
        choise = int(input("Введите вариант: "))
        if choise == 1:
            logging.info('Выбран вариант удаления Edge')
            delete_edge()
        elif choise == 2:
            logging.info('Выбран вариант установки Edge')
            install_edge()
        elif choise == 0:
            exit()
        else:
            print('Введите правильный вариант')
            logging.info('Выбран неправильный вариант')
