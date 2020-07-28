#Uses python3

import sys
visited=[];f_time=[];t=0

def dfs(node,G):
    global t
    visited[node]=True
    stack=[node];count=1
    while(len(stack)>0):
        sink=True
        x=stack[-1]
        for i in G[x]:
            if(not visited[i]):
                count+=1
                stack.append(i)
                visited[i]=True
                sink=False
        if(sink):
            v=stack.pop()
            t+=1
            f_time[v]=t
    return count

def number_of_strongly_connected_components(adj,rev):
    global visited;global f_time
    visited=[False for i in range(n+1)]
    f_time=[0 for i in range(n+1)]
    result = 0
    #write your code here
    new={}
    for i in range(1,len(adj)+1):
        if(not visited[i]):
            dfs(i,rev)
    #print(f_time)
    #print(adj)
    for i in range(1,len(adj)+1):
        new[f_time[i]]=[]
        for j in adj[i]:
            new[f_time[i]].append(f_time[j])
    #print(new)
    visited=[False for i in range(n+1)]
    for i in range(len(adj),0,-1):
        if(not visited[i]):
            dfs(i,new)
            result+=1
    return result

if __name__ == '__main__':
    '''
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    '''
    n,m=map(int,input().split())
    edges=[tuple(map(int,input().split())) for i in range(m)]
    
    adj = {};rev={}
    for i in range(1,n+1):
        adj[i]=[]
        rev[i]=[]
    for (a, b) in edges:
        adj[a].append(b)
        rev[b].append(a)
    print(number_of_strongly_connected_components(adj,rev))
