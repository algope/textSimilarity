from operator import itemgetter
from compare_signatures import CompareSignatures


class LSH:

    def __init__(self, minHash, t):
        self._minHash = minHash
        self._t = t

    def run(self):
        return self.apply_LSH_technique(self._minHash, self._t)

    def apply_LSH_technique(self, minHash, t):
        rows = 3
        bands = 4
        candidates = {}
        array_buckets = []
        for band in range(bands):
            array_buckets.append([[] for i in range(101)])

        i = 0
        for b in range(bands):
            buckets = array_buckets[b]
            band = minHash[i:i + rows, :]
            for col in range(band.shape[1]):
                key = int(sum(band[:, col]) % len(buckets))
                buckets[key].append(col)
            i = i + rows

            for item in buckets:
                if len(item) > 1:
                    pair = (item[0], item[1])
                    if pair not in candidates:
                        A = minHash[:, item[0]]
                        B = minHash[:, item[1]]
                        compare_signatures = CompareSignatures(A, B)
                        similarity = compare_signatures.run()
                        if similarity >= t:
                            candidates[pair] = similarity

        sort = sorted(candidates.items(), key=itemgetter(1), reverse=True)
        return candidates, sort
