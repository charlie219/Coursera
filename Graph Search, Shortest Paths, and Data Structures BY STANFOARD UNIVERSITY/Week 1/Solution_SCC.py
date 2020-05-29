from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
import sys
import os
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

sys.setrecursionlimit(15000)
stdin = open(os.path.join(sys.path[0],'input.txt'),'r')
n,x=multi_int_input()
graph={};rev_graph={}
for i in range(1,n+1):
    graph[i]=[]
    rev_graph[i]=[]
#print(graph)
for i in range(x):
    a,b=multi_int_input()
    graph[a].append(b)
    rev_graph[b].append(a)

#-------------------------------DRIVER CODE--------------------------------------------------  
t=0;s=-1
visited=[False for i in range(n+1)]
f_time=[0 for i in range(n+1)]
leader=[None for i in range(n+1)]
s=1
def dfs(node,G):
    global t
    visited[node]=True
    leader[node]=s
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
            #print(stack)
            v=stack.pop()
            t+=1;leader[v]=s
            f_time[v]=t
    return count
    
for i in range(n,0,-1):
    if(not visited[i]):
        s=i
        dfs(i,rev_graph)
        
new_g={}
for i in range(1,n+1):
    new_g[f_time[i]]=[]
    for j in graph[i]:
        new_g[f_time[i]].append(f_time[j])
        
ans=[]
visited=[False for i in range(n+1)]
for i in range(n,0,-1):
    temp=dfs(i,new_g)
    if(temp==1):
        continue
    ans.append(temp)
print(*sorted(ans)[::-1][:5])


'''
ANSWER: 434821,968,459,313,211
'''
























