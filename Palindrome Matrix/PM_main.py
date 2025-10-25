import sys
input = sys.stdin.readline


class PalindromeMatrix:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

idx = [[-1]*M for _ in range(N)]
cells = []
count = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] != '.':
            idx[i][j] = count
            cells.append((i, j))
            count += 1

uf = PalindromeMatrix(count)

# Horizontal unions
for i in range(N):
    j = 0
    while j < M:
        if grid[i][j] == '.':
            j += 1
            continue
        start = j
        while j < M and grid[i][j] != '.':
            j += 1
        end = j - 1
        while start < end:
            uf.union(idx[i][start], idx[i][end])
            start += 1
            end -= 1

# Vertical unions
for j in range(M):
    i = 0
    while i < N:
        if grid[i][j] == '.':
            i += 1
            continue
        start = i
        while i < N and grid[i][j] != '.':
            i += 1
        end = i - 1
        while start < end:
            uf.union(idx[start][j], idx[end][j])
            start += 1
            end -= 1

# Collect components
groups = {}
for k, (r, c) in enumerate(cells):
    root = uf.find(k)
    groups.setdefault(root, []).append((r, c))

# Assign optimal digits
for g in groups.values():
    digits = sorted(int(grid[r][c]) for r, c in g)
    median = digits[len(digits)//2]
    # choose smaller if even
    if len(digits) % 2 == 0:
        median = digits[len(digits)//2 - 1]
    for r, c in g:
        grid[r][c] = str(median)

# Output
for row in grid:
    print(''.join(row))
