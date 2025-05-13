#!/bin/bash

setupATLAS
lsetup "root recommended"

mkdir $1

python pdf_maker.py
python plots.py
python stats.py