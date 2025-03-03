# 读取数据
n = int(input())
arr = list(map(int, input().split()))

# 使用字典记录各个数字出现的次数
res = dict()
for i in range(n):
    if arr[i] not in res:
        res[arr[i]] = 0
    res[arr[i]] += 1

# 将字典 res 按照 value 降序，key 升序排列
# 返回列表
res = sorted(res.items(), key = lambda x: (-x[1], x[0]))

# sorted 可以按照 key 排序任意维数组与字典
# res.items() 是由 key 与 value 组成的元组
# 只能对可迭代对象排序

# 输出结果
for k, v in res:
    print(k ,v)