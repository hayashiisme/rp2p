# -*- coding: utf-8 -*-
import random
import array
import math
import matplotlib.pyplot as plt

random.seed()
while True:
    d = int(random.random() * 16.0)
    if d > 3: break
print("{} points".format(d))
aa = []
for n in range(d): aa.append(array.array('d', [ random.random(), random.random() ]))
for a in aa: print(a)

# plot
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
for a in aa: ax.plot(a[0], a[1], 'g.', markersize=10)
plt.tight_layout()
#plt.savefig(op, dpi=300)
plt.show()



    
# 最初の点との組み合わせで2点間の距離を取る
dists = []
for i in range(len(aa) - 1):
    for j in range(i + 1, len(aa)):
        x1 = aa[i][0]
        y1 = aa[i][1]
        x2 = aa[j][0]
        y2 = aa[j][1]
        dists.append([math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), i, j])

for dist in sorted(dists): print(dist)

