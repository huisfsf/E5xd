import os
import pandas as pd

# 获取当前文件夹路径
folder_path = os.getcwd()

# 创建一个空的DataFrame来存储所有的最大值和文件路径
max_values = pd.DataFrame()

# 遍历文件夹中的所有Excel文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)
        # 读取Excel文件中的第一个表格
        df = pd.read_excel(file_path, sheet_name=0)
        # 找到每一列的最大值并添加到max_values DataFrame中
        max_values[file_name] = df.max()
        # 添加文件路径到新的一列中
        max_values[file_name + ' file'] = file_path

# 将所有最大值和文件路径写入一个新的Excel文件
max_values.to_excel('max_values_with_path.xlsx', index=False)
