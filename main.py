from __future__ import division
import os
import re
import random
import time
import codecs
import binascii
from bisect import bisect_right
from heapq import heappop, heappush
from itertools import islice, chain


class Shingling:

    def __init__(self, length):
        self.k = length

    def run(self):
        self.shingling()

    def get_shingles(self, line, size):
        normalized = line.strip().lower()
        if len(normalized) <= size:
            return frozenset((normalized,))

        # An entity may be made of several components.
        components = normalized.split()

        def shinglingle(component):
            slices = (islice(component, i, None) for i in range(size))
            return (''.join(chars) for chars in zip(*slices))

        comp_shingles = (shinglingle(comp) for comp in components)
        # Flatten the iterable of all shingles.
        result = frozenset(chain.from_iterable(comp_shingles))
        return result

    def shingling(self):
        """class Shingling that constructs k–shingles of a given length k (e.g., 10) from a given document, computes a
        hash value for each unique shingle, and represents the document in the form of an ordered set of its hashed
        k-shingles. """

        # The current shingle ID value to assign to the next new shingle we
        # encounter. When a shingle gets added to the dictionary, we'll increment this
        # value.
        curShingleID = 0

        # Create a dictionary of the articles, mapping the article identifier (e.g.,
        # "t8470") to the list of shingle IDs that appear in the document.
        global_shingles = {}

        doc_names = []
        num_shingles = 0

        for file in os.listdir('./data'):
            print(file)
            with codecs.open('./data/'+file, encoding="utf-8") as f:

                # Read all of the words (they are all on one line) and split them by white
                # space.
                lines = f.readlines()[1:]
                doc_in_lines = []
                for line in lines:
                    if line is not '\n':
                        doc_in_lines.append(line)

                # Retrieve the article ID, which is the first word on the line.
                file_id = str(file)
                # Maintain a list of all document IDs.
                doc_names.append(file_id)

                # 'shinglesInDoc' will hold all of the unique shingle IDs present in the
                # current document. If a shingle ID occurs multiple times in the document,
                # it will only appear once in the set (this is a property of Python sets).
                shingles = set()

                # For each line in the document...
                # Construct the shingle text by combining three words together.
                for line in doc_in_lines:

                    shingle = self.get_shingles(line, 5)
                    # Hash the shingle to a 32-bit integer.

                    for shin in shingle:
                        crc = binascii.crc32(shin.encode()) & 0xffffffff
                        # Add the hash value to the list of shingles for the current document.
                        # Note that set objects will only add the value to the set if the set
                        # doesn't already contain it.
                        shingles.add(crc)

                # Store the completed list of shingles for this document in the dictionary.
                global_shingles[file_id] = shingles


if __name__ == "__main__":
    shingling = Shingling(5)
    shingling.run()
