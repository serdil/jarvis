from datetime import date


class FreeJob:
    job_id = None
    name = None
    start = None
    recurring = None

    def __init__(self, job_id, name, recurring=False):
        self.job_id = job_id
        self.name = name
        self.recurring = recurring
        self.reset()

    def set_id(self, id):
        self.job_id = id

    def get_id(self):
        return self.job_id

    def get_name(self):
        return self.name

    def is_recurring(self):
        return self.recurring

    def reset(self):
        self.start = date.today()

    def get_priority(self):
        return self.days_since_start()

    def days_since_start(self):
        days = (date.today() - self.start).days
        return self.make_sure_not_zero(days)

    @staticmethod
    def make_sure_not_zero(val):
        if val == 0:
            return 1
        else:
            return val
