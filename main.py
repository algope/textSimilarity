from shingling import Shingling
from compare_sets import CompareSets

if __name__ == "__main__":
    shingling = Shingling(1)
    shingles = shingling.run()

    # print(shingles['340.txt'])
    # print(shingles['341.txt'])

    comparison = CompareSets(shingles['340.txt'], shingles['341.txt'])
    similarity = comparison.run()
    print("Similarity is: %s" % similarity)

