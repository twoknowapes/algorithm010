###### 位运算
* 概念解析
1. 直接对整数的内存中的二进制位进行操作
* 位运算符
1. 左移（<<）
2. 右移（>>）
3. 按位或（|）
4. 按位与（&）
5. 按位取反（~）
6. 按位异或（^）
* 常用操作
1. X & 1 == 1 OR == 0 判断奇偶（x % 2 == 1）
2. X = X & (X - 1) -> 清零最低位的 1
3. X & -X -> 得到最低位的 1
4. X >> 1 -> X/2
5. X & ~X -> 0
* 适用场景
1. 判断奇偶数
2. 交换两个数
3. 取余
4. 生成第一个大于 a 的满足 2^n 的数
5. 求相反数
6. 求绝对值
7. 获取 int 型变量的第 k 位
8. 某个数的二进制里面的 1 的个数
9. 比较两个数的大小
* 实战题目
1. [位 1 的个数](https://leetcode-cn.com/problems/number-of-1-bits/)
2. [2 的幂](https://leetcode-cn.com/problems/power-of-two/)
3. [比特位计算](https://leetcode-cn.com/problems/counting-bits/)
4. [颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)
5. [N 皇后](https://leetcode-cn.com/problems/n-queens/description/)
6. [N 皇后 II](https://leetcode-cn.com/problems/n-queens-ii/description/)
###### [布隆过滤器](https://en.wikipedia.org/wiki/Bloom_filter)
* 概念解析
1. 一个很长的二进制向量和一系列随机映射函数
2. 空间效率和查询时间远远超过一般算法
3. 存在一定的误识别率和删除困难
* 基本实现
1. [位图 + 哈希表](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/)
```
from bitarray import bitarray
import mmh3
import math


class BloomFilter:
    def __init__(self, size, hash_num):
        # Size of bit array to use
        self.size = size
        # Number of hash functions to use
        self.hash_num = hash_num
        # Bit array of given size
        self.bit_array = bitarray(size)
        # Initialize all bits as 0
        self.bit_array.setall(0)
    
    def add(self, item)：
        """
        Add an item in the filter
        """
        digests = []
        for seed in range(self.hash_num):
            digets = mmh3.hash(item, seed) % sef.size
            digets.append(diget)
            
            # Set the bit True in bit_array
            self.bit_array[digets] = 1
    
    def lookup(self, item):
        """
        Check for existence of an item in filter
        """
        for seed in range(self.hash_num):
            digets = mmh3.hash(item, seed) % self.size
            if self.bit_array[digets] == 0:
                return 'Nope'
        return 'Probably'
        
    @classmethod
    def get_size(self, n, p):
        """
        Return the size of bit array(m) to uesd using
        m: number of items expected to be stored filtered
        p: False Positive probability in decimal
        """
        m = -(n * math.log(p)) / (math.log(2） ** 2)
        return int(m)
        
    @calssmethod
    def get_hash_count(self, m, n):
        """
        Return the hash function(k) to be used using
        m: size of bit array
        n: number of items expected to be stored filtered
        """
        k = (m / n) * math.log（2)
        return int(k)
```
2. [其他实现](https://github.com/jhgg/pybloof)
* [适用场景](https://blog.csdn.net/tianyaleixiaowu/article/details/74721877)
1. 垃圾邮件识别
2. 网页去重
3. 缓存穿透
4. 集合判重
5. 查询加速
6. 比特币网络
7. 分布式系统
###### LRU 缓存
* 概念解析
1. [置换算法](https://en.wikipedia.org/wiki/Cache_replacement_policies)
1.1 LRU：Least Recently Used（最近最少使用）
1.2 LFU：Least Frequently Used（最近最不常用）
2. 缓存：一种提高数据读取性能的技术
* 基本实现
1. 基于哈希表 + 双向链表
2. 基于数组
* 适用场景
1. 记忆
2. 钱包 - 储物柜
* 实战题目
1. [LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache/#/)
###### 排序算法
* 排序类型
1. 插入排序（Insertion Sort）
```
def insertionSort(arr):
    """
    1. 从前到后逐步构建有序序列
    2. 对于未排序数据在已排序序列中从后向前扫描以找到相应位置并插入
    3. 设立哨兵
    """
    for i in range(1, len(arr)):
        curr, preI  = arr[i], i
        
        while preI > 0 and arr[preI - 1] > curr:
            arr[preI] = arr[preI - 1]
            preI -= 1
        arr[preI] = curr
    
    return arr
```
2. 希尔排序（Shell's Sort）
```
def sheelSort(arr):
    """
    1. 选择一个增量序列 t1、t2...tk（t > ti）
    2. 按步骤 1 的增量序列对序列进行 K 次排序
    3. 每次排序根据对应的增量 ti 将待排序列分割成若干 m 的子序列
    4. 分别对个子表进行直接插入排序
    """
    gap = len(arr) // 2
    
    while gap:
        for i in range(gap, len(arr)):
            while i - gap >= 0 and arr[i - gap] > arr[i]:
                arr[i - gap], arr[i] = arr[i], arr[i - gap]
                i -= gap
        gap //= 2
            
    return arr
```
3. 选择排序（Selection Sort）
```
def selectionSort(arr):
    """
    1. 在选出最小（或最大）的一个数与第 1 位置的数交换
    2. 然后在剩下的数中再找最小（或最大）与第 2 位置的数交换
    3. 依次类推直到第 n-1 个元素和第 n 个元素比较为止
    """
    for i in range(len(arr)):
        MinI = i
        for j in range(1, i + 1):
            minI = j
            if i != minI:  
                arr[i], arr[minI] = arr[minI], arr[i]
    
    return arr
```
4. [堆排序（Heap Sort）](https://www.geeksforgeeks.org/heap-sort/)
```
def heapify(arr, length, parent_index):
    """
    1. 建堆：数组元素依次建立大顶堆
    2. 排序：依次取堆顶元素并删除
    3. 重复：建堆和排序直到元素只剩下一个
    """
    temp = arr[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        if child_index + 1 < length and arr[child_index + 1] > arr[child_index]:
            child_index = child_index + 1
        if temp > arr[child_index]:
            break
        arr[parent_index] = arr[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1
    arr[parent_index] = temp

def heapSort(arr):
    # Build a max heap
    for i in range((len(arr) -2) // 2, -1, -1):
        heapify(arr, len(arr), i)
    
    # Only by one extact elements
    for j in range(len(arr) - 1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, j, 0)
```
5. 冒泡排序（Bubble Sort）
```
def bubbleSort(arr):
    """
    1. 自上而下对相邻的两个数依次进行比较和调整
    2. 让较大的数下沉、较小的数往上冒
    3. 每当相邻的数比较后与排序要求相反时就将它们互换
    """
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
```
6. 快速排序（Quick Sort）
```
def quickSort(arr, begin, end):
    """
    1. 选择一个基准元素 pivot（通常选择第一个元素或最后一个元素）
    2. 将小意思放 pivot 左边、大元素放 pivot 右边
    3. 依次对左边和右边的子数组继续进行排序
    """
    if begin >= end: return
    
    pivot_index = partition(arr, begin, end)
    quickSort(arr, begin, pivot_index - 1)
    quickSort(arr, pivot_index + 1, end)

def partition(arr, begin, end):
    pivot = arr[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if arr[i] < pivot:
            mark += 1
            arr[mark], arr[i] = att[i], arr[mark]
    arr[begin], arr[mark] = arr[mark], arr[begin]
    return mark
```
7. 归并排序（Merge Sort）
```
def mergeSort(arr):
    """
    1. 把待排序序列分为若干个子序列
    2. 对子序列分别采用归并排序
    3. 将排序号的子序列合并为一个最终的有序序列
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1 
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr
```
8. 桶排序（Bucket Sort）
```
def bucketSort(arr):
    """
    1. 将要排序的数据分到几个有序的桶里
    2. 每个桶里的数据再单独进行排序
    3. 桶内排完序后再把每个桶里的数据按照顺序依次取出
    """
    _min, _max = min(arr), max(arr)
    # 桶大小
    bucketNum = (_max - _min) // len(arr)
    # 桶数组
    bucketList = [[] for _ in range(bucketNum + 1)]
    
    # 向桶数组填数
    for i in arr:
        bucketList[(i - _min) // bucketNum)].append(i)
        arr.clear()
     
    # 向桶数组回填
    for bucket in bucketList:
        for j in sorted(i):
            arr.append(j)

    return arr
```
9. 计数排序（Counting Sort）
```
def countingSort(arr):
    """
    1. 桶排序的一种特殊情况
    2. 当排序的 n 个数据并不大时把数据划分成 k 个桶
    3. 每个桶内的数据值都是相同的
    """
    _min, _max = min(arr), max(arr) 
    temp = [0] * (_max - _min + 1)

    for c in arr:
        temp[c - _min] += 1
    
    j = 0
    for i inrange(len(arr)):
        while temp[j] == 0:
            j += 1
        arr[i] = j + _min
        temp[j] -= 1

    return arr
```
10. 基数排序（Radix Sort）
```
def radixSort(arr):
    """
    1. 按照低位先排序、然后收集
    2. 再按照高位排序、然后收集
    3. 依次类推直到最高位
    """
    _max = max(arr)
    # 最大位数
    maxDigit = len(str(_max))
    bucketList = [[] for _ in range(10)]
    
    # 低位排序
    div, mod = 1, 10
    for i in range(maxDigit):
        for j in nums:
            bucketlist[i % mid // div].append(i)
            div *= 10
            mod *= 10
            
            idx = 0
            for k in range(10):
                for bucket in bucketList[j]:
                    arr[idx] = bucket
                    idx += 1
                bucketList[j] = []

    return arr
```
![df0cdbb73bd19a2d69a52c54d8b9fc0c.jpeg](evernotecid://07AA3624-C509-4A21-989E-ECD0CE405181/appyinxiangcom/28530034/ENResource/p1946)
* 动画效果
1. [十大经典排序算法动图演示](https://www.cnblogs.com/onepixel/p/7674659.html)
2. [九种经典排序算法可视动画](https://www.bilibili.com/video/av25136272)
3. [十五种排序算法的动画展示](https://www.bilibili.com/video/av63851336)
* 排序分析
1. 执行效率
1.1 最好、最坏、平均时间复杂度
1.2 时间复杂度系数、常数、低阶
1.3 比较次数和交换（或移动）次数
2. 内存消耗
3. 稳定性
* 注意要点
1. 排序算法无绝对的优劣
2. 工程上的排序实践
2.1 工程上的排序是综合排序
2.2 数组较小时：插入排序
2.3 数组较大时：快速排序或其他 O(N * logn) 的排序
* 常考面试
1. 按照访问磁石对 10 万条 URL 访问日志进行排序
2. 两个 10 万条字符串数组如何快速找出两个数组中相同的字符串
3. 有两个包含 1 亿行字符串的文件如何快速找出相同的字符串
* 实战题目
1. [数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array/)
2. [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)
3. [合并区间](https://leetcode-cn.com/problems/merge-intervals/)
4. [翻转对](https://leetcode-cn.com/problems/reverse-pairs/)
5. [力扣排行榜](https://leetcode-cn.com/problems/design-a-leaderboard/)