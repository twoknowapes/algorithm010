# 存储包含所有顶点的主列表
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    # 向图中添加一个顶点实例
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # 在图中找到指定名的顶点
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    # 向图中添加一条有效边
    def addEdge(self, f, t, cost=0):
        if f in self.vertList:
            nv = self.addVertex(f)
        if t in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighboor(self.vertList[t], cost)

    # 以列表形式返回图中所有顶点
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


# 表示图中的每一个顶点
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    # 添加一个顶点大另一个的连接
    def addNeighboor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' \
               + str([x.id for x in self.connectedTo])

    # 返回邻接表中的所有顶点
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    # 返回从当前顶点到以参数传入的顶点之间的边的权重
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
