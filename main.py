from shingling import Shingling
from compare_sets import CompareSets
from min_hashing import MinHashing
from compare_signatures import CompareSignatures

if __name__ == "__main__":
    shingling = Shingling(1)
    shingles = shingling.run()

    # print(shingles['340.txt'])
    # print(shingles['341.txt'])

    comparison = CompareSets(shingles['340.txt'], shingles['341.txt'])
    similarity = comparison.run()
    print("Similarity is: %s" % similarity)

    min_hashing = MinHashing(shingles['340.txt'], 100)
    min_hashing2 = MinHashing(shingles['340.txt'], 100)

    val1 = min_hashing.run()
    val2 = min_hashing2.run()

    compare_signatrues = CompareSignatures(val1, val2)
    compared = compare_signatrues.run()
    print("Estimation: %s" % compared)




