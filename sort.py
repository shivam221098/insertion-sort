import time
import random
import matplotlib.pyplot as plt
x_coordinate = []
y_coordinate = []
for k in range(1, 100, 10):
    array = [random.randint(1, 1000) for i in range(k * 100)]
    array.sort()
    start = time.time()
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            j = i - 1
            temp = array[i]
            while temp < array[j] and j >= 0:  # shifting values 1 step forward till we are getting larger values.
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
    print(array)
    print("Time taken: ", round(time.time() - start, 6))
    x_coordinate.append(k * 100)
    y_coordinate.append(round(time.time() - start, 2))

plt.plot(x_coordinate, y_coordinate, marker="o")
print(x_coordinate, y_coordinate)
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()

