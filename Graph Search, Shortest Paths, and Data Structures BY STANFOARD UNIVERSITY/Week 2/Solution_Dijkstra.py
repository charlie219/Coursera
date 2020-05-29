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
stdin = open(os.path.join(sys.path[0],'dijkstraData.txt'),'r')


#----------------------------INPUT-----------------------------------------------------------------------
graph={};tot=0
find=[7,37,59,82,99,115,133,165,188,197]
n=200
for i in range(1,n+1):
    a=list(map(str,stdin.readline().split()))
    graph[i]={}
    for j in a[1:]:
        tot+=1
        #print("*",j,"*")
        ind=j.index(',')
        graph[i][int(j[:ind])]=int(j[ind+1:])
        
#-----------------------------DRIVER CODE-------------------------------------------------------------------
from heapq import heappush
dis=[1000000 for i in range(n+1)]
dis[1]=0
x={1:0}
boo=True
while(boo):
    boo=False
    h=[]
    for i in x.keys():
        for j in graph[i].keys():
            if(j not in x.keys()):
                boo=True
                heappush(h,(dis[i]+graph[i][j],j,i))
    if(not boo):
        break
    v=h[0]
    x[v[1]]=0
    dis[v[1]]=dis[v[2]]+graph[v[2]][v[1]]
ans=""
for i in find:
    ans+=str(dis[i])+","
    
print(ans)
    
























