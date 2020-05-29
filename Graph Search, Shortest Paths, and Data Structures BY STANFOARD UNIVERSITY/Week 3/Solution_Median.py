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
stdin = open(os.path.join(sys.path[0],'Median.txt'),'r')

#------------------------------DRIVER CODE----------------------------------------------------------------------------------------------
from heapq import heappush,heappop
ans=0
min_h=[];max_h=[]
n=10000                              #Number of inputs
len_max=0;len_min=0
for i in range(n):
    temp=int_input()
    heappush(max_h,-temp)
    len_max+=1
    if(len_min>0 and -max_h[0]>min_h[0]):
        x=heappop(max_h);y=heappop(min_h)
        heappush(max_h,-y);heappush(min_h,-x)

        
    if(len_max>len_min+1):
        len_max-=1;len_min+=1
        xy=-heappop(max_h)
        heappush(min_h,xy)
      
    ans+=-max_h[0]

print(ans)




















        
