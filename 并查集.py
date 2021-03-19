# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False # 有环！！！！！！！！！
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool: # 有环！！！！！！！！！
        x, y = self.findset(x), self.findset(y)
        return x == y

if __name__ == '__main__':
    T = int(input()) # T组数据
    while T:
        n, m = map(int, input().split(' ')) # n*n m个边
        uf = UnionFind(n)
        ok = 0 #已经是对角线了
        huan = 0 #环的数量
        for _ in range(m):
            x, y = map(int, input().split(' '))
            if x == y: ok += 1
            elif not uf.unite(x-1, y-1): huan += 1 # 形成环
        print(m+huan-ok)
        T -= 1

