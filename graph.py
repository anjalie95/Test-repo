
 #Undirected Graph
print("************* Undirected Graph ********************")
class Graph():

def __init__(self):
self.graph={}


def insert(self,v1,v2,pic):

    if not v1 in self.graph.keys():
        self.graph[v1]=[]
    if not v2 in self.graph.keys():
        self.graph[v2]=[]

    self.graph[v1].append(v2) 

    if pic=="u":
        self.graph[v2].append(v1)


def delete(self,v):
for i in self.graph:
    for j in self.graph[i]:
        if j==v:
            self.graph[i].remove(v)
del self.graph[v]

def find_path(self,start,end,path=[]):

    path= path+[start]
    if start==end:
        return path
    if start not in self.graph.keys():
    return None
    for node in self.graph[start]:
        if node not in path:
            new_path=self.find_path(node,end,path)
    if new_path:
        return new_path
    return None

    def len_path(self,start,end):
        return len(self.find_path(start,end))

g=Graph()


g.insert("v1","v2","u")
g.insert("v1","v6","u")
g.insert("v2","v6","u")
g.insert("v5","v6","u")
g.insert("v3","v6","u")
g.insert("v6","v4","u")
print("\n This is the Undirected Graph -> ",g.graph)
print("\n This is the path -> ",g.find_path("v1","v4"))
print("\n This is the length of path -> ",g.len_path("v1","v4"))

#Directed Graph
print("\n***************** Directed Graph ********************")

class Graph():

def __init__(self):
self.graph={}


def insert(self,v1,v2,pic):

if not v1 in self.graph.keys():
self.graph[v1]=[]
if not v2 in self.graph.keys():
self.graph[v2]=[]

self.graph[v1].append(v2) 

if pic=="u":
self.graph[v2].append(v1)


def delete(self,v):
for i in self.graph:
for j in self.graph[i]:
if j==v:
self.graph[i].remove(v)
del self.graph[v]

def find_path(self,start,end,path=[]):

path= path+[start]
if start==end:
return path
if start not in self.graph.keys():
return []
for node in self.graph[start]:
if node not in path:
new_path=self.find_path(node,end,path)
if new_path:
return new_path
return []
def len_path(self,start,end):
return len(self.find_path(start,end))

dg=Graph()

dg.insert("v1","v2","d")
dg.insert("v5","v1","d")
dg.insert("v5","v2","d")
dg.insert("v4","v5","d")
dg.insert("v4","v2","d")
dg.insert("v3","v4","d")
dg.insert("v3","v2","d")

print("\n This is the Undirected Graph -> ",dg.graph)
print("\n This is the path -> ",dg.find_path("v3","v2"))
print("\n This is the length of path -> ",dg.len_path("v3","v2"))
