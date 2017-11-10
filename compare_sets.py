

class CompareSets:
    def __init__(self, s1, s2):
        self._s1 = s1
        self._s2 = s2

    def run(self):
        return self.compare()

    def compare(self):
        # Calculate and store the actual Jaccard similarity.
        return len(self._s1.intersection(self._s2)) / len(self._s1.union(self._s2))
