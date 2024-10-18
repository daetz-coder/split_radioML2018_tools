# RadioML2018.01a data splitting

+ memory  > 20GB



*This project provides a data partitioning method for processing the RadioML2018.01a dataset, supporting the output of single or multiple types of data. The output results are saved in npy files, making it convenient for subsequent loading and usage. This method allows flexible selection of different modulation types, SNR values, and sample sizes, with the results saved in npy format.*



### 1、Project Structure

```less
project/
│
├── data/
│
├── scripts/
│   ├── data_extractor.py
│   ├── data_saver.py
│   └── main.py
│
├── tests/
│   └── check_npy.ipynb
│
├── requirements.txt
└── README.md
```

### 2、Install dependencies

```bash
pip install requirements.txt
```



### 3、Execution

+ --hdf5_path: The path to the input HDF5 file (required).

+ --output_dir: The root directory for saving the output data (required).

+ --modulations: The list of target modulation types (optional). If not specified, all 24 modulation types are selected by default.

+ --snrs: The list of target SNRs (required).

+ --samples: The number of samples extracted under each condition (default is 1000).

```bash
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --snrs 6 \
    --samples 10
```

```bash
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --snrs -20 30 \
    --samples 10
```

```bash
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --modulations 'QPSK' 'BPSK' \
    --snrs 6 \
    --samples 10
```



### 4、Result

```less
project/
│
├── data/
│   └── selected_data/
│       ├── SNR_6/
│       │   ├── X_SNR_6_mod_QPSK.npy
│       │   └── X_SNR_6_mod_BPSK.npy
│       └── SNR_10/
│           ├── X_SNR_10_mod_QPSK.npy
│           └── X_SNR_10_mod_BPSK.npy
│
├── scripts/
│   ├── data_extractor.py
│   ├── data_saver.py
│   └── main.py
│
├── tests/
│   └── check_npy.ipynb
│
├── requirements.txt
└── README.md
```





### 5、Terminal log

```bash
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --snrs 6 \
    --samples 10
```

```less
2024-10-18 16:01:19,326 - INFO - 可用的调制类型：OOK, 4ASK, 8ASK, BPSK, QPSK, 8PSK, 16PSK, 32PSK, 16APSK, 32APSK, 64APSK, 128APSK, 16QAM, 32QAM, 64QAM, 128QAM, 256QAM, AM-SSB-WC, AM-SSB-SC, AM-DSB-WC, AM-DSB-SC, FM, GMSK, OQPSK
2024-10-18 16:01:19,327 - INFO - 打开HDF5文件: ../GOLD_XYZ_OSC.0001_1024.hdf5
2024-10-18 16:01:33,334 - INFO - 目标调制类型：OOK, 4ASK, 8ASK, BPSK, QPSK, 8PSK, 16PSK, 32PSK, 16APSK, 32APSK, 64APSK, 128APSK, 16QAM, 32QAM, 64QAM, 128QAM, 256QAM, AM-SSB-WC, AM-SSB-SC, AM-DSB-WC, AM-DSB-SC, FM, GMSK, OQPSK
2024-10-18 16:01:33,334 - INFO - 目标 SNR：6 dB
2024-10-18 16:01:33,334 - INFO - 每种条件下提取的样本数量：10
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_OOK.npy
2024-10-18 16:01:33,379 - INFO - 提取并保存 OOK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_4ASK.npy
2024-10-18 16:01:33,425 - INFO - 提取并保存 4ASK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_8ASK.npy
2024-10-18 16:01:33,467 - INFO - 提取并保存 8ASK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_BPSK.npy
2024-10-18 16:01:33,510 - INFO - 提取并保存 BPSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_QPSK.npy
2024-10-18 16:01:33,553 - INFO - 提取并保存 QPSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_8PSK.npy
2024-10-18 16:01:33,595 - INFO - 提取并保存 8PSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_16PSK.npy
2024-10-18 16:01:33,637 - INFO - 提取并保存 16PSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_32PSK.npy
2024-10-18 16:01:33,685 - INFO - 提取并保存 32PSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_16APSK.npy
2024-10-18 16:01:33,728 - INFO - 提取并保存 16APSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_32APSK.npy
2024-10-18 16:01:33,770 - INFO - 提取并保存 32APSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_64APSK.npy
2024-10-18 16:01:33,813 - INFO - 提取并保存 64APSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_128APSK.npy
2024-10-18 16:01:33,855 - INFO - 提取并保存 128APSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_16QAM.npy
2024-10-18 16:01:33,897 - INFO - 提取并保存 16QAM 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_32QAM.npy
2024-10-18 16:01:33,940 - INFO - 提取并保存 32QAM 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_64QAM.npy
2024-10-18 16:01:33,988 - INFO - 提取并保存 64QAM 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_128QAM.npy
2024-10-18 16:01:34,030 - INFO - 提取并保存 128QAM 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_256QAM.npy
2024-10-18 16:01:34,072 - INFO - 提取并保存 256QAM 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_AM-SSB-WC.npy
2024-10-18 16:01:34,115 - INFO - 提取并保存 AM-SSB-WC 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_AM-SSB-SC.npy
2024-10-18 16:01:34,157 - INFO - 提取并保存 AM-SSB-SC 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_AM-DSB-WC.npy
2024-10-18 16:01:34,200 - INFO - 提取并保存 AM-DSB-WC 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_AM-DSB-SC.npy
2024-10-18 16:01:34,242 - INFO - 提取并保存 AM-DSB-SC 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_FM.npy
2024-10-18 16:01:34,291 - INFO - 提取并保存 FM 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_GMSK.npy
2024-10-18 16:01:34,333 - INFO - 提取并保存 GMSK 在 6 dB 下的 10 个样本成功。
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_OQPSK.npy
2024-10-18 16:01:34,375 - INFO - 提取并保存 OQPSK 在 6 dB 下的 10 个样本成功。
2024-10-18 16:01:34,376 - INFO - 所有数据提取与保存操作已完成。
```

```bash
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --modulations 'QPSK' 'BPSK' \
    --snrs 6 \
    --samples 2
```

```less
2024-10-18 15:56:47,481 - INFO - 可用的调制类型：OOK, 4ASK, 8ASK, BPSK, QPSK, 8PSK, 16PSK, 32PSK, 16APSK, 32APSK, 64APSK, 128APSK, 16QAM, 32QAM, 64QAM, 128QAM, 256QAM, AM-SSB-WC, AM-SSB-SC, AM-DSB-WC, AM-DSB-SC, FM, GMSK, OQPSK
2024-10-18 15:56:47,482 - INFO - 打开HDF5文件: ../GOLD_XYZ_OSC.0001_1024.hdf5
2024-10-18 15:57:01,735 - INFO - 目标调制类型：QPSK
2024-10-18 15:57:01,735 - INFO - 目标 SNR：6 dB
2024-10-18 15:57:01,735 - INFO - 每种条件下提取的样本数量：2
数据已保存到 ./data/selected_data/SNR_6/X_SNR_6_mod_QPSK.npy
2024-10-18 15:57:01,772 - INFO - 提取并保存 QPSK 在 6 dB 下的 2 个样本成功。
2024-10-18 15:57:01,772 - INFO - 所有数据提取与保存操作已完成。
```





