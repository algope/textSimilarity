# coding=utf-8
from __future__ import division

import binascii
import codecs
import os
from itertools import islice, chain


class Shingling:
    """class Shingling that constructs k–shingles of a given length k (e.g., 10) from a given document, computes a
           hash value for each unique shingle, and represents the document in the form of an ordered set of its hashed
           k-shingles. """

    def __init__(self, length):
        self.k = length

    def run(self):
        return self.shingling()

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
        # Dictionary to store collections of shingles per document.
        global_shingles = {}

        for file in os.listdir('./data'):

            with codecs.open('./data/' + file, encoding="utf-8") as f:

                # Read all lines (except first one since it is the heading of the article)
                lines = f.readlines()[1:]
                doc_in_lines = []
                for line in lines:
                    if line is not '\n':
                        doc_in_lines.append(line)

                # Get the file name for indexing in the dictionary.
                file_id = str(file)

                # Storing the shingles as a set
                shingles = set()

                for line in doc_in_lines:

                    shingle = self.get_shingles(line, self.k)

                    for shin in shingle:
                        # Hashing and storing the shingle
                        crc = binascii.crc32(shin.encode('utf-8')) & 0xffffffff
                        shingles.add(crc)

                global_shingles[file_id] = shingles

        return global_shingles
