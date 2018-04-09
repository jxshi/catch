"""Dataset with 'Influenza A virus [segment 5]' sequences.

A dataset with 21336 'Influenza A virus [segment 5]' sequences.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom

__author__ = 'Hayden Metsky <hayden@mit.edu>'


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/influenza_a_segment5.fasta.gz", relative=True)
sys.modules[__name__] = ds