# -*- coding: utf-8 -*- 
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import font_manager, rc
from pandas import *
import pandas as pandas
import matplotlib.font_manager as fm

font = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf')

plt.figure(figsize=(16,16))

company=[]
revenue=[]
with open('Fortune_1000.csv', 'r') as f:
    for line in csv.DictReader(f):
        company.append(line.value(company))
print(company)
#     revenue=data['revenue']
total_rev_10 = np.sum(revenue[1:11].value())
mean_rev_10 = np.mean(revenue[1:11].value())
print("total_rev_10: ", format(round(total_rev_10),','))
print("mean_rev_10: ", '{:,.2f}'.format(mean_rev_10))
 
ss = 0
for rev in revenue[1:11]:
    ss = ss + (rev - mean_rev_10)**2
variance_rev_10 = ss / (len(revenue[1:11])-1)
print("variance_rev_10: ", '{:,.2f}'.format(variance_rev_10))
     
std_rev_10 = math.sqrt(variance_rev_10)
print("std_rev_10: ", '{:,.2f}'.format(std_rev_10))
     
names2 = ['Average', 'Standard deviation']
values2 = [mean_rev_10, std_rev_10]
     
plt.subplot(2, 2, 1)
bar = plt.bar(company[1:11], revenue[1:11], color = ['blue', 'pink', 'green'])
plt.title('미국 최대10업체 매출', fontproperties=font)
plt.xlabel('Companies', fontproperties=font)
ax = 세월_대['대분류'].plot.bar(color = ['blue', 'pink', 'green'])
ax.set_xticklabels(세월['대분류'].value_counts().index, fontproperties=font, rotation = 0)
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+'{:,.0f}'.format(height), ha='center', va='bottom', rotation='vertical')
 
     
plt.subplot(2, 2, 2)
bar2 = plt.bar(names2, values2, color = ['blue', 'pink', 'green'])
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.2f' % height, ha='center', va='bottom')
         
plt.subplot(2, 2, 3)   
plt.pie(revenue[1:11], labels=company[1:11], autopct='%.1f', colors=['blue', 'pink', 'green'])
 
plt.subplot(2, 2, 4) 
heights = [10, 20, 15]
bars = ['A_long', 'B_long', 'C_long']
y_pos = range(len(bars))
plt.bar(y_pos, heights)
# Rotation of the bars names
plt.xticks(y_pos, bars, rotation=90)
 
# plt.rc('font', size=8)          # controls default text sizes
# plt.rc('axes', titlesize=8)     # fontsize of the axes title
# plt.rc('axes', labelsize=8)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=8)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=8)    # fontsize of the tick labels
# plt.rc('legend', fontsize=8)    # legend fontsize
# plt.rc('figure', titlesize=8)  # fontsize of the figure title
     
plt.suptitle('Fortune 1000 Top10 (Unit:million USD)')
plt.savefig('Fortune 1000.png', bbox_inches='tight')
plt.show()