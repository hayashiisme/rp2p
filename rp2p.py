# -*- coding: utf-8 -*-
import random
import array

random.seed()
while True:
    d = int(random.random() * 16.0)
    if d > 3: break
print("{} points".format(d))
aa = []
for n in range(d): aa.append(array.array('d', [ random.random(), random.random() ]))
for a in aa: print(a)

    
