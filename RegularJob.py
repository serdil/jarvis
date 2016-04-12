from datetime import date


class RegularJob:
    job_id = None
    name = None
    start = None
    deadline = None
    minfactor = None
    priority_bonus = 0

    def __init__(self, job_id, name, deadline, minfactor=10):
        self.job_id = job_id
        self.name = name
        self.deadline = deadline
        self.start = date.today()
        self.minfactor = minfactor

    def set_id(self, id):
        self.job_id = id

    def get_id(self):
        return self.job_id

    def get_name(self):
        return self.name

    def is_recurring(self):
        return False

    def get_priority(self):
        return self.get_base_priority() + self.priority_bonus

    def set_priority_bonus(self, bonus):
        self.priority_bonus = bonus

    def get_base_priority(self):
        elapsed_days = self.days_since_start()
        remaining_days = self.days_till_deadline()
        return float(self.duration_factor()) * elapsed_days / remaining_days

    def days_since_start(self):
        days = (date.today() - self.start).days
        return self.make_sure_at_least_one(days)

    def days_till_deadline(self):
        days = (self.deadline - date.today()).days
        return self.make_sure_at_least_one(days)

    def duration_factor(self):
        timeframe = self.job_timeframe()
        if timeframe < self.minfactor:
            return self.minfactor
        else:
            return timeframe

    def job_timeframe(self):
        return (self.deadline - self.start).days

    def get_priority_bonus(self):
        return self.priority_bonus

    @staticmethod
    def has_deadline():
        return True

    def is_urgent(self):
        return self.days_till_deadline() <= 2

    @staticmethod
    def make_sure_at_least_one(val):
        if val < 1:
            return 1
        else:
            return val
