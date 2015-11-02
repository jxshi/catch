"""Dataset with 'Human immunodeficiency virus 2' sequences.

A dataset with 43 'Human immunodeficiency virus 2' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from hybseldesign.datasets import GenomesDatasetSingleChrom

__author__ = 'Hayden Metsky <hayden@mit.edu>'


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/hiv2.fasta", relative=True)
sys.modules[__name__] = ds