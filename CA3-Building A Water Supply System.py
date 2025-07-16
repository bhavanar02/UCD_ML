class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def min_cost(villages, well_costs, connections):
    edges = []
    uf = UnionFind(villages + 1)
    total_cost = 0
    
    for i in range(villages):
        if well_costs[i] >= 0:
            edges.append((well_costs[i], i, villages))
    
    for start, end, cost in connections:
        edges.append((cost, start - 1, end - 1))
    edges.sort()
    for cost, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            total_cost += cost
    
    return total_cost

if __name__ == "__main__":
    import sys
    
    data = sys.stdin.read().split()
    idx = 0
    test_cases = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(test_cases):
        villages = int(data[idx])
        num_roads = int(data[idx + 1])
        idx += 2
        wells = list(map(int, data[idx:idx + villages]))
        idx += villages
        roads = []
        
        for _ in range(num_roads):
            a, b, c = map(int, data[idx:idx + 3])
            roads.append((a, b, c))
            idx += 3
        
        results.append(min_cost(villages, wells, roads))
    
    for i in results:
        print(i)
