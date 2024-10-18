# scripts/main.py
# -*- coding: utf-8 -*-
import h5py
import numpy as np
import argparse
import os
import logging
from data_extractor import extract_X_data, modulation_list, snr_list
from data_saver import save_to_npy, create_directory

def main():
    # 设置日志配置
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 打印可用的调制类型
    logging.info(f"可用的调制类型：{', '.join(modulation_list)}")

    # 解析命令行参数
    parser = argparse.ArgumentParser(description='从HDF5文件中提取指定条件的X数据样本。')
    parser.add_argument('--hdf5_path', type=str, required=True, help='HDF5文件的路径。')
    parser.add_argument('--output_dir', type=str, required=True, help='输出文件夹的路径。')
    parser.add_argument('--modulations', type=str, nargs='+', default=modulation_list, help='目标调制类型列表，如 QPSK BPSK。默认选择所有调制类型。')
    parser.add_argument('--snrs', type=int, nargs='+', required=True, help='目标信噪比列表，如 6 10。')
    parser.add_argument('--samples', type=int, default=1000, help='每种条件下提取的样本数量。')

    args = parser.parse_args()

    # 验证用户指定的调制类型是否存在于 modulation_list 中
    invalid_modulations = [mod for mod in args.modulations if mod not in modulation_list]
    if invalid_modulations:
        logging.error(f"以下调制类型不存在于 modulation_list 中：{', '.join(invalid_modulations)}")
        logging.info(f"可用的调制类型：{', '.join(modulation_list)}")
        raise ValueError("存在无效的调制类型，请检查输入。")

    # 设置随机种子（可选）
    np.random.seed(42)

    # 创建输出目录
    create_directory(args.output_dir)

    # 打开HDF5文件并读取数据
    logging.info(f"打开HDF5文件: {args.hdf5_path}")
    try:
        with h5py.File(args.hdf5_path, 'r') as h5file:
            X = h5file['X'][:]  # (2555904, 1024, 2)
            Y = h5file['Y'][:]  # (2555904, 24)
            Z = h5file['Z'][:]  # (2555904, 1)
    except Exception as e:
        logging.error(f"无法打开或读取HDF5文件: {e}")
        raise e

    # 定义提取条件
    target_modulations = args.modulations  # 用户指定的调制类型列表
    target_snrs = args.snrs
    num_samples_per_condition = args.samples

    # 打印目标调制类型和 SNR
    logging.info(f"目标调制类型：{', '.join(target_modulations)}")
    logging.info(f"目标 SNR：{', '.join(map(str, target_snrs))} dB")
    logging.info(f"每种条件下提取的样本数量：{num_samples_per_condition}")

    # 遍历每个 SNR
    for snr in target_snrs:
        # 检查 SNR 是否在 snr_list 中
        if snr not in snr_list:
            logging.warning(f"SNR {snr} dB 不存在于 snr_list 中，跳过。")
            continue

        # 创建对应 SNR 的文件夹
        snr_folder = os.path.join(args.output_dir, f"SNR_{snr}")
        create_directory(snr_folder)

        # 遍历每个调制类型
        for modulation in target_modulations:
            try:
                sel_X = extract_X_data(
                    X, Y, Z,
                    modulation_type=modulation,  # 当前调制类型
                    snr=snr,
                    num_samples=num_samples_per_condition
                )

                # 保存数据为 .npy 文件
                file_name = f"X_SNR_{snr}_mod_{modulation}.npy"
                file_path = os.path.join(snr_folder, file_name)
                save_to_npy(file_path, sel_X)
                logging.info(f"提取并保存 {modulation} 在 {snr} dB 下的 {num_samples_per_condition} 个样本成功。")
            except ValueError as e:
                logging.error(e)

    logging.info("所有数据提取与保存操作已完成。")

if __name__ == "__main__":
    main()
