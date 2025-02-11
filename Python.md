1. ```python
   input()
   # 会将输入的转换成字符串（所以需要强制转换成 int 与 float）
   # 输入不以空格中断，而是以换行中断
   
   a, b = map(int, input().split())
   # 读取两数，以空格划分，然后将其转换为 int
   
   numbers = list(map(int, input().split()))
   print(numbers) 
   # 读取列表（一维数组）
   # list()：将其转换为列表
   
   matrix = []
   for i in range(3):
       row = list(map(int, input().split()))
       matrix.append(row)
   # 读取矩阵（二维数组 = 一维数组的一维数组）
   # 将 row 当作是一个元素加在最后即可
   # matrix[1][1] 可以正常使用
   ```

2. ```python
   a = [[]]
   # 二维列表（1）
   # 只进行了列表的声明，并没有初始化
   # 所以进行 a[0][0] = 1 这样的操作是错误的
   
   a = [[0 for i in range(m)] for j in range(n)]
   # 二维列表（2）
   # 二维数组 n 行 m 列（注意顺序）
   # 声明列表的同时进行了初始化，所以可以直接赋值
   ```

3. ```python
   a = [0, 1, 2, 3, 4, 5]
   a[1:4] = [1, 2]
   # a = [0, 1, 2, 4, 5]
   # 将 1 ~ 3 的元素替换成了 1 和 2
   # 所以 a[1:4] = [] 可以实现列表的删除
   ```

4. ```python
   a = [0, 1, 2, 3, 4]
   
   b = a
   # 深拷贝
   
   b = a[:]
   # 浅拷贝
   ```

5. ```python
   length = len(a) 
   # 返回列表长度
   
   a.append(x) 
   # 在列表末尾添加一个新元素 x
   
   a.pop() 
   # 删除列表的最后一个元素
   
   a.reverse() 
   # 将整个列表翻转
   
   b = a[::-1]
   # 返回一个逆序的新列表
   
   a.sort() 
   # 将整个列表从小到大排序
   ```

6. ```python
   a = [60]
   # 表示 a 的长度为 1，值为 60
   
   a = [60] * 60
   # 表示 a 的长度为 60，每个值都为 60
   ```

7. ```python
   for i in reversed(range(begin, ending)):
   # 倒序
   ```