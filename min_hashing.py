import random


class MinHashing:

    def __init__(self, s1, length):
        self._s1 = s1
        self._length = length

    def run(self):
        return self.hashing()

    def hashing(self):
        max_num = 2 ** 32 - 1
        prime = 4294975747
        min_hash = [None] * self._length
        random.seed(111)

        for n in range(self._length):
            a = random.randint(1, max_num)
            b = random.randint(1, max_num)
            vec = [None] * len(self._s1)

            for i, elem in enumerate(self._s1):

                calc = ((a * elem + b) % prime) % max_num
                vec[i] = calc

            min_hash[n] = min(vec)

        return min_hash
