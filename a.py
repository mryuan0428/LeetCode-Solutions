class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False 
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool: 
        x, y = self.findset(x), self.findset(y)
        return x == y

if __name__ == '__main__':
    T = int(input()) 
    while T:
        n, m = map(int, input().split(' '))
        uf = UnionFind(n)
        ok = 0 
        huan = 0 
        for _ in range(m):
            x, y = map(int, input().split(' '))
            if x == y: ok += 1
            elif not uf.unite(x-1, y-1): huan += 1
        print(m+huan-ok)
        T -= 1

