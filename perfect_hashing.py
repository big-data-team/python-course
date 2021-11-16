from typing import List
import array
import struct

# https://docs.python.org/2/library/sys.html#sys.maxint
LONG_SIZE_IN_BYTES = struct.calcsize('l')
MIN_INT = -2 ** (8 * LONG_SIZE_IN_BYTES - 1)
MAX_TRIALS = 4


class HashError(Exception):
    pass


class PerfectHashFirstLevelError(HashError):
    pass


class PerfectHashSecondLevelError(HashError):
    pass


class HashTableChain:
    __slots__ = ("hash_function", "collection_size", "counts", "hash_table")

    def __init__(self, collection: List[int], hash_function=None):
        self.hash_function = hash_function or hash
        self.collection_size = len(collection)
        self.fill_hash_table(collection)

    def fill_hash_table(self, collection: List[int]):
        # TODO: implement me and use array.array
        pass

    def __contains__(self, item) -> bool:
        # TODO: implement me
        pass


class HashTablePerfect:
    """build static hash table with < 4n memory space with universal hash family"""
    __slots__ = (
        "hash_first_level", "hash_second_level",
        "hash_function_counter", "hash_function_counter_per_bucket",
        "max_trials_first_level", "max_hash_function_counter",
        "collection_size", "counts", "hash_table",
    )

    def __init__(self, collection: List[int], max_trials_first_level=MAX_TRIALS, max_hash_function_counter=None):
        self.collection_size = len(collection)
        self.max_trials_first_level = max_trials_first_level
        self.max_hash_function_counter = max_hash_function_counter or 2 * self.collection_size

        self.counts = array.array('l', [])
        self.hash_function_counter = 0
        self.hash_function_counter_per_bucket = array.array('l', [])

        self.fill_hash_table(collection)

    def fill_hash_table(self, collection: List[int]):
        for _ in range(self.max_trials_first_level):
            self.hash_first_level = self.generate_new_hash_function()
            self.hash_second_level = [hash] * self.collection_size
            self._fill_first_level_counts(collection)
            if self._is_big_memory_consumption():
                continue

            self._fill_second_level(collection)
            return

        raise PerfectHashFirstLevelError("cannot build perfect hash table within %s trials" % self.max_trials_first_level)

    def generate_new_hash_function(self):
        # TODO: implement me
        hash_function = lambda item: 0

        self.hash_function_counter += 1
        if self.hash_function_counter >= self.max_hash_function_counter:
            raise PerfectHashSecondLevelError("cannot build perfect hash table with %s hash functions" % self.max_hash_function_counter)

        return hash_function

    def _fill_first_level_counts(self, collection: List[int]):
        # TODO: implement me
        self.counts = array.array('l', [0] * self.collection_size)

    def _is_big_memory_consumption(self) -> bool:
        # TODO: implement me
        return True

    def _fill_second_level(self, collection: List[int]):
        self.hash_table = []
        for _ in range(self.collection_size):
            self.hash_table.append(array.array('l', []))

        # TODO: populate hash_function_counter_per_bucket
        self.hash_function_counter_per_bucket = array.array('l', [0] * self.collection_size)
        # TODO: implement me
        # you can use HashTableChain as temporary intermediate helper collection for buckets
        # in this case, do not forget to specify correct hash_function for it
        # hash_table_chain = HashTableChain(collection, hash_function=self.hash_first_level)

    def __contains__(self, item) -> bool:
        # TODO: implement me
        return False
