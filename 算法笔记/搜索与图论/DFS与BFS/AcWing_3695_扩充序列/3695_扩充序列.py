def f(u, k):
    # u：扩充第 u 次
    # k：第 k 个数字

    if k > 2 ** u:
        return f(u - 1, 2 ** (u + 1) - k)
        # 位于右侧：对称到上一轮的位置

    elif k == 2 ** u:
        return u + 1
        # 位于中间：直接返回结果

    else:
        return f(u - 1, k)
        # 位于左侧：上一轮的相同位置


n, k = map(int, input().split())
# 读取需要扩充 n - 1 次与第 k 个数字

# 递归调用
res = f(n - 1, k)
print(res)