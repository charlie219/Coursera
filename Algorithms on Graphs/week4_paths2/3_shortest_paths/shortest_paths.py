#Uses python3

import sys
import queue
from collections import deque 


def shortet_paths(adj,s):
    n=len(adj)
    m=1e19;dis={}
    for i in range(1,len(adj)+1):
        dis[i]=m
    dis[s]=0
    x=0;neg=False
    q=deque()
    while(True):
        boo=False
        for i in adj.keys():
            for j in adj[i].keys():
                if(dis[j]>dis[i]+adj[i][j]):
                    boo=True
                    dis[j]=dis[i]+adj[i][j]
                    if(x==n):
                        q.append(j)
                        q.append(i)
        if(not boo):
            break
        x+=1
        if(x==n+1):
            break
    #print(q)
    neg_cy={}
    visited=[False for i in range(n+1)]
    while(len(q)>0):
        v=q.popleft()
        neg_cy[v]=1
        for i in adj[v].keys():
            if(not visited[i]):
                visited[i]=True
                q.append(i)
    for i in range(1,n+1):
        if(dis[i]==m):
            print("*")
        elif(i in neg_cy):
            print("-")
        else:
            print(dis[i])
            

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj={}
    for i in range(1,n+1):
        adj[i]={}
    for ((a, b), w) in edges:
        adj[a][b]=w
    s = data[0]
    '''
    n,m=map(int,input().split())
    adj = [[] for _ in range(n)]
    adj={}
    for i in range(1,n+1):
        adj[i]={}
    for i in range(m):
        a=[int(i) for i in input().split()]
        adj[a[0]][a[1]]=a[2]
    s=int(input())
    '''
    shortet_paths(adj,s)

