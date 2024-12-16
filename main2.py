import hashlib
import time
import sys
import pickle

# Function to read dictionary from a file
def read_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# Function to create the rainbow table
def create_rainbow_table(dictionary):
    rainbow_table = {}
    for word in dictionary:
        # Compute the SHA1 hash
        hashed = hashlib.sha1(word.encode()).hexdigest()
        rainbow_table[word] = hashed
    return rainbow_table

# Path to the dictionary file
dictionary_file = "10k-most-common.txt"

# Read the dictionary
try:
    dictionary = read_dictionary(dictionary_file)
except FileNotFoundError:
    print(f"Error: File {dictionary_file} not found.")
    sys.exit(1)

# Measure the time taken to create the table
start_time = time.time()
rainbow_table = create_rainbow_table(dictionary)
end_time = time.time()

time_taken = end_time - start_time

# Measure the size of the rainbow table using pickle (serializing to measure memory footprint)
rainbow_table_size = sys.getsizeof(pickle.dumps(rainbow_table))

# Print results
print("Rainbow Table:")
for word, hashed in list(rainbow_table.items()):  
    print(f"{word}: {hashed}")

print(f"\nTime taken to create the rainbow table: {time_taken:.6f} seconds")
print(f"Size of the rainbow table: {rainbow_table_size} bytes")