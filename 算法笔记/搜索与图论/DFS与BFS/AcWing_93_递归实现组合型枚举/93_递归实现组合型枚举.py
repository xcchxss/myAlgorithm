# u：枚举第 u 个位置
# d：从数字 d 开始枚举
def f(u, d):
    if u == m:
        for i in range(u):
            print(ans[i] + 1, end = " ")
            # 从 0 开始，所以需要加 1
        print()
    # 递归终点，打印输出
    else:
        for i in range(d, n):
        # 从 d 开始，到 n - 1
        # 第 u 个位置的起点是由 u - 1 个位置的起点决定的
            if flag[i] == False:
                flag[i] = True
                ans[u] = i
                f(u + 1, i + 1)
                # 递归下一个位置，从 i + 1 开始枚举
                flag[i] = False
                # 回溯，尝试其他枚举方法


n, m = map(int, input().split())
ans = [0] * m
flag = [False] * n
# ans：存储最终结果
# flag：判断数字是否使用过

f(0, 0)