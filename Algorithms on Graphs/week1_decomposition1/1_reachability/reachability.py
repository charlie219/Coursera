#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    q=[x];
    visited={}
    for i in adj.keys():
        visited[i]=False
    visited[x]=True                         #Using BFS instead of DFS
    while(len(q)>0):
        v=q[0];q.pop(0)
        if(v==y):
            return 1
        for i in adj[v]:
            if(not visited[i]):
                visited[i]=True
                q.append(i)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = {}
    for i in range(1,n+1):
        adj[i]=[]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    print(reach(adj, x, y))
