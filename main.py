from shingling import Shingling
from compare_sets import CompareSets
from min_hashing import MinHashing
from compare_signatures import CompareSignatures

if __name__ == "__main__":
    """Main function of our experiment.
    It runs all the classes implemented using the data stored in the folder "/data" inside the project.
    This data folder contains extracts from news related with different topics. The first line is the headline."""

    # Generates the dictionary with shingles from all documents.
    shingling = Shingling(1)
    shingles = shingling.run()

    # Computes the Jaccard similarity of two given documents.
    comparison = CompareSets(shingles['340.txt'], shingles['341.txt'])
    similarity = comparison.run()
    print("Jaccard similarity is: %s" % similarity)

    # Builds the minHash of two given documents and a given length.
    min_hashing = MinHashing(shingles['340.txt'], 100)
    min_hashing2 = MinHashing(shingles['340.txt'], 100)
    val1 = min_hashing.run()
    val2 = min_hashing2.run()

    # Estimates similarity of two minhash signatures as a fraction of components, in which they agree.
    compare_signatrues = CompareSignatures(val1, val2)
    compared = compare_signatrues.run()
    print("Estimation of the compared signatures: %s" % compared)

