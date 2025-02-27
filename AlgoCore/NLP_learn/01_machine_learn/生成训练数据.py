import pandas as pd
import numpy as np
#
# # 设置随机种子，保证结果可重复
# np.random.seed(42)
#
# # 数据量
# data_size = 200
#
# # 生成特征
# # 面积（100 ~ 500 平方英尺，正相关）
# area = np.random.randint(100, 501, size=data_size)
#
# # 房龄（0 ~ 50 年，负相关）
# age = np.random.randint(0, 51, size=data_size)
#
# # 距离地铁（100 ~ 3000 米，负相关）
# distance_to_subway = np.random.randint(100, 3001, size=data_size)
#
# # 生成房价
# # 假设公式：价格 = 面积 * 0.3 - 房龄 * 0.5 - 距离 * 0.02 + 噪声
# price = (
#     area * 0.3  # 面积增加价格
#     - age * 0.5  # 房龄增加降低价格
#     - distance_to_subway * 0.02  # 距地铁远降低价格
#     + np.random.normal(0, 5, size=data_size)  # 添加随机噪声
# )
#
# # 确保价格为正值
# price = np.maximum(price, 1)
#
# # 构建数据集
# data = pd.DataFrame({
#     "Area (sq ft)": area,
#     "Age (years)": age,
#     "Distance to Subway (m)": distance_to_subway,
#     "Price (10k RMB)": np.round(price, 2)  # 保留两位小数
# })
#
# # 保存为 Excel 文件
# excel_file = "/mnt/data/correlated_housing_data.xlsx"
# data.to_excel(excel_file, index=False, encoding="utf-8")
# excel_file

# 保证数据的一致性
np.random.seed(42)

data_size = 200
# 生成特征
# 面积
area = np.random.randint(100, 500, size=200)

# 房龄（0 ~ 50 年，负相关）
age = np.random.randint(0, 51, size=data_size)

# 距离地铁（100 ~ 3000 米，负相关）
distance_to_subway = np.random.randint(100, 3001, size=data_size)

# 生成价格
price = (
    area * 0.3  # 面积增加价格
    - age * 0.5  # 房龄增加降低价格
    - distance_to_subway * 0.02  # 距地铁远降低价格
    + np.random.normal(0, 5, size=data_size)  # 添加随机噪声
)

price = np.maximum(price, 1)




