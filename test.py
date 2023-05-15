import numpy as np
import matplotlib.pyplot as plt
import time

# test = np.array([range(0, 5), range(0, 5), range(0, 5)])

# print(test[0, 1])


# for j in range(0,3):
#     img = np.random.normal(size=(100,150))
#     plt.figure(1); plt.clf()
#     plt.imshow(img)
#     plt.title('Number ' + str(j))
#     plt.pause(3)

v1 = np.random.normal(size=(100000,100))
v2 = np.random.normal(size=(100000,100))
start = time.monotonic()

out = v1 + v2

mid = time.monotonic()

for x in range(0, 100000):
    for y in range(0, 100):
        out = v1[x][y] + v2[x][y]

end = time.monotonic()

print(mid - start)
print(end - mid)