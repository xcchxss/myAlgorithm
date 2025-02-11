### 题目描述

![](https://raw.githubusercontent.com/xcchxss/myAlgorithm/refs/heads/main/python_files/AcWing/%E6%A8%A1%E6%8B%9F/756_%E8%9B%87%E5%BD%A2%E7%9F%A9%E9%98%B5/756_%E8%9B%87%E5%BD%A2%E7%9F%A9%E9%98%B5.bmp)

### 方法技巧

### 详细代码

```python
n, m = map(int, input().split())
# 读入要求矩阵的行与列

ans = [[0 for i in range(m)] for j in range(n)]
# 蛇形矩阵 ans（注意先列（m）后行（n））
# 初始值默认为 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 偏移量矩阵 dx 与 dy
# 对应着四个不同的方向：右 -> 下 -> 左 -> 上 -> 右

num = 1
x = y = 0
i = 0
# num：蛇形矩阵 ans 中的所有数字
# x y：初始坐标
# i：移动方向，初始移动方向为向右，所以 i = 0

while num <= n * m:
# 矩阵填满之后退出

    ans[x][y] = num
    num = num + 1
    # 填入矩阵，数字加一

    a = x + dx[i]
    b = y + dy[i]
    # a b 为 x y 沿 i 方向移动后得到的新坐标

    if a < 0 or a >= n or b < 0 or b >= m or ans[a][b]:
        i = (i + 1) % 4
        a = x + dx[i]
        b = y + dy[i]
    # 判断新坐标是否合理（超出边界、填过数字）
    # 新坐标无效 -> 换下一个方向再次移动
    # 此时得到的新坐标 a b 一定合理
    # 唯一不合理的情况也即矩阵填满了，会随即退出循环

    x = a
    y = b
    # 更新 x y 坐标
    # 判断是否填满，没填满再去填入数字

for i in range(n):
    for j in range(m):
        print(ans[i][j], end = " ")
    print()
# 循环打印蛇形矩阵
```