while True:
    n = int(input())
    if n == 0:
        break
    # 读取数据
    
    s = ["1" for i in range(n)]
    # 对字符串列表声明并初始化
    
    for i in range(n):
        s[i] = list(input())
        s[i].reverse()
        s[i] = "".join(s[i])
    # 1、每一行字符串作为列表中的一个元素读入，同时转换成列表（而不是字符串）
    # 2、将列表逆置（字符串不好操作）
    # 3、将列表转换为字符串
    # 题目所求为字符串后缀，将其逆置后转化为求其前缀
    
    s.sort()
    # 将列表中的字符串排序（排序按照字符串前缀字典序大小进行排序）
    # 字符串排序时，遇到相等字符会比较下一个
    # 如果比完了所有字符，长度短的字符串默认较小
    # "aaa" < "ab" < "abc" < "bsdafdffs" < "z"
    # 所以当排序之后，比较首尾两个即可
    # （1）当首位字符串该位置相同，则所有字符串该位置都相同
    # （2）当首位字符串该位置不相同，则找到了最长 “前缀”
    
    ans = ""
    # 储存结果

    for i in range(len(s[0])):
        if s[0][i] == s[n - 1][i]:
            ans  = "".join(list(ans) + list(s[0][i]))
            # 将相同的部分加入到结果中
            # "+"：只能用于列表的拼接
            # 先转换为列表拼接，再将其转换为字符串
        else:
            break
    
    for i in range(len(ans)):
        print(ans[len(ans) - 1- i], end = "")
        # 倒序输出
    print()