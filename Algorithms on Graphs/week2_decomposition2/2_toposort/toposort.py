#Uses python3

import sys
order=[];visited={}
def dfs(adj,x):
    visited[x]=True
    stack=[x];boo=True
    for i in adj[x]:
        if(not visited[i]):
            dfs(adj,i)
    order.append(x)
        
    


def toposort(adj):
    global visited
    for i in adj.keys():
        visited[i]=False
    #write your code here
    for i in adj.keys():
        if(not visited[i]):
            dfs(adj,i)
            

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
    toposort(adj)
    print(*order[::-1])

'''
5 10
4 5
3 1
2 1
2 3
5 1
2 5
4 1
2 4
3 4
3 5
'''
