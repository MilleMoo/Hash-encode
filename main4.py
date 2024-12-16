import hashlib
import time

# Example password
password = "securepassword123"

# Convert to bytes
password_bytes = password.encode()

# Measure hashing time
start_time = time.perf_counter()
hash_result = hashlib.sha1(password_bytes).hexdigest()
end_time = time.perf_counter()

# Calculate elapsed time
elapsed_time = end_time - start_time

print(f"SHA-1 hash: {hash_result}")
print(f"Time taken: {elapsed_time:.10f} seconds")
