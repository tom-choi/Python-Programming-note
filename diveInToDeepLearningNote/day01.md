## 小结

* `pandas`软件包是Python中常用的数据分析工具中，`pandas`可以与张量兼容。
* 用`pandas`处理缺失的数据时，我们可根据情况选择用插值法和删除法。

## 练习

创建包含更多行和列的原始数据集。

1. 删除缺失值最多的列。
2. 将预处理后的数据集转换为张量格式。

# 問題1: 删除缺失值最多的列。
```py
import pandas as pd
import numpy as np

# 建立一個100行10列的資料集
raw_data = pd.DataFrame(np.random.randn(10,10)) 

# 在2,4,7列中加入缺失值
raw_data.iloc[:8,2] = np.nan
raw_data.iloc[5:8,4] = np.nan 
raw_data.iloc[8:,7] = np.nan

# 統計每列的缺失值個數
missing_count = raw_data.isnull().sum()
print(raw_data)
```