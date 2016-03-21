from utils import create_job


class JobsManager:
    jobs_counter = -1
    jobs = []

    def __init__(self, jobs=[]):
        self.jobs.extend(jobs)
        self.sort_jobs()

    def sort_jobs(self):
        self.jobs = list(reversed(sorted(self.jobs, key=self.job_priority)))

    def finish_job(self, job_id):
        job_index = self.find_job_index_by_id(job_id)
        if job_index != -1:
            self.finish_job_at_index(job_index)

    def remove_job(self, job_id):
        job_index = self.find_job_index_by_id(job_id)
        if job_index != -1:
            self.remove_job_at_index(job_index)

    def find_job_index_by_id(self, job_id):
        index = 0
        for job in self.jobs:
            if job.get_id() == job_id:
                return index
            index += 1
        return -1

    def finish_job_at_index(self, job_index):
        if self.jobs[job_index].is_recurring():
            self.jobs[job_index].reset()
        else:
            del self.jobs[job_index]

    def remove_job_at_index(self, job_index):
        del self.jobs[job_index]

    def get_jobs(self):
        self.sort_jobs()
        return self.jobs

    def add_job(self, job_properties):
        self.jobs.append(create_job(self.increment_id(), job_properties))

    def increment_id(self):
        self.jobs_counter += 1
        return self.jobs_counter

    @staticmethod
    def job_priority(job):
        return job.get_priority()
