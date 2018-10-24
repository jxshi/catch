"""Dataset with 'Gyrovirus GyV3' sequences.

A dataset with 3 'Gyrovirus GyV3' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/gyrovirus_gyv3.fasta.gz", relative=True)
sys.modules[__name__] = ds