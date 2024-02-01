## 小结

* 微分和积分是微积分的两个分支，前者可以应用于深度学习中的优化问题。
* 导数可以被解释为函数相对于其变量的瞬时变化率，它也是函数曲线的切线的斜率。
* 梯度是一个向量，其分量是多变量函数相对于其所有变量的偏导数。
* 链式法则使我们能够微分复合函数。

## 练习

1. 绘制函数$y = f(x) = x^3 - \frac{1}{x}$和其在$x = 1$处切线的图像。
1. 求函数$f(\mathbf{x}) = 3x_1^2 + 5e^{x_2}$的梯度。
1. 函数$f(\mathbf{x}) = \|\mathbf{x}\|_2$的梯度是什么？
1. 你可以写出函数$u = f(x, y, z)$，其中$x = x(a, b)$，$y = y(a, b)$，$z = z(a, b)$的链式法则吗?

# Question 1

```py
%matplotlib inline
# Question 1
x = np.arange(0, 3, 0.1)
# y-f(a)=f'(a)(x-a)
# y = f'(a)(x-a) + f(a)
# y = f'(1)(x-1) + f(1)
# y = 4x-4   
plot(x, [x**3-1/x, 4*x-4], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
```

# Question 2
$$
\nabla_{\mathbf{x}} f(\mathbf{x}) = 
\bigg[\frac{\partial f(\mathbf{x})}{\partial x_1}, \frac{\partial f(\mathbf{x})}{\partial x_2}\bigg] = (6x_1,5e^{x_2})
$$

# Question 3
$$
\nabla_{\mathbf{x}} \frac{\partial||b||^2}{\partial b} = 
\bigg[\frac{\partial \sum{}{} b_i^2}{\partial b_1}, \frac{\partial \sum{}{} b_i^2}{\partial b_2}, \ldots,\frac{\partial \sum{}{} b_i^2}{\partial b_m}\bigg] \\
= [2b_1, 2b_2, \ldots, 2b_m] \\
= 2b^T
$$

# Question 4
$$
u = f(x,y,z) ,x = x(a,b),y =y(a,b) \\
\frac{df}{da} = \frac{df}{dx}\frac{dx}{da} + \frac{df}{dy}\frac{dy}{da} + \frac{df}{dz}\frac{dz}{da}\\
\frac{df}{db} = \frac{df}{dx}\frac{dx}{db} + \frac{df}{dy}\frac{dy}{db} + \frac{df}{dz}\frac{dz}{db}
$$