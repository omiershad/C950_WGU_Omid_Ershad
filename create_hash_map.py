# ChainingHashTable implements a hash table using chaining for collision resolution.

class ChainingHashTable:
    # Constructor initializes hash table with empty buckets
    def __init__(self, initial_capacity=10):
        # Create empty buckets
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts key-value pair into hash table
    def insert(self, key, item):
        # Calculate bucket index by hashing key
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Update value if key already exists in bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # Otherwise insert new key-value pair into bucket
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for key in hash table
    def search(self, key):
        # Calculate bucket index
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Linear search for key in bucket
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Removes key-value pair from hash table
    def remove(self, key):
        # Calculate bucket index
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Linear search for key-value in bucket
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])