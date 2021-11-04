from typing import List
import array
import struct

# https://docs.python.org/2/library/sys.html#sys.maxint
LONG_SIZE_IN_BYTES = struct.calcsize('l')
MIN_INT = -2 ** (8 * LONG_SIZE_IN_BYTES - 1)
MAX_TRIALS = 4


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
    __slots__ = ("hash_first_level", "hash_second_level", "collection_size", "counts", "hash_table")

    def __init__(self, collection: List[int], max_trials=MAX_TRIALS):
        self.collection_size = len(collection)
        self.fill_hash_table(collection)

    def fill_hash_table(self, collection: List[int]):
        # TODO: implement me and use array.array
        raise ValueError("cannot build perfect hash table within %s trials" % MAX_TRIALS)

    def __contains__(self, item) -> bool:
        # TODO: implement me
        pass
