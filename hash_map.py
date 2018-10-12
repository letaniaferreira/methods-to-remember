class MyHashMap(object):
    
    def __init__(self):
        self.length = 5
        self.hash_map = [None] * self.length
        self.occupancy = 0

    def insert(self, key, val):

        my_hash = self.hash_key(key)

        if self.hash_map[my_hash] is None:
            self.hash_map[my_hash] = [(key, val)]
        else:
            self.hash_map[my_hash].append((key, val))
        self.occupancy += 1
        if self.occupancy >= self.length * 0.8:
            self.increase_map()
        
    def search(self, key):

        index = self.hash_key(key)

        if self.hash_map[index] is None:
            return None

        for item in self.hash_map[index]:
            if key == item[0]:
                return item[1]
        
        return None

    def hash_key(self, key):

        if key is None:
            raise Exception('None is an invalid key')

        if type(key) != int:
            num = 0
            for item in key:
                n = ord(item)
                num += n
        else:
            num = key
        my_hash = ((num * 5) % self.length)

        return my_hash

    def increase_map(self):

            self.length = int(self.length * 1.2)
            old_map = self.hash_map
            self.hash_map = [None] * self.length
            # Need to reset so we can reinsert
            self.occupancy = 0
            #I need to take all items from map and add them to new map using new lenght
            for item in old_map:
                if item is not None:
                    lst_len = len(item)
                    while lst_len >= 1:
                        new_hash = item.pop()
                        self.insert(new_hash[0], new_hash[1])
                        lst_len -= 1

def main():
    nested_dict = {}
    kv = [
        ('hello', 'world'),
        ('please', 'implement me'),
        ('one hundred', 100),
        ('nested', nested_dict),
        (200, 'two hundred'),
        (11, 'eleven'),
        (0, 'zero'),
        ('no_value', None),
        (-2, 'negative'),
        (11, 'anothereleven')
    ]

    hashmap = MyHashMap()

    for k, v in kv:
        hashmap.insert(k, v)
        assert hashmap.search(k) is v

    assert hashmap.search('missing') is None


# main()