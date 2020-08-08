###### 字符串匹配
* [概念解析](https://lemire.me/blog/2017/07/07/are-your-strings-immutable/)
1. 字符串的逻辑结构与线性表极为相似
2. 区别仅在于串的数据对象约束为字符集
* 存储结构
1. 顺序存储
2. 链式存储
* 常见操作
1. 增：O(n)/特殊 O(1)
2. 删：O(n)/特殊 O(1)
3. 查
* 单模式算法
1. BF 算法
2. RK 算法
3. [BM 算法](https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
4. [KMP 算法](https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171)
5. [Sunday 算法](https://blog.csdn.net/u012505432/article/details/52210975)
* 多模式算法
1. Trie 树
2. AC 自动机
* 常考面试
1. 回文子串
2. 字符串分割成子串且子串都是回文串
3. 在字典中查找某串
4. 实现 Trie 树
5. 各种动态规划
* 实战题目
1. [转换成小写字母](https://leetcode-cn.com/problems/to-lower-case/)
2. [最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)
3. [宝石与石头](https://leetcode-cn.com/problems/jewels-and-stones/)
4. [字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)
5. [字符串转换整数](https://leetcode-cn.com/problems/string-to-integer-atoi/)
6. [最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/description/)
7. [反转字符串](https://leetcode-cn.com/problems/reverse-string/)
8. [反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii/)
9. [翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)
10. [反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)
11. [仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters/)
12. [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)
13. [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)
14. [找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)
15. [验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)
16. [验证回文字符串 II](https://leetcode-cn.com/problems/valid-palindrome-ii/)
17. [最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)
18. [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
19. [编辑距离](https://leetcode-cn.com/problems/edit-distance/)
20. [正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)
21. [通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/)
22. [不同的子序列](https://leetcode-cn.com/problems/wildcard-matching/)