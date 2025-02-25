class UnionFind:
    def __init__(self, size):
        # The ith element of the Parent[] array is the parent of the ith item.
        # Initialize the parent array with each element as its own representative.
        self.parent = list(range(size))
        self.rank = [0] * size

    '''
        Find representative of the set given a element i. The representative is always the root of the tree. 
    '''
    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path Compression Here
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    '''
        Combine two sets and make one. 
        1. Find reps of the two sets of two elements given in the input 
        2. Put either one of the trees (represent the set) under the root node of the another tree
    '''
    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        # Let the irep be the parent of jrep
        self.parent[jrep] = irep

    def union_by_rank(self, i, j):
        # 小的往大的底下放
        irep = self.find(i)
        jrep = self.find(j)

        if irep == jrep:
            # do nothing
            return

        # Union by Rank
        if self.rank[irep] < self.rank[jrep]:
            self.parent[irep] = jrep
        elif self.rank[jrep] < self.rank[irep]:
            self.parent[jrep] = irep
        else:
            self.parent[jrep] = irep
            self.rank[irep] += 1







size = 5
uf = UnionFind(size)
uf.union(1,2)
uf.union(3,4)
in_same_set = (uf.find(1) == uf.find(2))
print("Are 1 and 2 in the same set?", "Yes" if in_same_set else "No")

'''
n: number of the element
Time Complexity: O(n) - Worst Case the tree becomes like a linked list
Space Complexity: O(n) - the parent array 

Optimization: 
Path Compression (Used to improve find()):

Union By Rank (Modifications to union())
Put tree with smaller height under the tree with larger height so there is no increase in height. 
If the ranks are equal, it doesn’t matter which tree goes under the other, but the rank of the result will always be one greater than the rank of the trees.
'''

'''
Reference: https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
'''

