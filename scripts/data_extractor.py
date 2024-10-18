# scripts/data_extractor.py
# -*- coding: utf-8 -*-
import numpy as np

# 定义调制类型和 SNR 列表
modulation_list = [
    'OOK', '4ASK', '8ASK', 'BPSK', 'QPSK', '8PSK', '16PSK', '32PSK',
    '16APSK', '32APSK', '64APSK', '128APSK', '16QAM', '32QAM', '64QAM',
    '128QAM', '256QAM', 'AM-SSB-WC', 'AM-SSB-SC', 'AM-DSB-WC',
    'AM-DSB-SC', 'FM', 'GMSK', 'OQPSK'
]
snr_list = list(range(-20, 32, 2))  # [-20, -18, ..., 28, 30]

def extract_X_data(X, Y, Z, modulation_type, snr, num_samples):
    """
    提取指定调制类型、信噪比下的随机样本的X数据。

    参数:
        X (numpy.ndarray): IQ数据，形状为 (2555904, 1024, 2)
        Y (numpy.ndarray): 调制类型标签，One-hot编码，形状为 (2555904, 24)
        Z (numpy.ndarray): 信噪比标签，形状为 (2555904, 1)
        modulation_type (str): 目标调制类型，如 'QPSK'
        snr (int): 目标信噪比，如 6
        num_samples (int): 需要提取的样本数量

    返回:
        selected_X (numpy.ndarray): 提取的IQ数据
    """
    try:
        modulation_index = modulation_list.index(modulation_type)
    except ValueError:
        raise ValueError(f"调制类型 '{modulation_type}' 不存在于 modulation_list 中。")

    if snr not in snr_list:
        raise ValueError(f"SNR '{snr}' dB 不存在于 snr_list 中。")

    modulation_mask = Y[:, modulation_index] == 1
    snr_mask = Z[:, 0] == snr
    combined_mask = modulation_mask & snr_mask
    selected_indices = np.where(combined_mask)[0]

    total_available = selected_indices.shape[0]
    if total_available < num_samples:
        raise ValueError(f"可用样本数量 ({total_available}) 少于请求的样本数量 ({num_samples})。")

    random_indices = np.random.choice(selected_indices, size=num_samples, replace=False)
    selected_X = X[random_indices]

    return selected_X
