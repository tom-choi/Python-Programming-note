# 2.1. 数据操作
import torch
# 我们可以使用 arange 创建一个行向量 x
x = torch.arange(12)
print(x)
# 可以通过张量的shape属性来访问张量（沿每个轴的长度）的形状 。
print(x.shape)
# 如果只想知道张量中元素的总数，即形状的所有元素乘积，
# 可以检查它的大小（size）。 
# 因为这里在处理的是一个向量，所以它的shape与它的size相同。
x.numel()
# 要想改变一个张量的形状而不改变元素数量和元素值，可以调用reshape函数。
a = x.reshape(3, 4)
print(a)
# 有时，我们希望使用全0、全1、其他常量
b = torch.zeros((2, 3, 4))
print(b)
c = torch.ones((2, 3, 4))
print(c)
# 隨機值
d = torch.randn(3, 4)
print(d)
# 我们还可以通过提供包含数值的Python列表（或嵌套列表），来为所需张量中的每个元素赋予确定值。
e = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(e)
# 运算符
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
x + y, x - y, x * y, x / y, x ** y  # **运算符是求幂运算
# e
f = torch.exp(x)
# 我们也可以把多个张量连结（concatenate）在一起， 把它们端对端地叠起来形成一个更大的张量。
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
a = torch.cat((X, Y), dim=0)
b = torch.cat((X, Y), dim=1)
# 有时，我们想通过逻辑运算符构建二元张量。 以X == Y为例
# 对于每个位置，如果X和Y在该位置相等，则新张量中相应项的值为1。 
# 这意味着逻辑语句X == Y在该位置处为真，否则该位置为0。
istrue = (X == Y)

# 在上面的部分中，我们看到了如何在相同形状的两个张量上执行按元素操作。
# 在某些情况下，即使形状不同，我们仍然可以通过调用 广播机制（broadcasting mechanism）来执行按元素操作
a = torch.arange(3).reshape(3, 1)
b = torch.arange(2).reshape(1, 2)
print(a, b)
print(a + b)
# 如下所示，我们可以用[-1]选择最后一个元素，可以用[1:3]选择第二个和第三个元素：
print(X[-1], X[1:3])
# 除读取外，我们还可以通过指定索引来将元素写入矩阵。
X[1, 2] = 9
print(X)
# 如果我们想为多个元素赋值相同的值，我们只需要索引所有元素，然后为它们赋值。 
# 例如，[0:2, :]访问第1行和第2行，其中“:”代表沿轴1（列）的所有元素。 
# 虽然我们讨论的是矩阵的索引，但这也适用于向量和超过2个维度的张量。
X[0:2, :] = 12
print(X)
# 节省内存
# 运行一些操作可能会导致为新结果分配内存。
# 例如，如果我们用Y = X + Y，我们将取消引用Y指向的张量，而是指向新分配的内存处的张量。
before = id(Y)
Y = Y + X
print(id(Y) == before)
# 这可能是不可取的，原因有两个：首先，我们不想总是不必要地分配内存。 
# 在机器学习中，我们可能有数百兆的参数，并且在一秒内多次更新所有参数。 
# 幸运的是，执行原地操作非常简单。 
Z = torch.zeros_like(Y)
print('id(Z):', id(Z))
Z[:] = X + Y
print('id(Z):', id(Z))
# 如果在后续计算中没有重复使用X， 
# 我们也可以使用X[:] = X + Y或X += Y来减少操作的内存开销
before = id(X)
X += Y
id(X) == before
# 转换为其他Python对象
A = X.numpy()
B = torch.tensor(A)
print(type(A), type(B))
a = torch.tensor([3.5])
print(a, a.item(), float(a), int(a))
print(istrue)
istrue = (X > Y)
print(istrue)