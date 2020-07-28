#Uses python3

import sys
import queue
from heapq import heappush,heappop

def distance(adj, s, t):
    dis={};h=[];m=1000000
    for i in range(len(adj)):
        dis[i+1]=m
        heappush(h,[m,i+1])
    dis[s]=0
    x=1
    while(len(h)>0):
        u=heappop(h)[1]
        boo=True
        #print(adj[u])
        for v in adj[u].keys():
            if(dis[v]>dis[u]+adj[u][v]):
                dis[v]=dis[u]+adj[u][v]
                heappush(h,[dis[v],v])
    
    if(dis[t]==m):
        return -1
    else:
        return dis[t]


if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    s, t = data[0], data[1]
    adj={}
    for i in range(1,n+1):
        adj[i]={}
    for ((a, b), w) in edges:
        adj[a][b]=w
    '''
    n,m=map(int,input().split())
    adj = [[] for _ in range(n)]
    adj={}
    for i in range(1,n+1):
        adj[i]={}
    for i in range(m):
        a=[int(i) for i in input().split()]
        adj[a[0]][a[1]]=a[2]
    s,t=map(int,input().split())
    '''
    print(distance(adj, s, t))
