from RegularJob import RegularJob
from RecurringJob import RecurringJob
from FreeJob import FreeJob


def create_job(job_id, properties):
    properties["job_id"] = job_id
    job_type = properties["type"]
    if job_type == "regular":
        return create_regular_job(properties)
    elif job_type == "recurring":
        return create_recurring_job(properties)
    elif job_type == "free":
        return create_free_job(properties)


def create_regular_job(properties):
    return RegularJob(properties["job_id"], properties["name"], properties["deadline"])


def create_recurring_job(properties):
    return RecurringJob(properties["job_id"], properties["name"], properties["period"])


def create_free_job(properties):
    return FreeJob(properties["job_id"], properties["name"], properties["recurring"])
