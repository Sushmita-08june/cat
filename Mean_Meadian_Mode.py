#Finding mean of array (average of array numbers)
n_num = [2, 5, 6, 7, 8]
n = len(n_num)
meanofn_num = sum(n_num) / n
print(meanofn_num)

#or

from statistics import mean
n_num = [2, 5, 6, 7, 8]
print(mean(n_num))

#Median of array (middle number after arranging small value to bigger value from left to right)
A = [4, -4,-2,-1, 0, 5, 8]
A.sort()
n = len(A)
if n % 2 == 0:
    median1 = A[n//2]
    median2 = A[n//2 -1]
    median = (median1 + median2) / 2
else :
    median = A[n//2]
print('median of A is', median)


#or

from statistics import median , median_low, median_high
A = [1 , 2 , 3 , 4 , 5, 6]
print('Median of data-set A is %s ' % (median(A)))
print('Median low is % s' % (median_low(A)))
print('Median high is % s' % (median_high(A)))

#Mode of the array
from statistics import mode, multimode
B = [1, 2, 5, 1, 1, 3, 2, 2,2, 3]
C = ('aabbbbbccdddddfffffg')
print(mode(B))
print(multimode(C))

