# -*- coding: utf-8 -*- 
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import rc
from pandas import *
import pandas as pandas
import matplotlib.font_manager as fm

font = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf', size=18)
font2 = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf', size=12)
font3 = {'weight': 'bold', 'size': 8}
# plt.rc('font', **font2)

plt.figure(figsize=(20,15))
 
data = read_csv('Fortune_1000.csv', encoding="utf-8")
company = data['company'].tolist()
old_revenue = data['revenue'].tolist()
revenue = [x/1000 for x in old_revenue]
old_profit = data['profit'].tolist()
profit = [x/1000 for x in old_profit]
total_rev = np.sum(revenue)
revenue_percent = [x*100/total_rev for x in revenue]

# df = pandas.read_csv('Fortune_1000.csv')
# sorted_df = df.sort_values(by=["profit"], ascending=False)
# sorted_df.to_csv('Fortune_1000_sortedprofit.csv', index=False)
data2 = read_csv('Fortune_1000_sortedprofit.csv')
company2 = data2['company'].tolist()
old_revenue2 = data2['revenue'].tolist()
revenue2 = [x/1000 for x in old_revenue2]
old_profit2 = data2['profit'].tolist()
profit2 = [x/1000 for x in old_profit2]
#Best 5 profiting companies
prof2=profit2[:5]; comp2=company2[:5]
#Worst 5 profiting companies to be appended later
profb=[]; compb=[]

i = 1
y=len(profit2)
while True:
    p=profit2[(y-i)]
    c=company2[(y-i)]
    if not math.isnan(p):
        profb.append(p)
        compb.append(c)
        if len(profb)==5:
            break
    i += 1

for x in reversed(profb):
    prof2.append(x)
    
for x in reversed(compb):
    comp2.append(x)


# ******************************** Drawing subplots ****************************************

#Bar chart for sales #################################################################################      
plt.subplot(241)
bar = plt.bar(company[0:10], revenue[0:10], color = ['skyblue'])
plt.xticks([])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False)      # ticks along the bottom edge are off
plt.title('1) 미국 최대10업체 매출', fontproperties=font2)
i=0
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+company[i]+" ("+'%.1f'%height+") ", ha='left', va='top', rotation=90, fontsize=8)
    i=i+1
plt.ylim(0, 590)

# Bar chart for profit and loss ########################################################################
plt.subplot(242)
bar = plt.bar(comp2[0:5], prof2[0:5], color = ['skyblue'])
i=0
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+comp2[i]+" ("+'%.1f'%height+") ", ha='center', va='top', rotation=90, fontsize=8)    
    i=i+1
bar = plt.bar(comp2[5:], prof2[5:], color = ['red'])
i=0
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, "   "+comp2[i]+" ("+'%.1f'%height+")", ha='center', va='bottom', rotation=90, fontsize=8)    
    i=i+1
# plt.xticks(rotation='vertical')
plt.xticks([])
# plt.set_xticks(range(10), [])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False)      # ticks along the bottom edge are off
plt.title('2) 미국 최대10수익&손액', fontproperties=font2)
plt.ylim(-8, 100)

# Bar chart for all top 50 companies wrt sales, and their sales, profits and losses ########################################################################
plt.subplot(243)
bar = plt.bar(company[:50], revenue[:50], color = ['skyblue'], label='revenue')
bar = plt.bar(company[:50], profit[:50], color = ['green'], label='profit')
plt.xlabel('Revenue decreasing order ->', fontproperties=font3)
plt.xticks([])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False)      # ticks along the bottom edge are off
plt.title('3) 미국 최대50매출&그의 수익&손액', fontproperties=font2)
plt.ylim(-8, 590)
plt.legend()

# Bar chart for all top 50 companies wrt profits, and their sales, profits and losses ########################################################################
plt.subplot(244)
bar = plt.bar(company2[:50], revenue2[:50], color = ['skyblue'], label='revenue')
bar = plt.bar(company2[:50], profit2[:50], color = ['green'], label='profit')
plt.xlabel('Profit decreasing order ->', fontproperties=font3)
plt.xticks([])
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False)      # ticks along the bottom edge are off
plt.title('4) 미국 최대50수익&그의 매출&수익', fontproperties=font2)
plt.ylim(0, 590)
plt.legend() 
 
# Histogram for mean and std #################################    
# plt.subplot(323)
# bar2 = plt.bar(names2, values2, color = ['blue', 'pink', 'green'])
# for rect in bar2:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+'{:,.0f}'.format(height), ha='center', va='bottom')

# Pie plot for sales top 10 &  all 990 as the rest #################################################################################         
plt.subplot(245)
explode = (0.1, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0)
plt.pie(revenue_percent[0:10], labels=company[0:10], explode=explode, 
        autopct=lambda p: '{:.2f}%'.format(p * np.sum(revenue_percent[0:10]) / 100), shadow=True, startangle=-120,
        pctdistance=0.8, labeldistance=1.05, textprops={'fontsize': 8})
# plt.axis('equal')
plt.title('5) 미국 최대10업체 매출 비율', fontproperties=font2)

# Pie plot for sales top 10 &  all 990 as the rest #################################################################################         
plt.subplot(246)
revenue_percent2 = [np.sum(revenue_percent[10:])]
labels2 = ["the rest"]
explode = (0.1, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(revenue_percent[0:10]+revenue_percent2, labels=company[0:10]+labels2, explode=explode, autopct='%.2f', shadow=True, startangle=0,
        pctdistance=0.8, labeldistance=1.05, textprops={'fontsize': 6})
plt.title('6) 미국 최대10업체와 나머지의 매출 비율', fontproperties=font2)

# Histogram for all 1000 companies, showing both sales and profits ################################################################################################
plt.subplot(247)
plt.style.use('default')
plt.rcParams['font.size'] = 12

plt.hist(revenue, bins=50, alpha=0.3, edgecolor='blue', label='revenue')
plt.xlim(0, 600)
# plt.hist(profit2, bins=100, alpha=1, edgecolor='blue', histtype='step', label='profit')
# plt.ylim(0, 40)
# plt.hist(profit2, bins=100, density=True, alpha=0.75, histtype='step', label='profit')
# plt.ylim(0, 0.05)
# plt.xlim(3, 100)
plt.yscale('log')
plt.xlabel('Revenue', fontproperties=font3)
plt.ylabel('Count', fontproperties=font3)
plt.title('7) 미국 최대1000업체 매출 히스토그램', fontproperties=font2)
plt.legend()

# Histogram for all 1000 companies, showing both sales and profits ################################################################################################
plt.subplot(248)
plt.style.use('default')
plt.rcParams['font.size'] = 12

plt.hist(profit2, bins=20, alpha=0.5, edgecolor='green', label='profit')
plt.xlim(-10, 100)
# plt.ylim(0, 100)

plt.yscale('log',base=10)
plt.xlabel('Profit', fontproperties=font3)
plt.ylabel('Count', fontproperties=font3)
plt.title('8) 미국 최대1000업체 수익 히스토그램', fontproperties=font2)
plt.legend()

# title, save, show  #########################################################################################################  
# plt.suptitle('Fortune 1000 Top 10 (단위:billion USD)', fontproperties=font, titleweight='bold')
plt.suptitle('2021년 미국 Fortune 1000 Top 10 (단위:billion USD)', fontproperties=font)
plt.savefig('Fortune 1000_1.png', bbox_inches='tight')
plt.subplots_adjust(
    top=0.911,
    bottom=0.09,
    left=0.040,
    right=0.970,
    hspace=0.14,
    wspace=0.22,
)
plt.show()

# f, (a0, a1) = plt.subplots(1, 2, width_ratios=[3, 1])
# f, (a0, a1, a2) = plt.subplots(3, 1, height_ratios=[1, 1, 3])