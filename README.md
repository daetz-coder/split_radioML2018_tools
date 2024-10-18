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

1、提取指定多个 SNR 下的所有调制类型数据
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --snrs 6 \
    --samples 2


2、提取所有调制类型在 -20 dB 和 30 dB 下各 10 个样本，保存为 .npy 文件
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --snrs -20 30 \
    --samples 10


3、指定调制类型在 -20 dB 和 30 dB 下各 10 个样本，保存为 .npy 文件
python scripts/main.py \
    --hdf5_path '../GOLD_XYZ_OSC.0001_1024.hdf5' \
    --output_dir './data/selected_data' \
    --modulations 'QPSK' 'BPSK' \
    --snrs 6 10 \
    --samples 10
