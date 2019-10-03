# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def sift_down(a, i):
    n = len(a)
    min_index = i
    if 2 * i + 1 < n:
        if ((a[2*i + 1].started_at < a[min_index].started_at)or
            ((a[2 * i + 1].started_at == a[min_index].started_at)and
             (a[2 * i + 1].worker < a[min_index].worker))):
            min_index = 2 * i + 1

    if 2 * i + 2 < n:
        if ((a[2*i + 2].started_at < a[min_index].started_at)or
            ((a[2 * i + 2].started_at == a[min_index].started_at)and
             (a[2 * i + 2].worker < a[min_index].worker))):
            min_index = 2 * i + 2

    if min_index != i:
        a[i], a[min_index] = a[min_index], a[i]
        sift_down(a, min_index)

def assign_jobs(n_workers, jobs):
    workers = []
    for i in range(n_workers):
        workers.append(AssignedJob(i, 0))

    result = []
    for job_time in jobs:
        result.append(workers[0])
        workers[0] = AssignedJob(workers[0].worker, workers[0].started_at + job_time)
        sift_down(workers, 0)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
