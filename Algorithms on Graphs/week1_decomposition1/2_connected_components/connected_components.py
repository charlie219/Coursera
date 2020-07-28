#Uses python3

import sys
visited={}
def dfs(adj,node):
    visited[node]=True
    for i in adj[node]:
        if(not visited[i]):
            dfs(adj,i)

def number_of_components(adj):
    result = 0
    global visited
    for i in adj.keys():
        visited[i]=False
    #write your code here
    for i in adj.keys():
        if(not visited[i]):
            dfs(adj,i)
            result+=1
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj={}
    for i in range(1,n+1):
        adj[i]=[]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    print(number_of_components(adj))
