#Uses python3

import sys


def negative_cycle(adj):
    dis={};m=1000000
    for i in range(1,len(adj)+1):
        dis[i]=m
    dis[1]=0
    n=len(adj)
    x=0;neg=False
    while(True):
        boo=False
        for i in adj.keys():
            for j in adj[i].keys():
                if(dis[j]>dis[i]+adj[i][j]):
                    boo=True
                    dis[j]=dis[i]+adj[i][j]
        if(not boo):
            break
        x+=1
        if(x>=n):
            neg=True
            break   
    return int(neg)


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
    '''
    n,m=map(int,input().split())
    adj = [[] for _ in range(n)]
    adj={}
    for i in range(1,n+1):
        adj[i]={}
    for i in range(m):
        a=[int(i) for i in input().split()]
        adj[a[0]][a[1]]=a[2]
    '''
    print(negative_cycle(adj))
