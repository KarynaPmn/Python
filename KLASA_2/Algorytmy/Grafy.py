##wejście
#5 4
#2 3
#1 3
#5 1
#5 3

D = {}

n, m = map(int, input().split())

for i in range(n):
    D[i+1] = []
    #D.update({i+1:[]})

for _ in range(m): #idzie ale nie ma zmiennej
    p, q = map(int, input().split())
    D[p].append(q)
    D[q].append(p)

print(D)

for i in range(1,n+1):
    if len(D[i]) == 0:
        print("Wiewior sam!")
    else:
        D[i].sort()
        for j in range(len(D[i])):
            print(D[i][j], end=" ")
        print()


##################################################

### losowy graf ###

# from random import randint
# n = 6
# D = {}

# for d in (1, n+1):
#     D[d] = []

# ik = 1 + randint(0, 6) / 10 # ile krawędzi ( 0.0 - 0.5 --> 1.0 - 1.5)

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i > j:
#             w = randint(0, 10) * ik
#             if w >= 5:
#                 D[i].append(j)
#                 D[j].append(i)
            
# for i in range(1,n+1):
#     if len(D[i]) == 0:
#         print("pusto")
#     else:
#         D[i].sort()
#         for j in range(len(D[i])):
#             print(D[i][j], end=" ")
#         print()

####################################

# 1. Policz sumę stopni wierzchołków grafu

sumWie = 0

for k, v in D.items():
    sumWie += len(v)

print("Suma wierzchołków: ", sumWie)


# 2. Znajdź wierzchołek o najwyższym stopniu

maxWie = 0

for _, y in D.items():
    maxWie = max(maxWie, len(y))

print("Najwyższy stopień: ", maxWie)

# 3. Znajdź wierzchołki samodzielnie



# 4. Sprawdź czy uda się dojść z wierzchołka x do y

## SPOSÓB I
# def DFS(n, D, vis):
#     if vis == None:
#         vis = list()
#     if n not in vis:
#         vis.append(n)
#     else:
#         return
#     for nei in D[n]: # sąsiad
#         DFS(nei, D, vis)
#     return vis

## SPOSÓB II
def DFS(n, D, vis):
    vis.append(n)
    for nei in D[n]:
        if nei not in vis:
            DFS(nei, D, vis)
    return vis

##
visited = []
W = DFS(1, D, visited)
print(W)
