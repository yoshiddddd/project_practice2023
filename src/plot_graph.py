import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
xlsx_path = "./excel_file/東京都の気温・降水量.xlsx"
read_xlsx_file = pd.read_excel(xlsx_path)
df = read_xlsx_file
# print(df)

# 削除する前にラベル保持
temper_label = df.values[0][0]
rain_label = df.values[1][0]

# 一列目の削除
df = df.drop(df.columns[0],axis=1)
month = df.columns
temper_value = df.iloc[0].astype(float)
rain_value = df.iloc[1].astype(float)

# !それぞれの最大最小値を取得（y軸で使用・一応変数置）
rain_min = rain_value.min()-50
rain_max = rain_value.max()+100
temp_min = temper_value.min()-5
temp_max = temper_value.max()+15
temp_arr = np.linspace(temp_min,temp_max,5)
rain_arr = np.linspace(rain_min,rain_max,5)
for i in range(len(rain_arr)):
    rain_arr[i] = math.floor(rain_arr[i]/10)*10
for i in range(len(temp_arr)):
    temp_arr[i] = math.floor(temp_arr[i]/10)*10
print(rain_arr)

# ?同一のx軸を共有するときのsubplotを作成する
fig,ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()
ax1.plot(month,temper_value,color = "brown",marker = 'o',label = temper_label)
ax2.bar(month,rain_value,label = rain_label)
ax1.set_ylabel(temper_label)
ax2.set_ylabel(rain_label)
# ax1.set_ylim(temp_min,temp_max)
# ax2.set_ylim(rain_min,rain_max)
ax1.set_yticks(temp_arr)
ax2.set_yticks(rain_arr)
#ax1を前面に持ってくる/ zorder(x):xが大きい方が前面にくる
ax1.set_zorder(2)
ax2.set_zorder(1)
ax1.set_frame_on(False)

# 凡例を表示させる・足し算によって複数表示させることが可能
handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
ax1.legend(handler1+handler2,label1+label2,borderaxespad=0)

# グリッドを背面に移動させる
ax2.set_axisbelow(True)
# ax1.grid()
ax2.grid()
plt.title("東京の気温・降水量")
plt.show()
