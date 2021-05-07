from epic_manager import EpicManager
from epic_manager_gui import EpicManagerGui
import logging
import time
import argparse


def main():
    # noinspection PyArgumentList
    logging.basicConfig(encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s')
    logger = logging.getLogger("epic_manager_log")
    logger.info(f'Welcome to Epic Manager')
    logger.info(f'.......................')
    time.sleep(1)
    epic_id = input("Please enter the Epic ID: ")
    if epic_id:
        # Create EpicManager instance
        epic_manager = EpicManager()

        # Do the thing
        result = epic_manager.manage_epic(epic_key=epic_id)
        logger.info(f"Finished! Result: {result}")
    else:
        logger.info(f"No Epic ID entered. Aborting.")


def main_gui():
    # noinspection PyArgumentList
    logging.basicConfig(encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s')
    logger = logging.getLogger("epic_manager_log")
    logger.info(f'Welcome to Epic Manager')
    logger.info(f'.......................')

    epic_manager_gui = EpicManagerGui()
    epic_manager_gui.show()


def get_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Jira Epic Manager')
    parser.add_argument('--gui', action='store_true', help='Use the GUI front end')
    return parser.parse_args()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = get_args()
    print(args.gui)
    if args.gui:
        main_gui()
    else:
        main()

