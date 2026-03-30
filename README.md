# Fasta-analysis
# FASTA Analysis Pipeline

## Description
This pipeline reads a FASTA file and calculates:
- Sequence length
- GC count
- GC percentage

It also filters sequences based on:
- Length > 20
- GC% > 40

## Input
FASTA file

## Output
CSV file with:
ID, Length, GC_Count, GC_Percent, Status

## Run
python fasta_pipeline.py test.fasta
