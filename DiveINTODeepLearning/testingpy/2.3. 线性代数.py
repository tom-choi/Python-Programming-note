import torch

x = torch.tensor(3.0)
y = torch.tensor(2.0)

print(x + y)
print(x * y)
print(x / y)
print(x**y)

# 向量
x = torch.arange(4)
print(x)

# 与普通的Python数组一样，我们可以通过调用Python的内置len()函数
print(len(x))

print(x.shape)

# 矩阵
A = torch.arange(20).reshape(5, 4)
print(A)

# 我们用来表示矩阵的转置
print(A.T)

# 作为方阵的一种特殊类型，对称矩阵（symmetric matrix）等于其转置：
B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B)

print(B == B.T)

# 当我们开始处理图像时，张量将变得更加重要，图像以维数组形式出现， 
# 其中3个轴对应于高度、宽度，以及一个通道（channel）轴， 
# 用于表示颜色通道（红色、绿色和蓝色）
X = torch.arange(24).reshape(2, 3, 4)
print(X)

# 标量、向量、矩阵和任意数量轴的张量（本小节中的“张量”指代数对象）有一些实用的属性。 
# 例如，你可能已经从按元素操作的定义中注意到，
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()  # 通过分配新内存，将A的一个副本分配给B
print(A, A + B)
# Hadamard积
print(A * B)
# 将张量乘以或加上一个标量不会改变张量的形状，
# 其中张量的每个元素都将与标量相加或相乘。
a = 2
X = torch.arange(24).reshape(2, 3, 4)
print(a + X, (a * X).shape)

# 降维
x = torch.arange(4, dtype=torch.float32)
print(x, x.sum())

# 例如，矩阵中元素的和可以记
print(A.shape, A.sum())

# 由于输入矩阵沿0轴降维以生成输出向量，因此输入轴0的维数在输出形状中消失。
A_sum_axis0 = A.sum(axis=0)
print(A_sum_axis0, A_sum_axis0.shape)
# 默认情况下，调用求和函数会沿所有的轴降低张量的维度，使它变为一个标量。
# 我们还可以指定张量沿哪一个轴来通过求和降低维度。
A_sum_axis1 = A.sum(axis=1)
print(A_sum_axis1, A_sum_axis1.shape)
# 指定axis=1将通过汇总所有列的元素降维（轴1）。因此，输入轴1的维数在输出形状中消失。
A_sum_axis1 = A.sum(axis=1)
print(A_sum_axis1, A_sum_axis1.shape)

# 沿着行和列对矩阵求和，等价于对矩阵的所有元素进行求和。
A.sum(axis=[0, 1])  # SameasA.sum()

# 平均值
print(A.mean(), A.sum() / A.numel())

# 同样，计算平均值的函数也可以沿指定轴降低张量的维度
print(A.mean(axis=0), A.sum(axis=0) / A.shape[0])

# 非降维求和
# 但是，有时在调用函数来计算总和或均值时保持轴数不变会很有用。
sum_A = A.sum(axis=1, keepdims=True)
print(sum_A)
print(A / sum_A)
print(A.cumsum(axis=0))

# 点积（Dot Product）
# 我们已经学习了按元素操作、求和及平均值。 另一个最基本的操作之一是点积。
y = torch.ones(4, dtype = torch.float32)
print(x, y, torch.dot(x, y))
print(torch.sum(x * y))

# 矩阵-向量积
print(A.shape, x.shape, torch.mv(A, x))

# 矩阵-矩阵乘法
B = torch.ones(4, 3)
print(torch.mm(A, B))

# L2范数
u = torch.tensor([3.0, -4.0])
print(torch.norm(u))

# L1范数: 我们将绝对值函数和按元素求和组合起来。
print(torch.abs(u).sum())

# Frobenius范数满足向量范数的所有性质，它就像是矩阵形向量的L2范数。
# 调用以下函数将计算矩阵的Frobenius范数。
print(torch.norm(torch.ones((4, 9))))

X = torch.arange(24).reshape(2, 3, 4)
print(len(X))

# The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 1
# print(A/A.sum(axis=1))