def f(u):
    if n + 1 == u:
        # 已经枚举了 n 个数
        # 输出结果
        for i in range(n):
            print(res[i], end = " ")
        print()
    else:
        # 开始枚举第 u 个位置的数
        # 结果要按字典序排列
        # 从小到大遍历 flag[] 依次使用没有使用过的元素
        for i in range(n):
            if flag[i] == False:
                res[u - 1] = i + 1
                flag[i] = True
                
                f(u + 1)
                # 开始枚举第 u + 1 个位置的数
                
                flag[i] = False
                # 回溯恢复现场，将该数字标记为未使用
                # flag[i] 为 False 的所有 i 都可以填在第 u 个位置上
                # 所以要遍历 flag[] 中所有元素
                # 当该位置同时可以填 2, 3 时，填 2 之后枚举下一个位置
                # 填 3 意味着 2 没有填，在填 3 之前将 2 恢复
                # 可以画递归搜索树帮助理解


n = int(input())
res = [0 for i in range(n)]
# 存储结果，长度为 n
flag = [False for i in range(n)]
# 结果由 1 ~ n 组成且不重复，记录该数是否在结果中
f(1)