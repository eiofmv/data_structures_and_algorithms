# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

def mod(a, b):
    return ((a % b) + b) % b

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = mod((ans * self._multiplier + ord(c)), self._prime)
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end            
            self.write_chain(reversed(self.elems.get(query.ind, [])))
        elif query.type == 'del':
            index = self._hash_func(query.s)
            l = self.elems.get(index, [])
            for i in range(len(l)):
                if query.s == l[i]:
                    self.elems[index].pop(i)
                    break
        elif query.type == 'find':
            self.write_search_result(query.s in self.elems.get(self._hash_func(query.s), []))
        else:
            index = self._hash_func(query.s)
            self.elems[index] = self.elems.get(index, [])
            if query.s not in self.elems.get(index, []):
                self.elems[index].append(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
