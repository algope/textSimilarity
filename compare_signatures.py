
class CompareSignatures:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2

    def run(self):
        return self.estimate()

    def estimate(self):
        count = 0
        for i, elem in enumerate(self._v1):
            if self._v1[i] == self._v2[i]:
                count = count + 1

        return count/len(self._v1)

