###### 动态规划
* 概念解析
1. 运筹学方法
2. 在多轮决策过程中的最优方法
3. 每次决策依赖于当前状态
* 基本实现
1. 最优子结构：opt[n] = best_of(opt[n-1), ...)
1.1 递归的定义最优解（递推：递归 + 记忆化）
1.2 以自底向上或自顶向下的记忆方式计算出最优解
1.3 根据计算最优解时得到的信息构造问题的最优解
2. 定义状态：opt[n]（最关键步骤）
3. 状态转移方程
3.1 opt[i] = opt[n-1] + opt[n-2]
3.2 opt[i,j] = opt[i+1][j] + opt[i][j+1]（a[i,j] 是否为空）
```
# 状态定义
dp = ...

# 初始状态
dp[0][0] = i
dp[0][1] = j
...

# DP 状态的推导
for i in ...
    for j in ...
        d[i][j] = ...
        
# 最优解
return dp[m][n]
```
* 适用场景
1. 一个模型：多阶段决策最优解模型
2. 三个特征
2.1 最优子结构
2.2 无后效性
2.3 重复子问题
* 常考面试
1. 背包问题
2. 计算两个字符串的相似度
3. 最长公共子串长度
4. 求最长递增子序列
5. 最小编辑距离
6. 爬楼梯
7. 连续子数组的最大和
8. 最长回文子串
* 实战题目
1. [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)
2. [不同路径](https://leetcode-cn.com/problems/unique-paths/)
3. [不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/submissions/)
4. [不同路径 III](https://leetcode-cn.com/problems/unique-paths-iii/)
5. [零钱兑换](https://leetcode-cn.com/problems/coin-change/)
6. [零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/)
7. [三角形最小路径和](https://leetcode-cn.com/problems/triangle/)
8. [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
9. [编辑距离](https://leetcode-cn.com/problems/edit-distance/)
10. [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)
11. [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
12. [打家劫舍](https://leetcode-cn.com/problems/house-robber/)
13. [打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/description/)
14. [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
15. [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
16. [买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
17. [买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)
18. [最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
19. [买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)