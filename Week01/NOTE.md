# 一维：线性结构
## 非受限线性表
### 数组
#### 概念解析
* 数组中所有元素类型必须相同
* 数组的最大长度必须在定义时给出
* 数组使用的内存空间必须连续（顺序结构）
#### 常见操作
* 增：在最后插入 O(1)/在中间某处 O(n)
* 删：O(n)
* 查：按索引查找 O(1)/特定的查找 O(n)
#### 注意要点
* 数据越界问题
* 多维数组
* 学习高级语言的容器
#### 优化方向
* 数组有序：二分查找
* 数组无序：Hash 帮助统计
#### 应用场景
* 数据数量确定
* 较少甚至不需要进行新增或删除
#### 常考面试
* 数组的查找最大值/最小值/给定值/重复值
* 数组的排序
* 多个数组的排序/合并/求交集/求并集
#### 实战题目
* [盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)
* [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
* [加一](https://leetcode-cn.com/problems/plus-one/)
* [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)
* [旋转数组](https://leetcode-cn.com/problems/rotate-array/)
* [移动零](https://leetcode-cn.com/problems/move-zeroes/)
### 链表
#### 概念解析
* 若干数据元素的有限序列
* 一个结点存储一条数据
1. 第一是具体的数据值
2. 第二是指向下一个结点的指针
* 链表使用的内存空间必须离散（链式结构）
#### 链表类型
* 单向链表
* 循环链表
* 双向链表
* 双向循环链表
* 静态链表
* 跳表：升维思想 + 空间换时间
#### 常见操作
* 增：O(1)
* 删：O(1)
* 查：O(n)
#### 实现技巧
* 技巧一：理解指针或引用的含义
* 技巧二：警惕指针丢失和内存泄漏
* 技巧三：利用哨兵简化实现难度
* 技巧四：重点留意边界条件处理
* 技巧五：举例画图 辅助思考
* 技巧六：多写多练 没有捷径
#### 应用场景
* 数据的元素个数不确定
* 需要经常进行新增或删除
#### 常考面试
* 从尾到头打印单链表
* 单链表实现约瑟夫环
* 逆置/反转单链表
* K 个节点为一组进行翻转
* 返回链表中间节点
* 单链表的排序
* 查找单链表的中间节点
* 查找单链表的倒数第 K 个节点
* 删除链表的倒数第 K 个结点
* 判断单链表是否有环
* 判断两个链表是否相交
* 求两个已排序单链表中相同的数据
* 合并两个有序链表且合并后依然有序
#### 实战题目
* [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
* [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
* [K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)
* [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
* [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
* [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)
## 受限线性表
### 栈
#### 概念解析
* 受限线性表：先进后出
* 只能在表尾新增删除数据
1. top -> 栈顶
2. bottom -> 栈底
#### 常见操作
* 入栈 push()：O(1)
* 出栈 pop()：O(1)
* 取栈顶元素 top() 或 peek()：O(1)
#### 栈的实现
* 顺序栈：支持动态扩容
* 链表栈
#### 适用场景
* 函数调用栈
* 编译器利用栈实现表达式求值
* 浏览器的前进后退概念使用栈
* 最近相关性或先进后出
#### 常考面试
* 实现一个栈
* 使用两个站实现一个队列
* 不借助额外空间实现栈的逆序
* 实现共享栈
* 括号的匹配问题
#### 实战题目
* [最小栈](https://leetcode-cn.com/problems/min-stack/)
* [用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/)
* [有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)
* [最长的有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)
* [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
* [逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)
* [接雨水](https://leetcode-cn.com/problems/trapping-rain-water/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)
### 队列
#### 概念解析
* 受限线性表：先进先出
* 只能在一端新增删除数据
1. front --> 队头
2. rear --> 队尾
3. flag --> 标记变量标记队列是否为满
#### 常见操作
* 入队 enqueue()：O(1)
* 出队 dequeue()：O(1)
#### 队列实现
* 顺序队列
* 链式队列
#### 队列类型
* 普通队列
* 双端队列
* 循环队列
* 阻塞队列
* 并发队列
* 阻塞并发队列
* 优先级队列
#### 常考面试
* 使用两个队列实现一个栈
* BFS 使用队列
* 滑动窗口
#### 实战题目
* [用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/)
* [设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)
* [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)