import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import font_manager, rc
import pandas as pd

# font="NanumGothicExtraBold.otf"
# font = font_manager.FontProperties(fname=font).get_name()
# rc('font', family=font)
plt.figure(figsize=(12,7))
  
# csv = pd.read_csv('Fortune_1000.csv', names = ['company','revenue'], encoding="utf-8")    # csv를 읽기
csv = pd.read_csv('Fortune_1000.csv', encoding="utf-8")    # csv를 읽기

company = csv['company']
revenue = csv['revenue']
mean_rev = np.mean(revenue[1:11])
print("mean_rev: ", mean_rev)
  
sum_rev = 0
for rev in revenue[1:11]:
    sum_rev = sum_rev + (rev - mean_rev)**2
variance_rev = mean_rev / len(revenue)
print("variance_rev: ", variance_rev)
  
std_rev = math.sqrt(variance_rev)
print("std_rev: ", std_rev)
  
names2 = ['평균', '표준편차']
values2 = [mean_rev, std_rev ]
  
plt.subplot(1, 3, 1)
  
  
bar = plt.bar(company[1:11], revenue[1:11], color = ['cornflowerblue', 'salmon', 'turquoise'])
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.0f' % height, ha='center', va='bottom', size = 12)
  
plt.subplot(1, 3, 2)
bar2 = plt.bar(names2, values2, color = ['cornflowerblue', 'salmon', 'turquoise'])
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.2f' % height, ha='center', va='bottom', size = 12)
      
plt.subplot(1, 3, 3)   
plt.pie(revenue[1:11], labels=company[1:11], autopct='%.1f', colors=['cornflowerblue', 'salmon', 'turquoise'])
  
  
plt.suptitle('Fortune 1000-Top10(단위:million USD)')
plt.savefig('Fortune 1000.png', bbox_inches='tight')
plt.show()