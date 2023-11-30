import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

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
month_value = []
month_num = 0
filenames = get_csv_filenames(dir_path)
i = 0
for csv_file in csv_list:
    df = pd.read_csv(csv_file)
    df = df.drop(df.columns[0],axis = 1)
    tmp_mean = round(df.mean(axis=1)[0],1)
    rain_mean = round(df.mean(axis=1)[1],1)
    df = df.drop(index = range(2,10))
    if  i == 0:
        merge_df_list = df
    else:
        merge_df_list = pd.concat([merge_df_list,df])

    # print(df.describe())
    print(extract_suffix(filenames[i]))
    print(f'気温の平均値：{tmp_mean}')
    print(f'降水量の平均値:{rain_mean}')
    i+=1
print(merge_df_list)
# print(month_num/6)
avg_temp = round(merge_df_list.loc[0].mean(), 1)
avg_rain = round(merge_df_list.loc[1].mean(), 1)
std_temp = round(merge_df_list.loc[0].std(), 1)
std_rain = round(merge_df_list.loc[1].std(), 1)

print("各月の全国平均気温")
print(avg_temp)
print("各月の気温標準偏差")
print(std_temp)
print("各月の全国平均降水量")
print(avg_rain)
print("各月の降水量標準偏差")
print(std_rain)

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.grid(True)

color = 'tab:red'
ax1.set_xlabel('月')
ax1.set_ylabel('平均気温', color=color)
ax1.plot(avg_temp, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('平均降水量', color=color)  
ax2.bar(range(len(avg_rain)), avg_rain, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax1.set_zorder(2)
ax2.set_zorder(1)
ax1.set_frame_on(False)
fig.tight_layout()  
plt.show()
