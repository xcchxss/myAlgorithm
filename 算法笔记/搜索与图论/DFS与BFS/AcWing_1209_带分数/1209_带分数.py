def f(u):
    global ans
    # 将最终结果 ans 设置为全局变量
    # 递归时尤其注意
    
    if u == 9:
        # 全排列枚举完毕之后，进行分段
        # 设置两个哨兵 i 与 j
        for i in range(len(res)):
            for j in range(i + 2, len(res)):
                
                a = 0
                for k in range(0, i + 1):
                    a = 10 * a + res[k]
                # a 从第 0 个元素到第 i 个元素
                
                b = 0
                for k in range(i + 1, j):
                    b = 10 * b + res[k]
                # b 从第 i + 1 个元素到第 j - 1 个元素
                # j 枚举的起点为 i + 2
                # 所以 i + 1 到 j - 1 中至少会有一个元素
                
                c = 0
                for k in range(j, len(res)):
                    c = 10 * c + res[k]
                # c 从第 j 个元素到第 len(res) - 1 个元素
                
                if n == a + b / c:
                    ans = ans + 1
    else:
        for i in range(len(flag)):
            if flag[i] == False:
                flag[i] = True
                res[u] = i + 1
                f(u + 1)
                flag[i] = False


n = int(input())
ans = 0
flag = [False] * 9
res = [0] * 9

f(0)
# 对 9 个数字进行全排列，然后进行分段

print(ans)