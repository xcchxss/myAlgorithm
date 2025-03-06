import bisect
# 导入用于二分搜索的包 bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort()
C = list(map(int, input().split()))
C.sort()
# 读入数据并初始化，排好序方便后续操作

res = 0
for i in range(N):
    flag = B[i]
    ans1 = bisect.bisect_left(A, flag)
    ans2 = bisect.bisect_right(C, flag)
    res = res + ans1 * (N - ans2)
    # 1、枚举 B 中元素的所有值，记作 flag
    # 2、在 A 中查找 flag 并返回下标，对应着比 B 小的元素数量
    # 3、在 C 中查找 flag 并返回下标，对应着比 B 大的元素数量

print(res)