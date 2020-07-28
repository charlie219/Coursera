#Uses python3

import sys
import queue

def distance(adj, s, t):
    visited=[False]*len(adj)
    visited[s-1]=True
    q=[[s,0]]
    while(len(q)>0):
        v=q[0];q.pop(0)
        if v[0]==t:
            return v[1]
        for i in adj[v[0]]:
            if(not visited[i-1]):
                q.append([i,v[1]+1])
                visited[i-1]=True
    return -1

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    s, t = data[2 * m], data[2 * m + 1]
    '''
    n,m=map(int,input().split())
    edges=[tuple(map(int,input().split())) for i in range(m)]
    s,t=map(int,input().split())
    '''
    adj = {}
    for i in range(1,n+1):
        adj[i]=[]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    print(distance(adj, s, t))
