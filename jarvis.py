import sys
from datetime import datetime

import persistence

def main():
    jobs_manager = persistence.retrieve_jobs_manager()
    while True:
        inputs = input("enter a command: ").split(" ")
        if len(inputs) == 0:
            continue
        else:
            process_inputs(inputs, jobs_manager)
        print_jobs(jobs_manager)
        persistence.persist_jobs_manager(jobs_manager)


def process_inputs(inputs, jobs_manager):
    command = inputs[0]
    if command == "exit":
        persist_and_exit_program(jobs_manager)
    elif command == "list":
        pass
    elif command == "add":
        validate_and_add_new_job(inputs, jobs_manager)
    elif command == "finish":
        validate_and_finish_job(inputs, jobs_manager)
    elif command == "remove":
        validate_and_remove_job(inputs, jobs_manager)
    elif command == "addbonus":
        validate_and_add_bonus_to_job(inputs, jobs_manager)
    else:
        print_invalid_command_message()


def persist_and_exit_program(jobs_manager):
    persistence.persist_jobs_manager(jobs_manager)
    sys.exit()


def print_jobs(jobs_manager):
    print("\n" + list_jobs_as_string(jobs_manager))


def list_jobs_as_string(jobs_manager):
    return "\n".join(jobs_as_strings(jobs_manager))


def jobs_as_strings(jobs_manager):
    return [job_as_string(job) for job in jobs_manager.get_jobs()]


def job_as_string(job):
    return str(str(job.get_id()) + ": " + job.get_name()) + " " + str(job.get_priority())


def validate_and_add_new_job(inputs, jobs_manager):
    if len(inputs) < 2:
        print_invalid_command_message()
    else:
        add_new_job(inputs, jobs_manager)


def add_new_job(inputs, jobs_manager):
    job_type = inputs[1]
    if job_type == "regular":
        validate_add_regular_job(inputs, jobs_manager)
    elif job_type == "recurring":
        validate_add_recurring_job(inputs, jobs_manager)
    elif job_type == "free":
        validate_add_free_job(inputs, jobs_manager)
    else:
        print_invalid_command_message()


def validate_add_regular_job(inputs, jobs_manager):
    if len(inputs) < 4 or not is_valid_date(inputs[3]):
        print_invalid_command_message()
    else:
        add_regular_job(inputs, jobs_manager)


def is_valid_date(datestr):
    try:
        parse_date(datestr)
        return True
    except ValueError:
        return False


def add_regular_job(inputs, jobs_manager):
    jobs_manager.add_job({"type": "regular", "name": inputs[2], "deadline": parse_date(inputs[3])})


def parse_date(datestr):
    return datetime.strptime(datestr, "%d.%m.%y").date()


def validate_add_recurring_job(inputs, jobs_manager):
    if len(inputs) < 4 or not is_valid_int(inputs[3]):
        print_invalid_command_message()
    else:
        add_recurring_job(inputs, jobs_manager)


def is_valid_int(intstr):
    try:
        int(intstr)
        return True
    except ValueError:
        return False


def add_recurring_job(inputs, jobs_manager):
    jobs_manager.add_job({"type": "recurring", "name": inputs[2], "period": int(inputs[3])})


def validate_add_free_job(inputs, jobs_manager):
    if len(inputs) < 3:
        print_invalid_command_message()
    elif len(inputs) == 4 and inputs[3] == "recurring":
        add_recurring_free_job(inputs, jobs_manager)
    else:
        add_non_recurring_free_job(inputs, jobs_manager)


def add_non_recurring_free_job(inputs, jobs_manager):
    jobs_manager.add_job({"type": "free", "name": inputs[2], "recurring": False})


def add_recurring_free_job(inputs, jobs_manager):
    jobs_manager.add_job({"type": "free", "name": inputs[2], "recurring": True})


def validate_and_finish_job(inputs, jobs_manager):
    if len(inputs) < 2 or not is_valid_int(inputs[1]):
        print_invalid_command_message()
    else:
        jobs_manager.finish_job(int(inputs[1]))


def validate_and_remove_job(inputs, jobs_manager):
    if len(inputs) < 2 or not is_valid_int(inputs[1]):
        print_invalid_command_message()
    else:
        jobs_manager.remove_job(int(inputs[1]))


def validate_and_add_bonus_to_job(inputs, jobs_manager):
    if len(inputs) < 3 or not is_valid_int(inputs[1]) or not is_valid_int(inputs[2]):
        print_invalid_command_message()
    else:
        jobs_manager.add_bonus_to_job(int(inputs[1]), int(inputs[2]))


def print_invalid_command_message():
    print("invalid command")


main()
