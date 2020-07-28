#Uses python3
import sys
import math
from heapq import heappush,heappop
dis=lambda x1,y1,x2,y2:math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
graph={}
def make_graph():
    dic={}
    for i in range(n):
        dic[i]=(x[i],y[i])
    for i in range(n):
        graph[i+1]={}
        for j in range(n):
            if(i==j):
                continue
            graph[i+1][j+1]=dis(dic[i][0],dic[i][1],dic[j][0],dic[j][1])
       
def minimum_distance(x, y):
    result = 0.
    make_graph()
    cost=[1e19]*(n+1);dic={}
    cost[1]=0
    q=[(0,1)]
    #print(graph)
    while(len(q)>0):
        v=heappop(q)
        if(v[1] in dic):
            continue
        dic[v[1]]=1
        result+=v[0]
        for each in graph[v[1]].keys():
            if(each not in dic and cost[each]>graph[v[1]][each]):
                heappush(q,(graph[v[1]][each],each))
                cost[each]=graph[v[1]][each]
        #print(q,dic)        
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    '''
    n=int(input());x=[];y=[]
    for i in range(n):
        a,b=map(int,input().split())
        x.append(a)
        y.append(b)
    '''
    print("{0:.9f}".format(minimum_distance(x, y)))
