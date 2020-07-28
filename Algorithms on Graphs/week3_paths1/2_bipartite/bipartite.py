#Uses python3

import sys
import queue

def bipartite(adj):
    visited=[False]*len(adj)
    visited[0]=True
    color=[-1]*len(adj)
    q=[1]
    while(len(q)>0):
        v=q[0];q.pop(0)
        for i in adj[v]:
            if(visited[i-1] and color[i-1]==color[v-1]):
                return 0
            if(not visited[i-1]):
                visited[i-1]=True
                color[i-1]=1 if color[v-1]==0 else 0
                q.append(i)
    return 1

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    '''
    n,m=map(int,input().split())
    edges=[tuple(map(int,input().split())) for i in range(m)]
    '''
    
    adj = {}
    for i in range(1,n+1):
        adj[i]=[]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    print(bipartite(adj))
