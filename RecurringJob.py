from datetime import date, timedelta
from RegularJob import RegularJob


class RecurringJob:
    job_id = None
    name = None
    period = None
    minfactor = None
    last_start = None
    job = None

    def __init__(self, job_id, name, period, minfactor=5):
        self.job_id = job_id
        self.name = name
        self.period = period
        self.minfactor = minfactor
        self.update_job()

    def set_id(self, id):
        self.job_id = id

    def get_id(self):
        return self.job_id

    def get_name(self):
        return self.name

    def is_recurring(self):
        return True

    def reset(self):
        self.update_job()

    def update_job(self):
        self.last_start = date.today()
        self.job = RegularJob(self.job_id, self.name, self.get_deadline(), self.minfactor)

    def get_deadline(self):
        return self.last_start + timedelta(days=self.period)

    def get_priority(self):
        return self.job.get_priority()
