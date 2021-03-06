"""Dataset with 'Influenza C virus [segment 7]' sequences.

A dataset with 177 'Influenza C virus [segment 7]' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/influenza_c_segment7.fasta.gz", relative=True)
sys.modules[__name__] = ds
