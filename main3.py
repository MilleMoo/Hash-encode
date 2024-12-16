import hashlib
import time

file_path = "10k-most-common.txt"

with open(file_path, "r", encoding="utf-8") as f:
    passwords = f.readlines()

passwords = [pwd.strip() for pwd in passwords]

total_time = 0
for password in passwords:
    start_time = time.perf_counter()
    hashlib.sha1(password.encode()).hexdigest()
    end_time = time.perf_counter()
    total_time += (end_time - start_time)

print(f"Number of passwords hashed: {len(passwords)}")
print(f"Total time taken: {total_time:.5f} seconds")
print(f"Average time per password: {total_time / len(passwords):.10f} seconds")
