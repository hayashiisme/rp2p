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

# plot
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

i_minx = -1
xa = []
ya = []

for n in range(d):
    x = random.random()
    if i_minx < 0:
        i_minx = n
    else:
        if xa[i_minx] >= x:
            i_minx = n
    xa.append(x)
    ya.append(random.random())

for n in range(d):
    print(xa[n], ya[n])
    s = 'r.' if n == i_minx else 'g.'
    ax.plot(xa[n], ya[n], s, markersize=10)

# 外側に輪ゴムをかける
i_mind = -1
cosm = -1
for n in range(d):
    if n == i_minx: continue
    # 角度を求めて
    if i_mind == -1:
        i_mind = n
        v0 = ( xa[i_minx], ya[i_minx] - 1 )
        va = ( xa[n] - xa[i_minx], ya[n] - ya[i_minx] )
        cosm = v0[0] * va[0] + v0[1] * va[1]
    else:
        v0 = ( xa[i_minx], ya[i_minx] - 1 )
        va = ( xa[n] - xa[i_minx], ya[n] - ya[i_minx] )
        cosa = v0[0] * va[0] + v0[1] * va[1]
        if cosm > cosa:
            i_mind = n
            cosm = cosa

ax.plot([ xa[i_minx], xa[i_mind] ], [ ya[i_minx], ya[i_mind] ])
            
plt.tight_layout()
plt.show()



    
