# python3

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.rank = [0 for _ in range(n_tables)]
        self.parents = list(range(n_tables))

    def merge(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent != dst_parent:
            if self.rank[src_parent] > self.rank[dst_parent]:
                dst_parent, src_parent = src_parent, dst_parent
            self.rank[dst_parent] += int(self.rank[src_parent] == self.rank[dst_parent])
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        

    def get_parent(self, table):
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
