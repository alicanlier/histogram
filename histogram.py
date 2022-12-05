# -*- coding: utf-8 -*- 
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import rc
from pandas import *
import pandas as pandas
import matplotlib.font_manager as fm

font = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf', size=16)
font2 = {'weight': 'bold', 'size': 10}
plt.rc('font', **font2)

# font_file_path_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
# print(len(font_file_path_list))
# print(font_file_path_list[:100]) #복잡하고 길게 나오는 군요 
# 
# # fav_font_file_path_list = filter(lambda x: True if "BM" in x or "SDM" in x else False, font_file_path_list)
# print()
# for font_file_path in font_file_path_list:
#     print(font_file_path)

# font="ARIALNBI.TTF"
# font = font_manager.FontProperties(fname=font).get_name()
# rc('font', family=font)
plt.figure(figsize=(8,16))
 
data = read_csv('Fortune_1000.csv', encoding="utf-8")
company = data['company'].tolist()
old_revenue = data['revenue'].tolist()
revenue = [x/1000 for x in old_revenue]

# df = pandas.read_csv('Fortune_1000.csv')
# sorted_df = df.sort_values(by=["profit"], ascending=False)
# sorted_df.to_csv('Fortune_1000_sortedprofit.csv', index=False)
data2 = read_csv('Fortune_1000_sortedprofit.csv')
company2 = data2['company'].tolist()
old_profit2 = data2['profit'].tolist()
profit2 = [x/1000 for x in old_profit2]
profa=profit2[:5]; compa=company2[:5]
profb=[]; compb=[]

i = 1
y=len(profit2)
while True:
    x=profit2[(y-i)]
    x2=company2[(y-i)]
    if not math.isnan(x):
        profb.append(x)
        compb.append(x2)
        if len(profb)==5:
            break
    i += 1

for x in reversed(profb):
    profa.append(x)
    
for x2 in reversed(compb):
    compa.append(x2)
print(profa)
print(compa)

#sum and mean calculations #######################
total_rev_10 = np.sum(revenue[1:11])
mean_rev_10 = np.mean(revenue[1:11])
print("total_rev_10: ", format(round(total_rev_10),','))
print("mean_rev_10: ", '{:,.2f}'.format(mean_rev_10))

#variance & std calculations #####################
ss = 0
for rev in revenue[1:11]:
    ss = ss + (rev - mean_rev_10)**2
variance_rev_10 = ss / (len(revenue[1:11])-1)
print("variance_rev_10: ", '{:,.2f}'.format(variance_rev_10))

std_rev_10 = math.sqrt(variance_rev_10)
print("std_rev_10: ", '{:,.2f}'.format(std_rev_10))
     
names2 = ['Average', 'Standard deviation']
values2 = [mean_rev_10, std_rev_10]

#Drawing subplots ################################# 
#Histogram for sales #################################      
plt.subplot(311)
# bar = plt.bar(company[1:11], revenue[1:11], fill=False) #, color = ['blue', 'pink', 'green'] 
bar = plt.bar(company[1:11], revenue[1:11], color = ['skyblue'])
# plt.xticks(rotation='vertical')
plt.xticks([])
# plt.set_xticks(range(10), [])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False)      # ticks along the bottom edge are off
plt.title('미국 최대10업체 매출', fontproperties=font)
i=0
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+company[i]+" \n"+'%.1f'%height, ha='center', va='center', rotation='vertical', fontsize=8)
    i=i+1
plt.ylim(0, 600)

# Histogram for profit and loss ########################3
plt.subplot(312)
# bar = plt.bar(company[1:11], revenue[1:11], fill=False) #, color = ['blue', 'pink', 'green'] 
bar = plt.bar(compa, profa, color = ['skyblue'])
# plt.xticks(rotation='vertical')
plt.xticks([])
# plt.set_xticks(range(10), [])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False)      # ticks along the bottom edge are off
plt.title('미국 최대10수익&손액', fontproperties=font)
i=0
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+compa[i]+" \n"+'%.1f'%height, ha='center', va='bottom', rotation='vertical', fontsize=8)
    i=i+1
plt.ylim(-20, 240)  
 
# Histogram for mean and std #################################    
# plt.subplot(323)
# bar2 = plt.bar(names2, values2, color = ['blue', 'pink', 'green'])
# for rect in bar2:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+'{:,.0f}'.format(height), ha='center', va='bottom')

# Pie plot for sales #################################         
plt.subplot(313)   
plt.pie(revenue[1:11], labels=company[1:11], autopct='%.1f')
plt.title('미국 최대10업체 매출 비율', fontproperties=font)
 
# title, save, show  #################################  
# plt.suptitle('Fortune 1000 Top 10 (단위:billion USD)', fontproperties=font, titleweight='bold')
plt.suptitle('Fortune 1000 Top 10 (단위:billion USD)', fontproperties=font)
plt.savefig('Fortune 1000.png', bbox_inches='tight')
plt.show()

# f, (a0, a1) = plt.subplots(1, 2, width_ratios=[3, 1])
# f, (a0, a1, a2) = plt.subplots(3, 1, height_ratios=[1, 1, 3])