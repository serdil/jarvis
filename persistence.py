import os
import pickle

from JobsManager import JobsManager

user_home = os.path.expanduser("~")
jarvis_home = os.path.join(user_home, ".jarvis")
jobs_manager_file = os.path.join(jarvis_home, "jobs_data")


def ensure_application_folder_exists():
    if not application_folder_exists():
        create_application_folder()


def application_folder_exists():
    return os.path.exists(jarvis_home)


def create_application_folder():
    os.makedirs(jarvis_home)


def retrieve_jobs_manager():
    ensure_application_folder_exists()
    if jobs_manager_exists():
        return deserialize_jobs_manager()
    else:
        return JobsManager()


def jobs_manager_exists():
    return os.path.exists(jobs_manager_file)


def deserialize_jobs_manager():
    return pickle.load(open(jobs_manager_file, "rb"))


def persist_jobs_manager(jobs_manager):
    pickle.dump(jobs_manager, open(jobs_manager_file, "wb"))
