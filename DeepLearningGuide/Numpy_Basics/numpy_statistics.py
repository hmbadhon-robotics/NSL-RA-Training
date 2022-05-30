import numpy as np
from matplotlib import pyplot as plt


a = np.array([2, 3, 4])

print(a)

##Using Numpy Reshape
a = np.arange(28).reshape(4, 7)

print(a)
#printing array shape
print(a.shape)

####CENSUS and SAMPLE

a = np.random.rand(20)
print(a)

## Mean
a = np.array([10, 14, 4, 7, 9, 12, 15])
print(np.mean(a))

## Median
a = np.array([10, 14, 4, 7, 9, 12, 15])
print(np.median(a))

##Mode
from scipy import stats
a = np.array([1, 1, 2, 3, 4, 4, 4, 5])
print(stats.mode(a))

## Mean and Median is needed to get the right overview of data.

##Normal Distribution

sizes = np.array([-1000,9, 8, 8, 9, 9, 1, 4, 5, 6, 7, 8, 9, 10, 1000, 10, 11, 11, 11, 11, 11, 13, 12, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 15, 16, 17, 18, 20])

plt.hist(sizes)
plt.show()

## Min Median and Mode is same in normal Distribution
print(np.mean(sizes))
print(np.median(sizes))
print(stats.mode(sizes))

#Variance and Standard Deviation
print(np.std(sizes))

print(np.std(sizes) * np.std(sizes))



##Need For SD and VAR is to find Outliers
## 95% data lies within (+/-) 2 unit of Standard Deviation

##Standardization
from scipy.stats import zscore

z_values=zscore(sizes)

#if a datapoint's z score is 0 it is in the mean
#if it is (+/-) 1, it is one unit away from standard deviation(68% data)
#if it is (+/-) 2, it is two unit away from standard deviation(95% data)

print("Outliers:")

print([sizes[index] for index, val in enumerate(z_values) if val < -2 or val > 2])



