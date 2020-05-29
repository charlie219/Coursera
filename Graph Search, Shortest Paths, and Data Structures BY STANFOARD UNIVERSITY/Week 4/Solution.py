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
stdin = open(os.path.join(sys.path[0],'algo1-programming_prob-2sum.txt'),'r')

#-------------------------------------INPUT-------------------------------------------------
hash_dic={}
for i in range(1000000):
    hash_dic[int_input()]=0
print(len(hash_dic))

#-------------------------------------DRIIVER CODE------------------------------------------
result=0
for i in range(-10000,10001):
    for j in hash_dic.keys():
        if(i-j in hash_dic.keys()):
            result+=1
            break
print(result)
