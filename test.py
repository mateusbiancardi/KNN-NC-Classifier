from collections import Counter
import cv2
import math


k = 5
k_neighbors = [1, 1, 2, 2, 4]



count = Counter(k_neighbors)
most_Common = count.most_common(1)[0][0]

print (most_Common)
    