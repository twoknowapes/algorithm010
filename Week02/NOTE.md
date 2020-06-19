# 一维：线性结构
## 非受限线性表
### 散列表
#### 概念解析
* 数组的一种扩展
* 基于数组支持按照下标随机访问数据的特性
* 散列结构
#### 常见操作
* 支持高效的数据插入、删除和查找操作
* 不支持快速顺序遍历散列表中的数据
#### 散列函数
* 基本要求
1. 散列函数计算得到的散列值是一个非负数
2. 如果 key1 = key2：hash(key1) == hash(key2)
3. 如果 key1 ≠ key2：hash(key1) != hash(key2)
* 如何设计
1. 散列函数的设计不能太复杂
2. 散列函数生成的值要尽可能随机且均匀分布
#### 装载因子：填入表中的元素个数 / 散列表的长度
* 装载因子阈值
* 动态扩容策略
#### 冲突解决
* 开放寻址法：数据量比较小、装载因子小
1. 线性探测
2. 二次探测
3. 双重散列
* 链表法：存储大对象、大数据量
#### 实现思路
* 设计一个合适的散列函数
* 定义装载因子阈值并设计动态扩容策略
* 选择合适的散列冲突解决方法
```
# 使用两个列表创建散列表
class HashTable:
    def __init__(self):
        # 指定初始大小（通常选一个素数尽可能提高冲突解决的效率）
        self.size = 11
        # 存储键
        self.slots = [None] * self.size
        # 存储值
        self.data = [None] * self.size
        
    # 散列函数：简单的取余函数
    def hashfunc(self. key, size):
        return key & sizze
        
    # 循环查找是否存在空槽 并确定下一个位置
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
        
    # 往映射中加入有个新的键-值对
    def put(self, key, data):
        hahsval = self.hashfunc(key, len(self.slots))
        
        if self.slots[hashval] == None:
            self.slots[hashval] = key
            self.data[hashval] = data
        else:
            if self.slots[hashval] == key:
                self.data[hahsval] = data
            else:
                nextslot = self.rehash(hashval, len(self.slots))
                while self.slots[nextsolt] != None and self.slots[nextsolt] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                  
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

    # 返回键对应的值
    def get(self, key):
        startslot = self.hashfunc(key, len(slef.slots))
        
        data, stop, found, position = None, False, False, startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
        
    def __getitem__(self, key)：
        return self.get(key)
        
    def __setitem__(self, key, data):
        self.put(key, data)
```
#### 适用场景
* 计数
* LRU 缓存淘汰算法
* Redis 有序集合
#### 实战题目
* [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/)
* [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)
* [两数之和](https://leetcode-cn.com/problems/two-sum/)
* [四数之和](https://leetcode-cn.com/problems/4sum/)
# 二维：非线性结构
![6ebf42641b5f98f912d36f6bf86f6569.jpeg](evernotecid://07AA3624-C509-4A21-989E-ECD0CE405181/appyinxiangcom/28530034/ENResource/p1137)
### 树
#### 概念解析：特殊化的图
* 树是包含 n（n>=0）个结点的有穷集
* 每个元素称为结点
* 有一个特定的结点被称为根结点或树根
* 除根结点外的其余元素被分为 m（m>=0）个互不相交的集合
#### 基本属性
* 树是按层级构建的
* 一个节点的所有子节点与另一个节点的所有子节点无关
* 叶子节点都是独一无二的
#### 相关概念
* 节点的高度
* 节点的深度
* 节点的层数
* 树的高度
### 二叉树
#### 概念解析：每个结点最多有两个子树的树结构
#### 五种形态
* 空二叉树
* 只有根节点二叉树
* 只有左子树
* 只有右子树
* 完全二叉树
#### 存储方式
* 顺序存储法 -> 列表之列表
```
class BinaryTree:
    # 创建一个二叉树实例
    def binaryTree(root):
        return [r, [], []]

    # 新建一个二叉树并将其作为当前节点的左子节点
    def insertLeft(root, newBranch):
        t = root.pop(1)
        if len(t) > 1:
            root.insertLeft(1, [newBranch, t, []])
        else:
            root.insertLeft(1, [newBranch, [], []])
        return root

    # 新建一个二叉树并将其作为当前节点的右子节点
    def insertRight(root, newBranch):
        t = root.pop(2)
        if len(t) > 1:
            root.insertRight(2, [newBranch, [], t])
        else:
            root.insertRight(2, [newBranch, [], []])

    # 在当前节点中存储参数 val 中的对象
    def setRootVal(root, newVal):
        root[0] = newVal

    # 返回当前节点存储的对象
    def getRootVal(root):
        return root[0]

    # 返回当前节点的左子节点所对应的二叉树
    def getLeftChild(root):
        return root[1]

    # 返回当前节点的右子节点所对应的测试
    def getRightChild(root):
        return root[2]
```
* 链式存储法 -> 节点与引用
```
class BinaryTree:
    def __inin__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self, newNode):
        # 没有左子节点则直接创建左子树实例
        if self.leftChild == None:
            sele.leftChild = BinaryTree(newNode)
        # 已存在左子节点则将已有左子节点降一层
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def serRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
```
#### 解析构建
#### 遍历方式
* 广度优先搜索
* 深度优先搜索
```
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.right)
        self.preorder(root.left)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```
#### 常考面试
* 判断一个树是否平衡
* 求二叉树的深度
* 二叉树的递归/非递归遍历
* 二叉树的最大路径和
* 所有路径的给定和
* 二叉树的最低公共父结点
* 求二叉树第 k 层的结点个数
* 树的层次遍历
#### 实战题目
* [二叉树前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
* [二叉树后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
* [二叉树中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
* [二叉树层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description)
* [N 叉树前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)
* [N 叉树后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
* [N 叉树层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)
* [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)
* [二叉树最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)
* [二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
* [路径总和](https://leetcode-cn.com/problems/path-sum/)
### 二叉堆
#### [概念解析](https://en.wikipedia.org/wiki/Heap_%28data_structure%29)
* 一个完全二叉树
1. 除了最底层其他每一层的节点都是满的
2. 在最底层从左往右填充节点
* 每个结点的值都必须大于等于（或小于等于）其子树中每个结点的值
1. 大于等于 -> 大顶堆
2. 小于等于 -> 小顶堆
#### 常见操作
* 堆化：O(n)
1. 从下往上
2. 从上往下
* 插入：O(longn)
1. 新元素一律先插入到堆的尾部
2. 依次从下向上调整整个堆的结构直到堆顶（HeapifyUp）
* 删最：O(logn)/O(1)
1. 将堆尾元素替换到顶部（即对堆顶被替代删除掉）
2. 依次从根向下调整整个堆的结构直到堆尾（HeapifyDown）
* 查最：O(1)
#### 基本实现
* 一般通过数组来实现
* 假设第一个元素在数组中的索引为 0
1. 索引为 i 的左子树的索引为（2 * i + 1）
2. 索引为 i 的右子树的索引为（2 * i + 2）
3. 索引为 i 的父结点的索引为 floor((i - 1) / 2)
```
class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    # 向上移动直到重获对的结构性质
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2
     
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.precUp(self.currentSize)
        
    def percDown(self, i):
        while (i * 2) < self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
            
    def minChild(self, i):
        if i * 2 + 1 >= self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
                
    def delMin(self):
        reval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.precDown(1)
        return reval
        
        
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
```
#### 适用场景
* 堆排序
1. 建堆：数组元素依次建立大顶堆
2. 排序：依次取堆顶元素并删除
3. 重复：建堆和排序直到元素只剩下一个
```
def heapify(arr, n, i):
    ```
    i: index of subtree rooted 
    n: size of heap
    ```
    # Initialize largest as root
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    # Left child of root exists and is greater than root 
    if l < n and arr[i] < arr[l]:
        largest = 1
    
    # Right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        larget = r
    
    # Change root if needed
    if largesst != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Heapify the root
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)
    
    # Only by one extact elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```
* 优先队列
* 求 Top K
* 求中位数
#### 常考面试
* 大文件排序
* 静态数据求中位数 
#### 实战题目
* [数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/)
* [最小的 K 个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)
* [前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)
* [丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)
### 红黑树
#### [二叉搜索树](https://visualgo.net/zh/bst?slide=1)
* 概念解析
1. 左子树上所有节点的值均小于它的根节点的值
2. 右子树上所有节点的值均大于它的根节点的值
3. 依次类推：左右子树也分别为二叉搜索树
* 常见操作
* 基本实现
* 简单分析
#### 平衡二叉树
* 概念解析
1. 左子树和右子树的深度差（平衡因子）的绝对值不超过 1
2. 左右子树也分别为平衡二叉树
* 基本实现
* 性能分析
#### 红黑树
* 概念解析
1. 根节点是黑色的
2. 每个叶子节点都是黑色的空节点（NIL）
3. 任何相邻的阶段都不能同时为红色
4. 每个节点到达其可达叶子节点的所有路径都包含相同数目的黑色节点
* 实现技巧
1. 把红黑树的平衡调整的过程比作魔方复原
2. 找准关注节点：不要搞丢、搞错关注节点
3. 插入操作的平衡调整比较简单而删除操作就比较复杂
* 适用场景
1. 解决普通二叉树在频繁插入、删除等动态更新操作时时间复杂度退化问题
2. 实际工程中更倾向用跳表来替代
* 实战题目
1. [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)
2. [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
### 递归树
#### 概念解析
* 递归树是迭代计算的模型
* 递归树的生成过程与迭代过程一致
* 递归树上所有项恰好是迭代后产生和式中的项
* 对递归树上的项求和就是迭代后方程的解
#### 生成规则
* 初始：递归树只有根节点（W(n)）
* 不断将函数项叶节点的迭代式（W(m)）表示成二层子树并替换该叶节点
* 继续递归树的生成直至树中无函数项（只有初值）为止
#### 适用场景
* 分析快速排序的时间复杂度
* 分析斐波那契数列的时间复杂度
* 分析全排列的时间复杂度
### 字典树
#### 概念解析
* 节点本身不存在完整单词
* 从根节点到某一节点路径经过的字符串连接起来为该节点对应的字符串
* 每个节点的所有子节点路径代表的字符都不相同
#### 适用场景
* 统计和排序大量的字符串
* 搜索引擎词频统计及关键字提醒
#### 实战题目
* [实现 Trie](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)
* [单词搜索](https://leetcode-cn.com/problems/word-search/)
* [单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)
### 并查集
#### 概念解析
* 一种树型数据结构在使用中以森林来表示
* 用于处理不交集的合并及查询问题
#### 常见操作
* 初始化：把每个点所在的集合测试为其自身 -> O(n)
* 合并：将两个元素所在的集合合并为一个集合 -> 建立关系
* 查找：查找元素所在集合（即根节点）
#### 优化方式
* 将 rank 浅的合并到 rank 深的
* 路径压缩
#### 适用场景
* 帮派识别：小弟 -> 老大
* 组团配对
#### 实战题目
* [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
* [朋友圈](https://leetcode-cn.com/problems/friend-circles/)
* [被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)
### 图
#### 概念解析：由顶点的有穷非空集合和顶点之间边的集合组成：G(V, E)
* G（Graph）：表示一个图
* V（Vertex）：图 G 中的顶点的集合
1. 度：入度和出度
2. 点与点之间：连通与否
* E（Edge）：图 G 中边的集合
1. 有向和无向（单行线）
2. 权重（边长）
#### 图的类型
* 无向图
* 有向图
* 完全图
#### 图的存储
* 邻接矩阵 -> 很多条边
* 邻接表 -> 稀疏连接
```
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
```
#### 适用场景
* 微信等社交网络中的好友关系
* 地图导航及交通网络
* 游戏地图与迷宫
* 计算机网络
* 人际关系推荐系统
* 知识图谱
#### 高级算法
* [拓扑排序（Topological Sorting）](https://zhuanlan.zhihu.com/p/34871092)
* 强连通分量
* [最短路径（Shortest Path）](https://www.bilibili.com/video/av25829980?from=search&seid=13391343514095937158)
* [最小生成树（Minimum Spanning Tree）](https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051)