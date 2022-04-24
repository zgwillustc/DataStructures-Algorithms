class HashTable:
    def __init__(self, table_size = 5):
        self.table_size = table_size
        self.entries = [None] * self.table_size

    def put(self, key, value):
        entry = self.__getEntry(key)
        if entry:
            entry[1] = value
            return
        bucket = self.__getorCreateBucket(key)
        bucket.append([key, value])

    def get(self, key):
#        idx = self.__hash(key)
#        bucket = self.entries[idx]
#        if bucket:
#            for entry in bucket:
#                if entry[0] == key:
#                    return entry[1]
#        return None
        entry = self.__getEntry(key)
        return None if not entry else entry[1]
#        if not entry:
#            return None
#        return entry[1]

    def remove(self, key):
#        idx = self.__hash(key)
#        bucket = self.entries[idx]
#        if not bucket:
#            raise Exception('Key not found.')
#        for entry in bucket:
#            if entry[0] == key:
#                bucket.remove(entry)
#                return
#        raise Exception('Key not found.')
        entry = self.__getEntry(key)
        if not entry:
            raise Exception('Key not found.')
        self.__getBucket(key).remove(entry)

    # Use chaining to handle collisions
    def __hash(self, key):
        return key % self.table_size

    def __getEntry(self, key):
        bucket = self.__getBucket(key)
        if bucket:
            for entry in bucket:
                if entry[0] == key:
                    return entry
        return None

    def __getBucket(self, key):
        return self.entries[self.__hash(key)]

    def __getorCreateBucket(self, key):
        idx = self.__hash(key)
        bucket = self.entries[idx]
        if not bucket:
            self.entries[idx] = []

        return self.entries[idx]

#%%
if __name__ == '__main__':
    table = HashTable()
    table.put(6, 'A') # 1
    table.put(8, 'B') # 3
    table.put(11, 'C')
    table.put(6, 'A+')
    print(table.get(6))
    print(table.get(10))
    # table.remove(6)
    #table.remove(60)
