#Uses python3

import sys
visited={};P=1
def chk(adj,node):
    
    visited[node][0]=True
    visited[node][1]=P
    stack=[node]
    while(len(stack)>0):
        v=stack.pop()
        for i in adj[v]:
            #print(v,i,visited,adj)
            if(visited[i][0] and visited[i][1]==P):
                return 1
            if(visited[i][0]):
                continue
            visited[i][0]=True
            visited[i][1]=P
            stack.append(i)
        #print(stack,visited)
    return 0
    


def acyclic(adj):
    global visited
    global P
    P=1
    for i in adj.keys():
        visited[i]=[False,None]
    for i in adj.keys():
        if(not visited[i][0]):
            if(chk(adj,i)):
                return 1
            P+=1
    return 0

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

    print(acyclic(adj))
'''
4 4
1 2
4 1
2 3
3 1
'''
