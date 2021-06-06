import random
from collections import deque
x=[]
for x in range(50):
    x.append(random.randint(0,300))
kolejka=deque(x)
print(kolejka)
kolejka.append(69)
kolejka.popleft()
kolejka.popleft()
print(kolejka)
