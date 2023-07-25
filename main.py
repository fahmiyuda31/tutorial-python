import time
start_time = time.time()

print("hello word")
print("testing hello word")

a = 0
for item in range(1, 100000000):
    a = a + 1

print(time.time() - start_time, "detik")

# python3 -m py_compile main.py 
# to compile python

