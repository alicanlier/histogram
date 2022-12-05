# -*- coding: utf-8 -*- 
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import rc
from pandas import *
import pandas as pandas
import matplotlib.font_manager as fm

font = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf', size=16, weight='bold') #weight='normal' weight='bold'
font2 = fm.FontProperties(fname='C:\\Windows\\Fonts\\malgun.ttf', size=12, weight='bold')
# font2 = {'weight': 'bold', 'size': 8}
font3 = {'weight': 'bold', 'size': 6}
# plt.rc('font', **font)

plt.figure(figsize=(12,8))
 
data = read_csv('Fortune_1000.csv', encoding="utf-8")
company = data['company'].tolist()
old_revenue = data['revenue'].tolist()
revenue = [x/1000 for x in old_revenue]
old_profit = data['profit'].tolist()
profit = [x/1000 for x in old_profit]

#sum and mean calculations for all #######################
total_rev = np.sum(revenue)
mean_rev = np.mean(revenue)
print("total_rev: ", format(round(total_rev),','))
print("mean_rev: ", '{:,.2f}'.format(mean_rev))

#variance & std(standard deviation) calculations for all #####################
ss = 0
for rev in revenue:
    ss = ss + (rev - mean_rev)**2
variance_rev = ss / (len(revenue)-1)
print("variance_rev: ", '{:,.2f}'.format(variance_rev))

std_rev = math.sqrt(variance_rev)
print("std_rev: ", '{:,.2f}'.format(std_rev))
     
names = ['Average_1000', 'Standard\ndeviation_1000']
values = [mean_rev, std_rev]

#sum and mean calculations for top 10 #######################
total_rev_10 = np.sum(revenue[0:10])
mean_rev_10 = np.mean(revenue[0:10])
print("total_rev_10: ", format(round(total_rev_10),','))
print("mean_rev_10: ", '{:,.2f}'.format(mean_rev_10))

#variance & std(standard deviation) calculations for top 10 #####################
ss = 0
for rev in revenue[1:11]:
    ss = ss + (rev - mean_rev_10)**2
variance_rev_10 = ss / (len(revenue[0:10])-1)
print("variance_rev_10: ", '{:,.2f}'.format(variance_rev_10))

std_rev_10 = math.sqrt(variance_rev_10)
print("std_rev_10: ", '{:,.2f}'.format(std_rev_10))
     
names2 = ['Average_10', 'Standard\ndeviation_10']
values2 = [mean_rev_10, std_rev_10]


# ******************************** Drawing subplots ****************************************

#Bar chart for mean and std (sqrt of variance) #################################   
plt.subplot(221)
bar2 = plt.bar(names+names2, values+values2, color = ['blue', 'pink', 'blue', 'pink'])
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, " "+'{:,.0f}'.format(height), ha='center', va='bottom')
plt.title('9) 미국 최대1000&최대10 매출 평균&표준편차', fontproperties=font2)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    rotation=10)      # ticks along the bottom edge are off
plt.ylim(0, 360) 

#Linear regression for revenue-profit relationship #################################   
plt.subplot(222)
# Generate data
# x = rng.uniform(0, 10, size=100)
# y = x + rng.normal(size=100)
x = revenue[:10]
y = profit[:10]

# Initialize layout: fig, ax = plt.subplots(figsize = (9, 9))
# Add scatterplot
plt.scatter(x, y, s=60, alpha=0.7, edgecolors="k")

# Fit linear regression via least squares with numpy.polyfit
# It returns an slope (b) and intercept (a)
# deg=1 means linear fit (i.e. polynomial of degree 1)
b, a = np.polyfit(x, y, deg=1)

# Create sequence of 100 numbers from 0 to 100 
xseq = np.linspace(0, 600, num=100)

# Plot regression line
plt.plot(xseq, a + b * xseq, color="k", lw=1.5);
plt.title('10) 미국 최대10매출&수익관계', fontproperties=font2)
plt.xlabel('Revenue', fontproperties=font2)
plt.ylabel('Profit', fontproperties=font2)

#Linear regression for revenue-profit relationship #################################   
# plt.subplot(223)
# x = revenue[600:]
# y = profit[600:]
# plt.scatter(x, y, s=10, alpha=0.3, edgecolors="k")
# b, a = np.polyfit(x, y, deg=1)
# xseq = np.linspace(0, 37, num=50)
# plt.plot(xseq, a + b * xseq, color="k", lw=1.5);


#Linear regression for revenue-profit relationship #################################   
plt.subplot(212)
x = revenue
y = profit
plt.scatter(x, y, s=10, alpha=0.8, edgecolors="k")
# b, a = np.polyfit(x, y, deg=1)
# xseq = np.linspace(0, 37, num=50)
# plt.plot(xseq, a + b * xseq, color="k", lw=1.5);
plt.title('11) 미국 최대1000매출&수익관계', fontproperties=font2)
plt.xlabel('Revenue', fontproperties=font2)
plt.ylabel('Profit', fontproperties=font2) 
 
# title, save, show  #################################  
# plt.suptitle('Fortune 1000 Top 10 (단위:billion USD)', fontproperties=font, titleweight='bold')
plt.suptitle('2021년 미국 Fortune 1000 Top 10 (단위:billion USD)', fontproperties=font)
plt.savefig('Fortune 1000_1_2.png', bbox_inches='tight')
plt.subplots_adjust(
    top=0.900,
    bottom=0.09,
    left=0.046,
    right=0.980,
    hspace=0.30,
    wspace=0.20,
)
plt.show()

