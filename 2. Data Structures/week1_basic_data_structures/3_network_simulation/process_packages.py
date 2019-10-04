# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):        
        arrived_at = request.arrived_at
        while (self.finish_time)and(self.finish_time[0] <= arrived_at):
            self.finish_time.popleft()
            
        if (len(self.finish_time) == self.size):
            return Response(True, -1)
        
        if self.finish_time:
            arrived_at = max(arrived_at, self.finish_time[-1])
            self.finish_time.append(arrived_at + request.time_to_process)
        else:
            self.finish_time.append(arrived_at + request.time_to_process)
            
        # write your code here
        return Response(False, arrived_at)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
