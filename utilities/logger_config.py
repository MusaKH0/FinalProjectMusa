import glob
import os
import logging
import time
from pathlib import Path


def logger_setup(logger_name):
    # ##-----------------Execution Log Logics----------------------------##
    # LOGGER_PATH = os.getcwd() + str(Path("/testLogs/logger_1.log"))
    # available_logs = glob.glob("/testLogs/*")
    # if available_logs == []:
    #     open(LOGGER_PATH, "w+")
    # else:
    #     if len(available_logs) == 1:
    #         LOGGER_PATH = os.getcwd() + str(Path("/testLogs/logger_2.log"))
    #         open(LOGGER_PATH, "w+")
    #     else:
    #         files_id = [int(i.split("_")[-1].split(".log")[0]) for i in available_logs]
    #         files_id.sort()
    #         LOGGER_PATH = os.getcwd() + str(Path("/testLogs/logger_{0}.log".format(files_id[-1] + 1)))
    #         open(LOGGER_PATH, "w+")

    time_stamp = time.strftime("%Y-%m-%d_%I-%M")
    filename = f"automation_{time_stamp}.log"
    logs_directory = "../testLogs/"
    relative_filepath = logs_directory + filename
    current_directory = os.path.dirname(__file__)
    destination_file = os.path.join(current_directory, relative_filepath)
    destination_directory = os.path.join(current_directory, logs_directory)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    logger = logging.getLogger(logger_name)
    if not len(logger.handlers):
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(destination_file)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt="%(asctime)s: %(levelname)s: %(name)s: - %(message)s",
                                      datefmt="%m-%d-%Y_%I:%M:%S %p")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
