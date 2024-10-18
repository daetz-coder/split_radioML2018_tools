# scripts/data_saver.py
# -*- coding: utf-8 -*-
import numpy as np
import os

def save_to_npy(file_path, data):
    """
    将数据保存为.npy文件。

    参数:
        file_path (str): 保存路径。
        data (numpy.ndarray): 要保存的数据。
    """
    np.save(file_path, data)
    print(f"数据已保存到 {file_path}")

def create_directory(path):
    """
    创建目录（如果不存在）。

    参数:
        path (str): 目录路径。
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"已创建目录: {path}")
