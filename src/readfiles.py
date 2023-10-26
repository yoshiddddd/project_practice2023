import matplotlib.pyplot as plt
import pandas as pd
import glob
import numpy as np
import math
import os
import re
def get_csv_filenames(directory):
    all_files = os.listdir(directory)
    csv_filenames = [os.path.splitext(file)[0] for file in all_files if file.endswith('.csv')]
    return csv_filenames

def extract_suffix(filename):
    no_extension = filename.split('.csv', 1)[0]
    return no_extension.rsplit('-', 1)[1]

csv_path = "./各地の気温・降水量2022/*.csv"
dir_path = "./各地の気温・降水量2022/"
csv_list = glob.glob(csv_path)
file_names = get_csv_filenames(dir_path)
number = 0
for files in csv_list:    
    read_csv_file = pd.read_csv(files)
    df = read_csv_file
    temper_label = df.values[0][0]
    rain_label = df.values[1][0]
    # 一列目の削除
    df = df.drop(df.columns[0],axis=1)
    month = df.columns
    temper_value = df.iloc[0].astype(float)
    rain_value = df.iloc[1].astype(float)
    # print(rain_value)
    # !それぞれの最大最小値を取得（y軸で使用・一応変数置）
    # rain_min = rain_value.min()-50
    # rain_max = rain_value.max()+100
    # temp_min = temper_value.min()-5
    # temp_max = temper_value.max()+15
    temp_arr = [0,10,20,30]
    rain_arr = [0,200,400,600]
    # temp_arr = np.linspace(temp_min,temp_max,4)
    # rain_arr = np.linspace(rain_min,rain_max,4)
    # for i in range(len(rain_arr)):
    #     rain_arr[i] = math.floor(rain_arr[i]/10)*10
    # for i in range(len(temp_arr)):
    #     temp_arr[i] = math.floor(temp_arr[i]/10)*10
    # ?同一のx軸を共有するときのsubplotを作成する
    fig,ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    ax1.plot(month,temper_value,color = "brown",marker = 'o',label = temper_label)
    ax2.bar(month,rain_value,label = rain_label)
    ax1.set_ylabel(temper_label)
    ax2.set_ylabel(rain_label)

    ax1.set_yticks(temp_arr)
    ax2.set_yticks(rain_arr)
    #!ax1を前面に持ってくる/ zorder(x):xが大きい方が前面にくる
    ax1.set_zorder(2)
    ax2.set_zorder(1)
    ax1.set_frame_on(False)
    # !凡例を表示させる・足し算によって複数表示させることが可能
    handler1, label1 = ax1.get_legend_handles_labels()
    handler2, label2 = ax2.get_legend_handles_labels()
    ax1.legend(handler1+handler2,label1+label2,borderaxespad=0)
    # グリッドを背面に移動させる
    ax2.set_axisbelow(True)
    ax2.grid()
    # title_name = file_names[number][-2:]
    title_name = extract_suffix(file_names[number])
    plt.title(f"{title_name}の気温・降水量")
    plt.savefig(f"./save_pdf/{file_names[number]}.pdf")
    number += 1
