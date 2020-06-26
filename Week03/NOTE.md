###### Recursion：Divder & Conquer/Backtrace
* 概念解析
* 基本实现
1. 一个问题的解可以分解为几个子问题的解
2. 这个问题与分解后的子问题求解思路完全一致
3. 存在递归终止条件
```
def recursion(level, param1, param2, ...):
    # recursion terminator（递归终止条件）
    if level > MAX_LEVEL:
        print_result
        # process result
        return
        
    # process logic in current level（处理当前层逻辑）
    process_data(level, data...)
    
    # drill down（下探到下一层）
    self.recursion(level + 1, p1, ...)
    
    # reverse the current level status if needed（清理当前层）
    reverse_state(level)
```
* 思维要点
1. 抵制人肉递归
2. 找最近重复性
3. 数学归纳法思维
* 注意要点
1. 堆栈溢出 -> 限制递归调用的最大深度
2. 重复计算 -> 缓存
* 适用场景
1. 汉诺塔问题
2. 斐波拉契数列
3. 阶乘问题
4. 数组的全排列
* 实战题目
1. [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
2. [组合](https://leetcode-cn.com/problems/combinations/)
##### 四大思想
###### 分治算法
* 概念解析
1. 核心思想：分而治之
2. 定义类似于递归且一般适合用递归来实现
* 基本实现
1. 分解：将原问题分解成一系列子问题且不能有重复子问题
2. 解决：递归地求解各个子问题
3. 合并：将子问题的结果合并成原问题
```
def divide_conquuer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return
        
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
   
    # conquer subproblems
    subres1 = self.divide_conquer(subproblem[0], p1, ...)
    subres2 = self.divide_conquer(subproblem[1], p1, ...)
    subres3 = self.divide_conquer(subproblem[2], p1, ...)
    ...
    
    # process and generate the final result
    res = process_result(subres1, subres2, subres3, ...)
    
    # revert the current level states
```
* 适用场景
1. 海量数据处理
2. 在算法设计过程中降低求解问题的时间
* 常考面试
1. 二分查找
2. 大整数乘法
3. 合并排序
4. 快速排序
5. 棋盘覆盖
6. 求出一组数据的有序对个数或逆序对个数
7. 二维平面上有 N 点的两个距离最近的点对
8. 如何快速求解两个矩阵的乘积 C = A * B
* 实战题目
1. [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)
2. [子集](https://leetcode-cn.com/problems/subsets/)
3. [多数元素](https://leetcode-cn.com/problems/majority-element/)
###### 回溯算法
* 概念解析
1. 本质上是：暴力枚举（重复计算）
2. 用来解决广义的搜索问题且适合用递归来实现
* 基本实现
1. 针对所给问题定义问题的解空间（至少含问题的一个（最优）解）
2. 确定易于搜索的解空间结构
3. 以深度优先方式搜索解空间同时使用剪枝函数避免无效搜索
3.1 约束函数：在扩展节点处减去不满足约束的子数
3.2 限界函数：减去得不到最优解的子树
* 适用场景
1. 一看就不需找：小规模数据
2. 搜索范围过大：缺乏规律或还不了解其规律的场景
* 常考面试
1. 深度优先搜索
2. 数独
3. 八皇后问题
4. 0-1 背包
5. 图的着色
6. 旅行商问题
7. 全排列问题
8. 正则表达式
9. 编译原理的语法分析
* 实战题目
1. [N 皇后](https://leetcode-cn.com/problems/n-queens/)
2. [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)
3. [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)
4. [全排列](https://leetcode-cn.com/problems/permutations/)
5. [全排列 II](https://leetcode-cn.com/problems/permutations-ii/)