from shingling import Shingling
from compare_sets import CompareSets
from min_hashing import MinHashing
from compare_signatures import CompareSignatures
from timeit import default_timer as timer
from lsh import LSH
import numpy as np

if __name__ == "__main__":
    """Main function of our experiment.
    It runs all the classes implemented using the data stored in the folder "/data" inside the project.
    This data folder contains extracts from news related with different topics. The first line is the headline."""

    # Generates the dictionary with shingles from all documents.
    print(">>> Generating shingles for all documents...")
    shingling = Shingling(1)
    start = timer()
    shingles = shingling.run()
    end = timer()
    print(">>> Shingles generated in %.2f secs" % (end-start))
    print("")

    # Computes the Jaccard similarity of two given documents.
    comparison = CompareSets(shingles['340.txt'], shingles['341.txt'])
    start = timer()
    similarity = comparison.run()
    end = timer()
    print(">>>>>> Jaccard similarity is: %s and it took: %.2f secs" % (similarity, (end-start)))
    print("")

    # Builds the minHash of two given documents and a given length.
    print(">>> Building the minHash for two given documents.")
    min_hashing = MinHashing(shingles['340.txt'], 100)
    min_hashing2 = MinHashing(shingles['341.txt'], 100)
    min_hashing3 = MinHashing(shingles['342.txt'], 100)
    min_hashing4 = MinHashing(shingles['343.txt'], 100)
    min_hashing5 = MinHashing(shingles['344.txt'], 100)
    min_hashing6 = MinHashing(shingles['345.txt'], 100)
    min_hashing7 = MinHashing(shingles['346.txt'], 100)
    min_hashing8 = MinHashing(shingles['347.txt'], 100)
    start = timer()
    val1 = min_hashing.run()
    val2 = min_hashing2.run()
    val3 = min_hashing3.run()
    val4 = min_hashing4.run()
    val5 = min_hashing5.run()
    val6 = min_hashing6.run()
    val7 = min_hashing7.run()
    val8 = min_hashing8.run()

    end = timer()
    print(">>> minHashes built in %.2f secs" % (end - start))
    print("")


    # Estimates similarity of two minhash signatures as a fraction of components, in which they agree.
    compare_signatrues = CompareSignatures(val1, val2)
    start = timer()
    compared = compare_signatrues.run()
    end = timer()
    print(">>>>>> Estimation of the compared signatures: %s and it took %.2f secs" % (compared, (end-start)))
    print("")


    print(">>> Calculating LSH...")
    # Estimating similarity of a group of documents using LSH
    a1 = np.array(val1)
    a2 = np.array(val2)
    a3 = np.array(val3)
    a4 = np.array(val4)
    a5 = np.array(val5)
    a6 = np.array(val6)
    a7 = np.array(val7)
    a8 = np.array(val8)

    matrix = np.column_stack((a1, a2, a3, a4, a5, a6, a7, a8))
    lsh = LSH(matrix, 0.8)
    candidates, sort = lsh.run()

    print(">>>>>> Similar pair of documents:")
    for i in range(len(sort)):
        pair = sort[i][0]
        print(pair)
