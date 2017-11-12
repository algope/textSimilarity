# Finding Similar Items: Textually Similar Documents
Lidia Fernández Garcés - lidiafg@kth.se | Alejandro González Pérez - agp@kth.se

## Introduction
In this project, we will test different ways of finding textual similarity within two documents. More specifically we will test shingling, minhashing, and locality-sensitive hashing methods.

## Structure
The project is structured in 5 classes that carry out all the tasks for implementing the methods mentioned above.

```
textSimilarity
│   README.md
│   compare_sets.py
|   compare_signatures.py
|   lsh.py
|   main.py
|   min_hashing.py
|   shingling.py
│
└───data
      file011.txt
      file012.txt
```
The folder `/data` contains the documents using to test our implementation. 

## Implementation
### Class Shingling
This class constructs k–shingles of a given length from a given document computes a hash value for each unique shingle and represents the document in the form of an ordered set of its hashed k-shingles.

Since we are working with documents, the function `shingling` reads all the lines of each text and then generates the shingles using a given size representing the number of characters that are going to be in the same shingle. 
Once we have all the shingles generated, we will encode them using the CRC algorithm and store them in our dictionary of shingles per each document.

### Class CompareSets
This class computes the Jaccard similarity of two sets of integers (two sets of hashed shingles). To calculate so, we will use the mathematical operation that calculates the length of the intersection and the length of the union of both shingle sets. Afterwards and by dividing this two numbers, we will obtain the Jaccard similarity.

### Class MinHashing
This class builds a minHash signature (in the form of a vector or a set) of a given length n from a given set of integers (a set of hashed shingles). More specifically, the method `hashing` uses the maximum value that our previous CRC algorithm function can generate, a higher prime of that number and a given seed for replicating the random number generation and builds the minHash signature.

### Class CompareSignatures
This class estimates similarity of two integer vectors (minhash signatures) as a fraction of components, with which they agree. To do so, it will compare all the elements of two minhash signatures previously calculated and count which ones are equal.

### Class LSH
This implements the LSH technique: given a collection of minhash signatures (matrix where each column is a vector of minhash values representing the document) and a similarity threshold t, the LSH class (using banding and hashing) finds all candidate pairs of signatures that agree on at least fraction t of their components.


## Running the project
To test the implementation, the only requirements are to have `Python 3.6.x` or above installed and install the library `numpy`with the command `pip install numpy` then run the `main.py` file as usual. This project doesn't require external dependencies for it to work.

`python main.py`
